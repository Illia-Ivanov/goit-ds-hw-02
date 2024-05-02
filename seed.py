import sqlite3
import faker
from random import randint


def fake_users(users_data):
    fake_users_data = []
    fake_data = faker.Faker()

    for i in range(users_data):
        fullname = fake_data.name()
        email = fake_data.email()
        fake_users_data.append((fullname, email))

    return fake_users_data


def generate_fake_data(fa_data):
    fake_data = faker.Faker()
    fakes_data = []

    for i in range(fa_data):
        fake_title = fake_data.sentence()
        fake_description = fake_data.text()
        fake_status_id = randint(1, 3)
        fake_user_id = randint(1, 10)
        fakes_data.append((fake_title, fake_description, fake_status_id, fake_user_id))
    return fakes_data


def insert_data_to_db(fakes_data, uf_data) -> None:
    conn = sqlite3.connect('your_database.db')
    cur = conn.cursor()

    us_d = '''INSERT INTO users (fullname,email) Values (?,?) '''
    cur.executemany(us_d, uf_data)

    inserting = """INSERT INTO tasks (title,description,status_id,user_id) VALUES (?,?,?,?)"""
    cur.executemany(inserting, fakes_data)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    fa_data = 20
    users_data = 20

    uf_data = fake_users(users_data)
    f_data = generate_fake_data(fa_data)

    insert_data_to_db(f_data, uf_data)
