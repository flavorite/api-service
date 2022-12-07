# api-service - OpenAPI generated FastAPI server

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0
- Build package: org.openapitools.codegen.languages.PythonFastAPIServerCodegen

## Requirements.

Python >= 3.7

## Installation & Usage

To run the server, please execute the following from the root directory:

```bash
pip3 install -r requirements.txt
uvicorn openapi_server.main:app --host 0.0.0.0 --port 8080
```

and open your browser at `http://localhost:8080/docs/` to see the docs.

## Running with Docker

To run the server on a Docker container, please execute the following from the root directory:

```bash
echo "AWS_ACCESS_KEY_ID=foo\nAWS_SECRET_ACCESS_KEY=bar\nAWS_DEFAULT_REGION=us-east-1\nAWS_DYNAMODB_HOST=http://host.docker.internal:4566" > localstack.env
```

```bash
docker-compose up --build
```

## Tests

To run the tests:

```bash
pip3 install pytest
PYTHONPATH=. pytest tests
```
