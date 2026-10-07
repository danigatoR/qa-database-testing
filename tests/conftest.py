import pytest

from database.db_connection import get_connection


@pytest.fixture
def cursor():
    connection = get_connection()
    cursor = connection.cursor()

    yield cursor

    connection.rollback()
    connection.close()