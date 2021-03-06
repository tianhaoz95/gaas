# GAAS

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/tianhaoz95/gaas)

## Getting Started

### Prerequisites

* Linux/MacOS (package version might be incompatible with Windows).
* Python 3.6+

### Prepare Workspace

```bash
# (Optional) If no virtualenv has been
# installed globally.
pip install virtualenv

# Clone the repository.
git clone git@github.com:[username]/gaas.git # Replace [username]

# Create a virtualenv in the repository.
cd gaas && python -m virtualenv .venv

# Activate the virtual environment and install dependencies.
source .venv/bin/activate && pip install -r requirements.txt
```

### CLI options

Use the following command to check available CLI options:

```bash
python -m gaas.cli --help
```

#### Train model

```bash
python -m gaas.cli --action train --app image_coloring
```

## Useful links

* [Credential repository](https://github.com/tianhaoz95/gaas-credentials)
