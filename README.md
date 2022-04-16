# AIRE LOGIC TECH TEST

## Loading project

This is intended to be run on most Linux Distros.... ubuntu 20.04 LTS in my case.

### installation

#### Locally
Requires [poetry](https://pypi.org/project/poetry/) to run... think of pip but better<br />
`poetry install`

#### Docker

example:<br />
build from basedir: `docker build -t techtest --rm -f .docker/Dockerfile .`<br />
run: `docker run -it --name tech_test --rm techtest`

##### docker-compose
`docker-compose -f .docker/docker-compose.yml up`

How to run? <br />
![image](https://user-images.githubusercontent.com/38649437/163672131-d38fcb4f-af4b-4a1a-aeba-670140a409ad.png)


## Caveats

I takes forever due to rate limiting and speed of apis


### Tests

To run tests use the following from the base direction `airelogic_tech_test`:<br />
```
python -m pytest tests/
```