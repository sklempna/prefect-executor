## TODO:

- make ports of services configurable via .env

- write custom dockerfile so you don't have to do those nasty installs in set-up-executor.sh

- logguru
- precommit

## DONE:

- configuration (passwords as env-variables, rest via config-file)

## Creating a flow on the executor

- in the directory executor/flows create a python file test_flow.py
- update executor/requirements.txt with the pip requirements
- log into executor docker exec -it pipelines_executor_1 bash
- install requirements pip install -r requirements.txt
- create work-pool `prefect work-pool create my-work-pool` interactively choose the second option
- run `prefect worker start --pool my-work-pool &`
- run `prefect deploy`


## Creating a flow

- mkdir docker-testflow
- inside docker-testflow create directory flows with python file with flow test_flow.py
- inside docker-testflow create dockerfile
- inside docker-testflow create requirements.txt
- log into cli: docker exec -it pipelines_cli_1 bash
- run `prefect work-pool create --type docker my-docker-pool`
- run `prefect worker start --pool my-docker-pool &`
- run `prefect deploy`
- run `exit`
