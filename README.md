# altinn-model-publisher
Transforms Altinn 2.0 models (seres) to modelldcat-ap-no compliant models and expose the collection

## Develop and run locally
### Requirements
- [pyenv](https://github.com/pyenv/pyenv) (recommended)
- [poetry](https://python-poetry.org/)
- [nox](https://nox.thea.codes/en/stable/)
- [nox-poetry](https://pypi.org/project/nox-poetry/)

### Install software:
```
% git clone https://github.com/Informasjonsforvaltning/altinn-model-publisher.git
% cd altinn-model-publisher
% pyenv install 3.9.0
% pyenv local 3.9.0
% pip install poetry==1.1.3
% pip install nox==2020.8.22
% pip install nox-poetry==0.5.0
% poetry install
```
### Environment variables
To run the service locally, you need to supply a set of environment variables. A simple way to solve this is to supply a .env file in the root directory.

```
```
### Running the API locally
 Start the endpoint:
```
% poetry shell
% FLASK_APP=altinn_model_publisher FLASK_ENV=development flask run --port=8080
```
## Running the API in a wsgi-server (gunicorn)
```
% poetry shell
% gunicorn  --chdir src "altinn_model_publisher:create_app()"  --config=src/altinn_model_publisher/gunicorn_config.py
```
## Running the wsgi-server in Docker
To build and run the api in a Docker container:
```
% docker build -t digdir/altinn-model-publisher:latest .
% docker run --env-file .env -p 8080:8080 -d digdir/altinn-model-publisher:latest
```
The easier way would be with docker-compose:
```
docker-compose up --build
```
## Running tests
We use [pytest](https://docs.pytest.org/en/latest/) for contract testing.

To run linters, checkers and tests:
```
% nox
```

## Updating mock data

1. Set API_URL env variable to `http://0.0.0.0:8000`
2. Start wiremock with `docker-compose up`
2. Go to `http://0.0.0.0:8000/__admin/recorder/` and start recording with target url 
3. Start the application with flask or gunicorn and run an http POST request to /update
4. Stop recording
