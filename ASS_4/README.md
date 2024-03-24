# Assignment 4: Flask App Containerization and Continuous Integration

## Overview

This repository contains a Flask application for text scoring, which has been containerized using Docker. Additionally, it incorporates a continuous integration setup with a pre-commit hook to ensure tests are passed before any code is committed to the 'main' branch.

## Project Structure

- `best_models/`: Pre-trained model files like LightGBM, Logistic Regression, and Naive Bayes.
- `data/`: Data files including raw, test, and training datasets in CSV format.
- `hooks/`: Custom Git hooks for continuous integration.
- `src/`: The source code for the Flask application, Docker configurations, and test scripts.

## Containerization with Docker

To containerize the Flask application, follow these steps:

1. **Build the Docker image:**

   ```sh
   cd src
   docker build -t flask_app .
   ```
2. **Run the Docker container:**

   ```sh
   docker run -d -p 5000:5000 flask_app
   ```

The Flask app will now be accessible at `http://localhost:5000/score`.

## Testing

The `test_code.py` file contains tests for the application. To run these tests within the Docker container, use the `test_docker` function.

## Generating Coverage Report

Generate a coverage report using pytest with the following command:

```sh
pytest --cov=app test_code.py > ../coverage.txt
```


## Accessing and Setting Up the Custom Pre-commit Hook

The repository includes a custom pre-commit hook within the `hooks` directory, which you can set up to run automatically before each commit to the 'main' branch. Follow these steps to access and enable the hook:

1. **Copy the Pre-commit Hook:**
   From the root of your repository, copy the `pre-commit` script from the `hooks` directory to the `.git/hooks` directory:

   ```sh
   cp hooks/pre-commit.txt .git/hooks/pre-commit
   ```
