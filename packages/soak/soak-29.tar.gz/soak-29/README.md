# soak
Process aridity templates en masse, like Helm but much more DRY

## Advantages
* Single sourcing of config i.e. DRY
* No need for all of your team to know Helm's many conventions
* Terraform native customisation is limited and verbose, and the override mechanism is another convention
* Multiple instances of your microservice without hacks
* Extensible via Python code

## Install
These are generic installation instructions.

### To use, permanently
The quickest way to get started is to install the current release from PyPI:
```
pip3 install --user soak
```

### To use, temporarily
If you prefer to keep .local clean, install to a virtualenv:
```
python3 -m venv venvname
venvname/bin/pip install -U pip
venvname/bin/pip install soak
. venvname/bin/activate
```

## Commands

### soak
Process aridity templates as per all soak.arid configs in directory tree.
