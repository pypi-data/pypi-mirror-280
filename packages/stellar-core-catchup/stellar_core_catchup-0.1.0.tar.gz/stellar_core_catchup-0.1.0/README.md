# stellar-core-catchup
Efficiently synchronize a Stellar Core validator node,

> [!WARNING]  
>  This project is under development and not ready for production use.

## Requirements

- Python 3.8+
- Ubuntu 22.04 LTS
- Stellar Core
- PostgreSQL

## Installation

```
pip install stellar-core-catchup
```

## Usage

```
stellar-core-catchup --help
```

- First, you need to run `stellar-core-catchup init` to initialize the configuration file.
- Second, you need to run `stellar-core-catchup catchup` to start the catchup process.
- Finally, you need to run `stellar-core-catchup merge` to merge databases, buckets, and history archives.