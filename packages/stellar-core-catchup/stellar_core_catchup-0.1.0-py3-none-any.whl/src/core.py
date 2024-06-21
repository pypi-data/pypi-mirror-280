import concurrent.futures
import dataclasses
import json
import os
import subprocess
import threading
import urllib.request
from enum import Enum
from shlex import split
from typing import List, Tuple

from dataclasses_json import dataclass_json
from jinja2 import Environment, FileSystemLoader

LEDGER_PRE_HISTORY = 64
LEDGER_PER_JOB = int(os.environ.get("LEDGER_PER_JOB", str(LEDGER_PRE_HISTORY * 2000)))
DEFAULT_DB_NAME = "postgres"
CATCH_DB_NAME = "stellar_catchup_{:04d}"
STELLAR_CORE_PORT = 12000

CONFIG_FILE_LOCK = threading.Lock()

# Horizon URLs
PUBLIC_HORIZON = "https://horizon.stellar.org"
TESTNET_HORIZON = "https://horizon-testnet.stellar.org"

# Stellar Core commands
STELLAR_INIT_DB_COMMAND = "/usr/bin/stellar-core --conf {conf_file} new-db"
STELLAR_INIT_HISTORY_COMMAND = "/usr/bin/stellar-core --conf {conf_file} new-hist local"
STELLAR_CATCHUP_COMMAND = "/usr/bin/stellar-core --conf {conf_file} catchup {destination_ledger}/{ledger_count}"
STELLAR_PUBLISH_COMMAND = "/usr/bin/stellar-core --conf {conf_file} publish"

DB_STATE_TABLES = [
    "ban",
    "offers",
    "peers",
    "publishqueue",
    "pubsub",
    "quoruminfo",
    "scphistory",
    "scpquorums",
    "storestate",
]
DB_HISTORY_TABLES = [
    "ledgerheaders",
    "txfeehistory",
    "txhistory",
    "txsethistory",
    "upgradehistory",
]


class JobFailedException(Exception):
    def __init__(self, job_id: int):
        self.job_id = job_id
        super().__init__(f"Job {job_id} failed")


class JobStatus(Enum):
    """Enum class for the job status."""

    PENDING = "pending"
    DONE = "done"
    FAILED = "failed"


@dataclass_json
@dataclasses.dataclass
class CatchUpJob:
    """Data class for a catch job.

    :param start_ledger: The start ledger number (include)
    :param destination_ledger: The destination ledger number (include)
    :param ledger_count: The number of ledgers to sync
    :param database_name: The database name
    :param log_dir: The log directory
    :param bucket_dir: The bucket directory
    :param history_dir: The history directory
    :param http_port: The HTTP port
    :param status: The job status
    """

    id: int
    start_ledger: int
    destination_ledger: int
    ledger_count: int
    database_name: str
    log_dir: str
    bucket_dir: str
    history_dir: str
    config_file_path: str
    http_port: int
    status: JobStatus


class Network(Enum):
    """Enum class for Stellar network."""

    PUBNET = "public"
    TESTNET = "testnet"


@dataclass_json
@dataclasses.dataclass
class Config:
    """Data class for the configuration.

    :param db_host: The database host
    :param db_port: The database port
    :param db_user: The database user
    :param db_password: The database password
    :param node_seed: The node seed
    :param network: The Stellar network
    :param workers: The number of parallel workers
    :param data_dir: The data directory
    :param history_dir: The history directory
    :param destination_ledger: The destination ledger
    :param catchup_jobs: The catchup
    """

    db_host: str
    db_port: str
    db_user: str
    db_password: str
    node_seed: str
    network: Network
    workers: int
    data_dir: str
    history_dir: str
    destination_ledger: int
    catchup_jobs: List[CatchUpJob]


def save_config(config: Config, path: str):
    data_dict = config.to_dict(config)
    # write the data to json file
    with open(path, "w") as f:
        json.dump(data_dict, f, indent=2)


def load_config(path: str) -> Config:
    # read the data from json file
    with open(path, "r") as f:
        data_dict = json.load(f)
    return Config.from_dict(data_dict)


