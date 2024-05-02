import sqlite3
from connection import create_connection


def create_table(conn, create_table_sql):
    """
    Створення таблиці у базі даних SQLite
    :param conn: об'єкт підключення
    :param create_table_sql: SQL-запит для створення таблиці
    """
    try:
        cursor = conn.cursor()
        cursor.execute(create_table_sql)
        conn.commit()
        print("Таблиця створена.")
    except sqlite3.Error as e:
        print("Помилка створення таблиці:", e)


if __name__ == '__main__':
    database = r"your_database.db"

    conn = create_connection()
    if conn is not None:
        create_users_table_sql = """
        CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        fullname VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE NOT NULL
        );
        """
        create_table(conn, create_users_table_sql)

        create_status_table_sql = """
        CREATE TABLE IF NOT EXISTS status (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) UNIQUE
        );
        """
        create_table(conn, create_status_table_sql)

        cursor = conn.cursor()
        cursor.execute("""
        INSERT INTO status (name) VALUES 
        ('new'),
        ('in progress'),
        ('completed');
        """)

        create_tasks_table_sql = """
        CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title VARCHAR(100),
        description TEXT,
        status_id INTEGER,
        user_id INTEGER,
        FOREIGN KEY (status_id) REFERENCES status(id) ON DELETE SET NULL ON UPDATE CASCADE,
        FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE ON UPDATE CASCADE
        );
        """

        create_table(conn, create_tasks_table_sql)

        conn.close()
    else:
        print("Помилка! Неможливо встановити з'єднання з базою даних.")
