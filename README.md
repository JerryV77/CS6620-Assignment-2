# CS6620-Assignment-2

## REST API

This project is a REST API with endpoints for GET, POST, PUT, and DELETE verbs, which built using Python's `http.server` module. It supports basic CRUD operations and includes Docker configurations for running the API and testing it.

## Prerequisites

- Docker: Make sure Docker is installed on your machine. You can download it from [here](https://www.docker.com/get-started).

## Building and Running the REST API

1. **Build the Docker image for the REST API:**
   Navigate to the project root directory and run the following command:
   ```
   docker build -t example_rest_api .
   ```
2. **Run the Docker container for the REST API:**
   
   Navigate to the project root directory and run the following command:
   ```
   docker run -p 8000:8000 example_rest_api
   ```
   This will start the REST API and map port 8000 as default on your host to port 8000 in the container. The API will be accessible at http://localhost:8000/api/items.

## Run the tests

1. **Build the Docker image for the tests:**
   Navigate to the project root directory and run the following command:
   ```
   docker build -f Dockerfile.test -t example_rest_api_test .
   ```
2. **Run the Docker container for the tests:**
   ```
   docker run example_rest_api_test
   ```
   This will run the tests and exit with a zero status if the tests pass and a non-zero status if the tests fail.