def update_job_status(config_path: str, job_id: int, status: JobStatus):
    with CONFIG_FILE_LOCK:
        config = load_config(config_path)
        for job in config.catchup_jobs:
            if job.id == job_id:
                job.status = status
                break
        save_config(config, config_path)


def get_latest_catchable_ledger_number(network: Network):
    """Get the latest catchable ledger number from the Horizon server.

    :param network: The network you want to get the latest ledger number
    :return: The latest ledger number
    """
    url = PUBLIC_HORIZON if network == Network.PUBNET else TESTNET_HORIZON
    with urllib.request.urlopen(url) as response:
        data = json.load(response)
        ledger = data["history_latest_ledger"]
        return ledger // LEDGER_PRE_HISTORY * LEDGER_PRE_HISTORY


def get_catchup_jobs(
    destination_ledger: int, data_dir: str, history_dir: str
) -> List[CatchUpJob]:
    """Get the job list for parallel catchup.

    :param history_dir: The history directory
    :param data_dir: The data directory
    :param destination_ledger: The destination ledger
    :return: The job list
    """
    if destination_ledger % LEDGER_PRE_HISTORY != 0:
        raise ValueError("Invalid destination ledger")
    job_list = []
    start_ledger = 1
    job_id = 1
    while start_ledger < destination_ledger:
        dest_ledger = min(start_ledger - 1 + LEDGER_PER_JOB, destination_ledger)
        ledger_count = dest_ledger - (start_ledger - 1)
        job_id_f = f"{job_id:04d}"
        core_data_dir = os.path.join(data_dir, f"stellar_core_{job_id_f}")
        history_data_dir = os.path.join(history_dir, f"stellar_core_{job_id_f}")
        job_list.append(
            CatchUpJob(
                job_id,
                start_ledger,
                dest_ledger,
                ledger_count,
                CATCH_DB_NAME.format(job_id),
                core_data_dir,
                os.path.join(core_data_dir, "bucket"),
                os.path.join(history_data_dir, "history"),
                os.path.join(core_data_dir, "stellar-core.cfg"),
                STELLAR_CORE_PORT + job_id,
                JobStatus.PENDING,
            )
        )
        start_ledger += LEDGER_PER_JOB
        job_id += 1
    return job_list


