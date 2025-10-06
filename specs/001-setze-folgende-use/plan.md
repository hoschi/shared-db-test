# Implementation Plan: Hybrid Prefix-Schema Pattern Test Cases

**Branch**: `001-setze-folgende-use` | **Date**: 2025-10-06 | **Spec**: [link](./spec.md)
**Input**: Feature specification from `/specs/001-setze-folgende-use/spec.md`

## Execution Flow (/plan command scope)
```
1. Load feature spec from Input path
   → If not found: ERROR "No feature spec at {path}"
2. Fill Technical Context (scan for NEEDS CLARIFICATION)
   → Detect Project Type from file system structure or context (web=frontend+backend, mobile=app+api)
   → Set Structure Decision based on project type
3. Fill the Constitution Check section based on the content of the constitution document.
4. Evaluate Constitution Check section below
   → If violations exist: Document in Complexity Tracking
   → If no justification possible: ERROR "Simplify approach first"
   → Update Progress Tracking: Initial Constitution Check
5. Execute Phase 0 → research.md
   → If NEEDS CLARIFICATION remain: ERROR "Resolve unknowns"
6. Execute Phase 1 → contracts, data-model.md, quickstart.md, agent-specific template file (e.g., `CLAUDE.md` for Claude Code, `.github/copilot-instructions.md` for GitHub Copilot, `GEMINI.md` for Gemini CLI, `QWEN.md` for Qwen Code or `AGENTS.md` for opencode).
7. Re-evaluate Constitution Check section
   → If new violations: Refactor design, return to Phase 1
   → Update Progress Tracking: Post-Design Constitution Check
8. Plan Phase 2 → Describe task generation approach (DO NOT create tasks.md)
9. STOP - Ready for /tasks command
```

## Summary
The feature is to implement a comprehensive test suite for a database access system that uses a hybrid prefix-schema pattern to enforce schema isolation. The technical approach involves using FastAPI, SQLAlchemy 2.0, and pytest to create a series of integration and performance tests that verify data integrity, security, and performance across different application domains.

## Technical Context
**Language/Version**: Python 3.11
**Primary Dependencies**: FastAPI, SQLAlchemy 2.0, Alembic, pytest, asyncpg
**Storage**: PostgreSQL
**Testing**: pytest
**Target Platform**: Linux server
**Project Type**: Single project (backend)
**Performance Goals**: Measure and baseline schema switching overhead and concurrent load performance.
**Constraints**: Ensure strict schema isolation.
**Scale/Scope**: Small data volume (< 1 GB per schema) for the first year.

## Constitution Check
*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

- **FCIS**: The proposed structure with `src/core` and `src/shell` aligns with this principle.
- **Strict Typing**: The use of SQLAlchemy 2.0 and FastAPI encourages strict typing.
- **Functional & Immutable**: The services will be implemented as free functions, and data structures will be treated as immutable.
- **Railway Oriented Programming**: The `returns` library will be used for error handling.
- **Data Validation at Boundaries**: Pydantic models will be used for data validation.
- **Dependency Inversion**: Protocols will be used where necessary.
- **Testing**: A comprehensive test suite is the core of this feature.
- **DRY**: Reusable logic will be encapsulated in service functions.
- **Logging**: `Loguru` will be used for structured logging.

## Project Structure

### Documentation (this feature)
```
specs/001-setze-folgende-use/
├── plan.md              # This file (/plan command output)
├── research.md          # Phase 0 output (/plan command)
├── data-model.md        # Phase 1 output (/plan command)
├── quickstart.md        # Phase 1 output (/plan command)
├── contracts/           # Phase 1 output (/plan command)
│   └── api.md
└── tasks.md             # Phase 2 output (/tasks command - NOT created by /plan)
```

### Source Code (repository root)
```
src/
├── notes_system/
│   ├── models.py
│   ├── services.py
│   └── api.py
├── video_analysis/
│   ├── models.py
│   ├── services.py
│   └── api.py
├── core/
│   ├── database.py
│   ├── middleware.py
│   └── config.py
└── shared/
    ├── auth.py
    └── utils.py
tests/
├── unit/
├── integration/
├── performance/
└── fixtures/
```

**Structure Decision**: The project will follow a single project structure with clear separation of concerns for each schema and a core set of shared services.

## Phase 0: Outline & Research
Completed. See `research.md`.

## Phase 1: Design & Contracts
Completed. See `data-model.md`, `contracts/api.md`, and `quickstart.md`.

## Phase 2: Task Planning Approach
*This section describes what the /tasks command will do - DO NOT execute during /plan*

**Task Generation Strategy**:
- Load `.specify/templates/tasks-template.md` as base.
- Generate tasks from the `data-model.md` to create the SQLAlchemy models.
- Generate tasks from the `quickstart.md` and the technical context to create the test suite.
- Create tasks for setting up the database connection, middleware, and configuration.

**Ordering Strategy**:
- TDD order: Tests before implementation.
- Dependency order: Models before services before tests.
- Mark [P] for parallel execution (independent files).

**Estimated Output**: 15-20 numbered, ordered tasks in `tasks.md`.

## Complexity Tracking
*Fill ONLY if Constitution Check has violations that must be justified*

| Violation | Why Needed | Simpler Alternative Rejected Because |
|-----------|------------|-------------------------------------|
| N/A       | N/A        | N/A                                 |

## Progress Tracking
*This checklist is updated during execution flow*

**Phase Status**:
- [x] Phase 0: Research complete (/plan command)
- [x] Phase 1: Design complete (/plan command)
- [x] Phase 2: Task planning complete (/plan command - describe approach only)
- [ ] Phase 3: Tasks generated (/tasks command)
- [ ] Phase 4: Implementation complete
- [ ] Phase 5: Validation passed

**Gate Status**:
- [x] Initial Constitution Check: PASS
- [x] Post-Design Constitution Check: PASS
- [x] All NEEDS CLARIFICATION resolved
- [ ] Complexity deviations documented