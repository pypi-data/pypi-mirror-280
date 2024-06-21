import sys
import click

from src.core import *


@click.group()
def cli():
    """Efficiently synchronize a Stellar Core validator node"""
    pass


@cli.command()
@click.option("--db-host", required=True, prompt=True, help="Database host")
@click.option(
    "--db-port",
    required=True,
    prompt=True,
    type=int,
    default=3306,
    help="Database port",
)
@click.option("--db-user", required=True, prompt=True, help="Database user")
@click.option(
    "--db-password",
    required=True,
    prompt=True,
    hide_input=True,
    help="Database password",
)
@click.option(
    "--node-seed",
    required=True,
    prompt=True,
    hide_input=True,
    help="Node seed, must be consistent with the seed used by your node.",
)
@click.option(
    "--data-dir",
    required=True,
    prompt=True,
    help="Data directory, we will place all data here except for the history history, "
    "please try to place it on high-speed storage devices",
)
@click.option(
    "--history-dir",
    required=True,
    prompt=True,
    help="History archive directory, we will place the history archive here, "
    "for the public network, it will take a lot of space",
)
@click.option(
    "--network",
    type=click.Choice(["public", "testnet"]),
    default="public",
    help="Network name, public or testnet (default: public)",
)
@click.option(
    "--destination-ledger",
    type=int,
    help="Destination ledger. If not given then sync until the latest ledger.",
)
@click.option(
    "--workers",
    type=int,
    help="The maximum number of processes that can be used to execute the given calls. "
    "If not given then as many worker processes will be created as the machine has processors.",
)
def init(
    db_host,
    db_port,
    db_user,
    db_password,
    node_seed,
    data_dir,
    history_dir,
    network,
    destination_ledger,
    workers,
):
    """Initialize the Stellar Core catchup."""
    click.echo("Initializing the Stellar Core catchup...")

    network = Network(network)

    if not destination_ledger:
        destination_ledger = get_latest_catchable_ledger_number(network)
    else:

        destination_ledger = (
            destination_ledger // LEDGER_PRE_HISTORY * LEDGER_PRE_HISTORY
        )

    if not workers:
        workers = os.cpu_count()

    click.echo("Creating the data and history directories...")
    data_dir_abspath, history_dir_abspath = init_data_and_history_dir(
        data_dir, history_dir
    )

    catchup_cfg_path = os.path.join(data_dir_abspath, "catchup-config.json")

    if os.path.exists(catchup_cfg_path):
        click.echo(
            "catchup-config.json found, seems the catchup has been initialized. "
            f"If you want to reinitialize, please delete {data_dir_abspath} and {history_dir_abspath} first."
        )
        sys.exit(1)

    catchup_jobs = get_catchup_jobs(
        destination_ledger, data_dir_abspath, history_dir_abspath
    )
    click.echo("Creating the databases...")
    init_databases(db_host, db_port, db_user, db_password, catchup_jobs)
    click.echo("Creating the stellar-core configuration files...")
    create_stellar_core_config_files(
        node_seed=node_seed,
        network=network,
        db_host=db_host,
        db_port=db_port,
        db_user=db_user,
        db_password=db_password,
        job_list=catchup_jobs,
    )
    click.echo("Creating catchup task configuration file...")
    cfg = Config(
        db_host=db_host,
        db_port=db_port,
        db_user=db_user,
        db_password=db_password,
        node_seed=node_seed,
        network=network,
        workers=workers,
        data_dir=data_dir_abspath,
        history_dir=history_dir_abspath,
        destination_ledger=destination_ledger,
        catchup_jobs=catchup_jobs,
    )
    save_config(cfg, catchup_cfg_path)
    click.echo("Initialization completed.")
    click.echo(f"Created, file path: {catchup_cfg_path}")
    click.echo(f"Destination ledger: {destination_ledger}")
    click.echo(f"Catchup jobs count: {len(catchup_jobs)}")
    click.echo(
        f"Port {STELLAR_CORE_PORT + 1} to {STELLAR_CORE_PORT + len(catchup_jobs)} are used for the catchup."
    )
    click.echo(f"Please run the following command to start the catchup:")
    click.echo(f"   stellar-core-catchup catchup --config {catchup_cfg_path}")


@cli.command()
@click.option("--config", help="Configuration file path")
def catchup(config):
    """Start the Stellar Core catchup."""
    click.echo("Starting the Stellar Core catchup...")
    start_catchup(config)


@cli.command()
@click.option("--config", help="Configuration file path")
def merge(config):
    """Merge the Stellar Core catchup results."""
    click.echo("Merging the Stellar Core catchup results...")
    config = load_config(config)

    if any(job.status != JobStatus.DONE for job in config.catchup_jobs):
        click.echo("Some jobs are not done, please make sure all jobs are done.")
        sys.exit(1)

    click.echo("Checking the ledger consistency...")
    check_ledger_consistency(config)
    click.echo("Merging the databases...")
    merge_db(config)
    click.echo("Finished, the merged database called `stellar_catchup_merged`.")
    click.echo("Merging the bucket directories...")
    merge_bucket(config)
    click.echo(
        f"Finished, you can find the merged bucket directory in "
        f"the {os.path.join(config.data_dir, 'merged_bucket')} directory."
    )
    click.echo("Merging the history tables...")
    merge_history(config)
    click.echo(
        f"Finished, you can find the merged history directory in "
        f"the {os.path.join(config.history_dir, 'merged_history')} directory."
    )
    click.echo("Merging completed.")
