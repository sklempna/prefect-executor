#!/bin/bash

apt install -y unixodbc libpq-dev
pip install -r executor/requirements.txt

prefect work-pool create --type process executor-pool
prefect --no-prompt deploy executor/flows/test_flow.py:test_function --name test-flow --pool executor-pool 
prefect worker start --pool executor-pool