# Tasks for Hybrid Prefix-Schema Pattern Test Cases

**Feature**: Implement a comprehensive test suite for a database access system that uses a hybrid prefix-schema pattern to enforce schema isolation.

## Phase 1: Setup and Core Infrastructure

### T001: Create Project Structure
**File**: `src/`
**Description**: Create the necessary directories for the project structure, including `src/notes_system`, `src/video_analysis`, `src/core`, `src/shared`, and the `tests` directory with its subdirectories.

### T002: Setup Core Database Connection [P]
**File**: `src/core/database.py`
**Description**: Implement the `SchemaAwareDatabase` class to manage schema-aware database connections using SQLAlchemy 2.0 and `asyncpg`.

### T003: Setup Configuration [P]
**File**: `src/core/config.py`
**Description**: Implement a configuration module to manage database URLs and other settings.

### T004: Setup Schema-Routing Middleware [P]
**File**: `src/core/middleware.py`
**Description**: Implement a FastAPI middleware to handle schema routing based on request headers or other parameters.

### T005: Setup Shared Utilities [P]
**File**: `src/shared/utils.py`
**Description**: Implement any shared utility functions that may be needed across the application.

### T006: Setup Shared Authentication [P]
**File**: `src/shared/auth.py`
**Description**: Implement a basic authentication and user management module to support permission testing.

## Phase 2: Data Models

### T007: Create `notes_system` Models [P]
**File**: `src/notes_system/models.py`
**Description**: Implement the SQLAlchemy models for the `notes_system` schema as defined in `data-model.md`.
**Dependencies**: T001

### T008: Create `video_analysis` Models [P]
**File**: `src/video_analysis/models.py`
**Description**: Implement the SQLAlchemy models for the `video_analysis` schema as defined in `data-model.md`.
**Dependencies**: T001

## Phase 3: Business Logic

### T009: Implement `notes_system` Services [P]
**File**: `src/notes_system/services.py`
**Description**: Implement the business logic for the `notes_system` as free functions.
**Dependencies**: T007

### T010: Implement `video_analysis` Services [P]
**File**: `src/video_analysis/services.py`
**Description**: Implement the business logic for the `video_analysis` as free functions.
**Dependencies**: T008

## Phase 4: API Endpoints

### T011: Create `notes_system` API Endpoints [P]
**File**: `src/notes_system/api.py`
**Description**: Implement the FastAPI endpoints for the `notes_system`.
**Dependencies**: T009

### T012: Create `video_analysis` API Endpoints [P]
**File**: `src/video_analysis/api.py`
**Description**: Implement the FastAPI endpoints for the `video_analysis`.
**Dependencies**: T010

## Phase 5: Testing

### T013: Create Test Fixtures
**File**: `tests/conftest.py`
**Description**: Create `pytest` fixtures for database connections, test users, and other test setup requirements.
**Dependencies**: T002, T006

### T014: Implement Schema Isolation Tests [P]
**File**: `tests/integration/test_schema_isolation.py`
**Description**: Implement the integration tests for schema isolation under parallel access.
**Dependencies**: T013

### T015: Implement Foreign Key Validation Tests [P]
**File**: `tests/integration/test_foreign_key_validation.py`
**Description**: Implement the integration tests for cross-schema foreign key validation.
**Dependencies**: T013

### T016: Implement Permission Isolation Tests [P]
**File**: `tests/integration/test_permission_isolation.py`
**Description**: Implement the integration tests for schema-specific permissions.
**Dependencies**: T013

### T017: Implement Performance Tests [P]
**File**: `tests/performance/test_schema_performance.py`
**Description**: Implement the performance tests for schema switching and concurrent load.
**Dependencies**: T013

## Phase 6: Documentation

### T018: Update README
**File**: `README.md`
**Description**: Replace the content of the `README.md` file with a detailed description of how to set up the environment, run the tests, and what the expected outcome is, based on `quickstart.md`.

## Parallel Execution Examples

The following tasks can be executed in parallel after Phase 1 is complete:

- **Models**: `T007` and `T008`
- **Services**: `T009` and `T010` (after models are complete)
- **API**: `T011` and `T012` (after services are complete)
- **Testing**: `T014`, `T015`, `T016`, and `T017` (after the application code is complete)

Example of running model tasks in parallel:
```bash
# Terminal 1
# (Work on T007: src/notes_system/models.py)

# Terminal 2
# (Work on T008: src/video_analysis/models.py)
```
