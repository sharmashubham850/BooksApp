from pathlib import Path
import sqlite3

# Concerned with storing and retrieving books from a SQLITE Database


def create_book_table():
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()

        command = '''CREATE TABLE IF NOT EXISTS books(
                Name TEXT Primary Key,
                Author TEXT,
                Read INTEGER
        )'''

        cursor.execute(command)
        conn.commit()


def add_book(name, author):
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()
        command = "INSERT INTO books VALUES(?, ?, 0)"

        cursor.execute(command, (name, author))
        conn.commit()


def get_all_books():
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()
        command = "SELECT * FROM books"

        cursor.execute(command)

        books = [{'name': row[0], 'author': row[1], 'read':row[2]}
                 for row in cursor.fetchall()]

    return books


def mark_book_as_read(name):
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()
        command = "UPDATE books SET read= 1 WHERE name= ?"

        cursor.execute(command, (name,))
        conn.commit()


def delete_book(name):
    with sqlite3.connect('data.db') as conn:
        cursor = conn.cursor()
        command = "DELETE FROM books WHERE name= ?"

        cursor.execute(command, (name,))
        conn.commit()
