# QA Database Testing

Automated database testing project developed with Python, Pytest and SQLite.

The project focuses on validating database operations, data integrity and expected behavior through automated tests.

## Technologies

- Python
- Pytest
- SQLite
- SQL
- Git / GitHub

## Database

This project uses SQLite as a lightweight relational database.

The database contains a `customers` table with:

| Field | Type | Constraints |
|---|---|---|
| `id` | INTEGER | PRIMARY KEY |
| `name` | TEXT | NOT NULL |
| `email` | TEXT | NOT NULL, UNIQUE |
| `phone` | TEXT | NOT NULL, UNIQUE |

## Test Coverage

The test suite currently contains **9 automated tests** covering positive and negative scenarios.

### Data Integrity
- Duplicate phone number
- Duplicate email
- Missing required name

### Data Retrieval
- Retrieve complete customer record
- Retrieve a specific customer email
- Retrieve a nonexistent customer

### Create and Verify
- Create a customer and verify stored data

### Update
- Update customer phone and verify the result

### Delete
- Delete a customer and verify it no longer exists

## Test Architecture

Tests
  ↓
Pytest Fixture
  ↓
Database Connection
  ↓
SQLite
  ↓
SQL Query
  ↓
Result
  ↓
Assertions

The database connection is centralized in `db_connection.py`.

The Pytest fixture provides the database cursor to the tests and handles transaction rollback and connection cleanup after each test.

## Project Structure

```text
qa-database-testing/
├── database/
│   ├── __init__.py
│   ├── db_connection.py
│   └── setup_database.py
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   └── test_customers.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md

## Setup

Clone the repository:

```bash
git clone https://github.com/danigatoR/qa-database-testing.git
```

Create and activate a virtual environment:

```bash
python -m venv .venv
.venv\Scripts\activate
```

Install the project dependencies:

```bash
pip install -r requirements.txt
```

## Running Tests

Run the complete test suite:

```bash
pytest
```

Run tests with verbose output:

```bash
pytest -v
```

Run a specific test:

```bash
pytest tests/test_customers.py::test_get_customers -v
```

The test suite currently contains **9 automated tests**.

## Purpose

This project was created to practice and demonstrate database testing using Python, Pytest and SQL.

The project focuses on:

- Validating database operations.
- Testing data integrity and constraints.
- Covering positive and negative scenarios.
- Verifying CRUD operations.
- Using Pytest fixtures for test setup and cleanup.
- Working with SQL queries and SQLite.
- Validating database state through automated assertions.