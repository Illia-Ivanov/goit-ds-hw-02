import sqlite3

def create_connection():
    """
    Вибір всіх даних з таблиці статус
    :return: Рядки результату
    """
    try:
        connection = sqlite3.connect("your_database.db")
        print("Підключення до бази даних успішно створено.")
        return connection

    except sqlite3.Error as e:
        print("Помилка підключення до бази даних:", e)
        return None


if __name__ == "__main__":
    connection = create_connection()
    if connection:
        connection.close()
        print("Підключення до бази даних закрито.")
