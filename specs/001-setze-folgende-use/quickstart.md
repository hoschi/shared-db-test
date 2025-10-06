# Quickstart: Running the Schema Isolation Tests

This guide provides the steps to set up the environment and run the test suite for the Hybrid Prefix-Schema Pattern implementation.

## Prerequisites
- Python 3.11+
- Poetry for dependency management
- Docker and Docker Compose for running a PostgreSQL instance

## Setup
1. **Clone the repository:**
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install dependencies:**
   ```bash
   poetry install
   ```

3. **Start the PostgreSQL database:**
   ```bash
   docker-compose up -d
   ```

4. **Run database migrations:**
   The test setup will handle the creation of schemas and tables automatically.

## Running the Tests
The test suite is organized into three main categories: unit, integration, and performance.

### Run all tests:
```bash
pytest
```

### Run unit tests:
```bash
pytest tests/unit
```

### Run integration tests:
```bash
pytest tests/integration
```

### Run performance tests:
```bash
pytest tests/performance
```

## Expected Outcome
When the tests are run, you should see output from `pytest` indicating the status of each test (passing, failing, or skipped). The test suite is designed to verify the schema isolation, and the output will show the results of these checks. A successful test run will show all tests passing, confirming that the schema isolation is working as expected. The performance tests will output metrics on schema switching overhead and concurrent load performance.