def create_database(
    db_host: str, db_port: str, db_user: str, db_password: str, db_name: str
) -> None:
    env = os.environ.copy()
    env["PGPASSWORD"] = db_password
    process = subprocess.Popen(
        split(
            f"psql --username {db_user} --host {db_host} --port {db_port} --dbname {DEFAULT_DB_NAME} -c 'CREATE DATABASE {db_name}'"
        ),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        raise OSError("Create database failed: {}".format(stderr.decode()))


def render_config_template(
    node_seed: str,
    network: Network,
    http_port: int,
    db_host: str,
    db_port: str,
    db_user: str,
    db_password: str,
    db_name: str,
    log_dir: str,
    bucket_dir: str,
    history_dir: str,
) -> str:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    env = Environment(loader=FileSystemLoader(os.path.join(current_dir, "templates")))
    template_name = (
        "stellar-core.cfg.public"
        if network == Network.PUBNET
        else "stellar-core.cfg.testnet"
    )
    context = {
        "http_port": http_port,
        "node_seed": node_seed,
        "db_host": db_host,
        "db_port": db_port,
        "db_user": db_user,
        "db_password": db_password,
        "db_name": db_name,
        "log_dir": log_dir,
        "bucket_dir": bucket_dir,
        "history_dir": history_dir,
    }
    return env.get_template(template_name).render(context)


def start_catchup_worker(job: CatchUpJob) -> int:
    """Start a worker to catch up the ledger.

    :param job: The catch job
    """
    print(f"Job {job.id}, started")

    # Init database
    init_db_command = STELLAR_INIT_DB_COMMAND.format(conf_file=job.config_file_path)
    process = subprocess.Popen(
        split(init_db_command), stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Job {job.id}, init database error: {stderr.decode()}")
        raise JobFailedException(job.id)

    # Init history
    init_history_command = STELLAR_INIT_HISTORY_COMMAND.format(
        conf_file=job.config_file_path
    )
    process = subprocess.Popen(
        split(init_history_command), stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Job {job.id}, init history error: {stderr.decode()}")
        raise JobFailedException(job.id)

    # Catchup
    catchup_command = STELLAR_CATCHUP_COMMAND.format(
        conf_file=job.config_file_path,
        destination_ledger=job.destination_ledger,
        ledger_count=job.ledger_count,
    )
    process = subprocess.Popen(
        split(catchup_command), stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Job {job.id}, catchup error: {stderr.decode()}")
        raise JobFailedException(job.id)

    # Publish
    publish_command = STELLAR_PUBLISH_COMMAND.format(conf_file=job.config_file_path)
    process = subprocess.Popen(
        split(publish_command), stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Job {job.id}, publish error: {stderr.decode()}")
        raise JobFailedException(job.id)
    print(f"Job {job.id}, finished")
    return job.id


def start_catchup(config_path: str):
    config = load_config(config_path)
    jobs = [job for job in config.catchup_jobs if job.status != JobStatus.DONE]
    with concurrent.futures.ProcessPoolExecutor(max_workers=config.workers) as executor:
        futures = [executor.submit(start_catchup_worker, job) for job in jobs]
        for future in concurrent.futures.as_completed(futures):
            try:
                job_id = future.result()
                update_job_status(config_path, job_id, JobStatus.DONE)
            except JobFailedException as e:
                update_job_status(config_path, e.job_id, JobStatus.FAILED)


def _init_dir(d: str) -> str:
    data_dir = os.path.abspath(d)
    if not os.path.exists(data_dir):
        os.makedirs(data_dir)

    if not os.path.isdir(data_dir):
        raise ValueError(f"Error: {data_dir} is not a directory")

    if not os.access(data_dir, os.R_OK | os.W_OK):
        raise ValueError(f"Error: No read/write permission for directory: {data_dir}")
    return data_dir


def init_data_and_history_dir(data_dir: str, history_dir: str) -> Tuple[str, str]:
    """Initialize the data and history directories.

    :param data_dir: The data directory
    :param history_dir: The history directory
    """
    return _init_dir(data_dir), _init_dir(history_dir)


def init_databases(
    db_host: str,
    db_port: str,
    db_user: str,
    db_password: str,
    job_list: List[CatchUpJob],
) -> None:
    """Initialize the databases."""
    for job in job_list:
        create_database(db_host, db_port, db_user, db_password, job.database_name)


def check_ledger_consistency(config: Config):
    env = os.environ.copy()
    env["PGPASSWORD"] = config.db_password

    for idx in range(len(config.catchup_jobs)):
        if idx == 0:
            continue
        process = subprocess.Popen(
            split(
                f"psql --username {config.db_user} --host {config.db_host} --port {config.db_port} "
                f"--dbname {config.catchup_jobs[idx].database_name} -c 'select prevhash as result from ledgerheaders where ledgerseq = {config.catchup_jobs[idx].start_ledger}'"
            ),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            raise OSError("Check ledger consistency failed")

        prev_process = subprocess.Popen(
            split(
                f"psql --username {config.db_user} --host {config.db_host} --port {config.db_port} "
                f"--dbname {config.catchup_jobs[idx - 1].database_name} -c 'select ledgerhash as result from ledgerheaders where ledgerseq = {config.catchup_jobs[idx - 1].destination_ledger}'"
            ),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True,
            env=env,
        )
        prev_stdout, prev_stderr = prev_process.communicate()
        if prev_process.returncode != 0:
            raise OSError("Check ledger consistency failed")

        if stdout.strip() != prev_stdout.strip():
            raise OSError(
                "Ledger inconsistency detected, please check the database, job {} and job {}".format(
                    idx, idx - 1
                )
            )


def create_stellar_core_config_files(
    *,
    node_seed: str,
    network: Network,
    db_host: str,
    db_port: str,
    db_user: str,
    db_password: str,
    job_list: List[CatchUpJob],
) -> None:
    """Create the Stellar Core configuration files."""
    for job in job_list:
        config = render_config_template(
            node_seed,
            network,
            job.http_port,
            db_host,
            db_port,
            db_user,
            db_password,
            job.database_name,
            job.log_dir,
            job.bucket_dir,
            job.history_dir,
        )
        directory = os.path.dirname(job.config_file_path)
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(job.config_file_path, "w") as f:
            f.write(config)


def merge_db(config: Config):
    env = os.environ.copy()
    env["PGPASSWORD"] = config.db_password

    # Create a new database with the first job db as template, it includes job 1 db data
    merged_db = "stellar_catchup_merged"
    process = subprocess.Popen(
        split(
            f"psql --username {config.db_user} --host {config.db_host} --port {config.db_port} --dbname {DEFAULT_DB_NAME} -c 'CREATE DATABASE {merged_db} template {config.catchup_jobs[0].database_name}'"
        ),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env,
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        raise OSError("Create database failed: {}".format(stderr.decode()))

    for job in config.catchup_jobs[1:]:
        for table in DB_HISTORY_TABLES:
            command = f"COPY (SELECT * FROM {table} WHERE ledgerseq >= {job.start_ledger} AND ledgerseq <= {job.destination_ledger}) TO STDOUT WITH (FORMAT BINARY)"
            print(f"Running psql command: {command}")
            src_process = subprocess.Popen(
                split(
                    f"psql --username {config.db_user} --host {config.db_host} --port {config.db_port} "
                    f"--dbname {job.database_name} -c '{command}'"
                ),
                env=env,
                stdout=subprocess.PIPE,
            )
            dest_process = subprocess.Popen(
                split(
                    f"psql --username {config.db_user} --host {config.db_host} --port {config.db_port} "
                    f"--dbname {merged_db} -c 'COPY {table} FROM STDIN WITH (FORMAT BINARY)'"
                ),
                env=env,
                stdin=src_process.stdout,
                stdout=subprocess.PIPE,
            )
            src_process.stdout.close()
            out, err = dest_process.communicate()
            if dest_process.returncode != 0:
                raise OSError(err.decode("utf-8"))

    # Copy state tables
    for table in DB_STATE_TABLES:
        process = subprocess.Popen(
            split(
                f"psql --username {config.db_user} --host {config.db_host} --port {config.db_port} "
                f"--dbname {merged_db} -c 'TRUNCATE TABLE {table}'"
            ),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
        )
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            raise OSError(f"Truncate table failed: {stderr.decode()}")

        src_process = subprocess.Popen(
            split(
                f"psql --username {config.db_user} --host {config.db_host} --port {config.db_port} "
                f"--dbname {config.catchup_jobs[-1].database_name} -c 'COPY {table} TO STDOUT WITH (FORMAT BINARY)'"
            ),
            env=env,
            stdout=subprocess.PIPE,
        )
        dest_process = subprocess.Popen(
            split(
                f"psql --username {config.db_user} --host {config.db_host} --port {config.db_port} "
                f"--dbname {merged_db} -c 'COPY {table} FROM STDIN WITH (FORMAT BINARY)'"
            ),
            env=env,
            stdin=src_process.stdout,
            stdout=subprocess.PIPE,
        )
        src_process.stdout.close()
        out, err = dest_process.communicate()
        if dest_process.returncode != 0:
            raise OSError(err.decode("utf-8"))


def merge_history(config: Config):
    job_list = config.catchup_jobs
    dest_path = os.path.join(config.history_dir, "merged_history")
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    for job in job_list:
        command = f"cp -r {job.history_dir}/ {dest_path}"
        process = subprocess.Popen(
            split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            print(f"Merge history error: {stderr.decode()}")
            raise OSError("Merge history failed")
        command = f"rm -rf {job.history_dir}"
        process = subprocess.Popen(
            split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE
        )
        stdout, stderr = process.communicate()
        if process.returncode != 0:
            print(f"Delete history error: {stderr.decode()}")
            raise OSError("Delete history failed")


def merge_bucket(config: Config):
    job_list = config.catchup_jobs
    dest_path = os.path.join(config.data_dir, "merged_bucket")
    if not os.path.exists(dest_path):
        os.makedirs(dest_path)
    last_job = job_list[-1]
    command = f"rsync -a {last_job.bucket_dir}/ {dest_path}"
    process = subprocess.Popen(
        split(command), stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    stdout, stderr = process.communicate()
    if process.returncode != 0:
        print(f"Merge bucket error: {stderr.decode()}")
        raise OSError("Merge bucket failed")
