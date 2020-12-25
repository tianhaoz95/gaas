#!/bin/bash

pip install -r requirements.txt

python -m gaas.cli --action system_check
