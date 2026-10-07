import sqlite3

import pytest


def test_create_customer_with_duplicate_phone(cursor):

    with pytest.raises(sqlite3.IntegrityError):
        cursor.execute("""
            INSERT INTO customers (name, email, phone)
            VALUES ('Laura', 'laura@example.com', '612345678')
        """)


def test_create_customer_with_duplicate_email(cursor):

    with pytest.raises(sqlite3.IntegrityError):
        cursor.execute("""
            INSERT INTO customers (name, email, phone)
        VALUES ('Laura', 'dani@example.com', '69845678')
        """)


def test_create_customer_without_name(cursor):

    with pytest.raises(sqlite3.IntegrityError):
        cursor.execute("""
            INSERT INTO customers (name, email, phone)
            VALUES (NULL, 'laura@example.com', '623456789')
        """)


def test_get_customers(cursor):

    cursor.execute("SELECT * FROM customers")

    rows = cursor.fetchall()

    assert len(rows) == 1

    row = rows[0]

    assert row["id"] == 1
    assert row["name"] == "Daniel"
    assert row["email"] == "dani@example.com"
    assert row["phone"] == "612345678"


def test_create_customer_and_verify_data(cursor):

    cursor.execute("""
        INSERT INTO customers (name, email, phone)
        VALUES ('Laura', 'laura@example.com', '623456789')
    """)

    cursor.execute("""
        SELECT * FROM customers
        WHERE email = 'laura@example.com'
    """)

    row = cursor.fetchone()

    assert row["name"] == "Laura"
    assert row["email"] == "laura@example.com"
    assert row["phone"] == "623456789"


def test_get_customers_email(cursor):

    cursor.execute("""
        SELECT email
        FROM customers
        WHERE id = 1
    """)

    row = cursor.fetchone()

    assert row["email"] == "dani@example.com"


def test_get_nonexistent_customer(cursor):

    cursor.execute("""
        SELECT *
        FROM customers
        WHERE id = 999
    """)

    row = cursor.fetchone()

    assert row is None


def test_update_customer_phone(cursor):

    cursor.execute("""
        UPDATE customers
        SET phone = '699999999'
        WHERE id = 1
    """)

    cursor.execute("""
        SELECT phone
        FROM customers
        WHERE id = 1
    """)

    row = cursor.fetchone()

    assert row["phone"] == "699999999"


def test_delete_customer(cursor):

    cursor.execute("""
        DELETE FROM customers
        WHERE id = 1
    """)

    cursor.execute("""
        SELECT *
        FROM customers
        WHERE id = 1
    """)

    row = cursor.fetchone()

    assert row is None