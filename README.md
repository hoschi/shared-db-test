# Hybrid Prefix-Schema Pattern Test Suite

This project provides a comprehensive test suite for a database access system that uses a hybrid prefix-schema pattern to enforce schema isolation in a multi-tenant application. It is built with Python, FastAPI, and SQLAlchemy.

## Overview

The core of this project is a schema-aware database layer that allows a single FastAPI application to serve multiple tenants, each with its own isolated database schema. The test suite is designed to verify:

- **Schema Isolation**: Data created in one tenant's schema is not accessible from another.
- **Data Integrity**: Foreign key relationships and other constraints are correctly enforced within each schema.
- **Performance**: The overhead of schema switching is measured and baselined.

## Getting Started

### Prerequisites

- Python 3.11+
- Poetry for dependency management

### Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    cd <repository-directory>
    ```

2.  **Install dependencies:**
    ```bash
    poetry install
    ```

### Running the Application

To run the FastAPI application locally, use the following command:

```bash
poetry run uvicorn src.main:app --reload
```

The application will be available at `http://127.0.0.1:8000`.

## Testing

The test suite is designed to be run in a CI environment using GitHub Actions, but it can also be run locally with a running PostgreSQL instance.

### CI Testing with GitHub Actions

The primary method for running the test suite is through the GitHub Actions workflow defined in `.github/workflows/test.yml`. This workflow automatically:

1.  Checks out the code.
2.  Sets up a Python environment and installs dependencies.
3.  Starts a PostgreSQL service container.
4.  Runs the full `pytest` suite, including integration tests against the PostgreSQL service.
5.  Reports test coverage, which must be at least 95%.

The workflow is triggered on every `push` event.

### Local Testing

To run the tests locally, you must have a PostgreSQL instance running and configured with the following credentials:

-   **User**: `user`
-   **Password**: `password`
-   **Database**: `testdb`
-   **Host**: `localhost`
-   **Port**: `5432`

You can start a compatible PostgreSQL instance using the provided `docker-compose.yml` file:

```bash
docker compose up -d
```

Once the database is running, you can run the tests:

**Run all tests:**

```bash
poetry run pytest
```

**Run only unit tests (no database required):**

```bash
poetry run pytest tests/unit
```

### Expected Outcome

When the tests are run, `pytest` will output the status of each test. A successful run will show all tests passing, confirming that the schema isolation and other features are working as expected. The test coverage report will also be displayed, and it must meet the 95% threshold for the build to pass in the CI environment.