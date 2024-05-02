import sqlite3


def execute_query(query):
    conn = sqlite3.connect('your_database.db')
    cursor = conn.cursor()

    cursor.execute(query)
    rows = cursor.fetchall()

    conn.commit()
    conn.close()
    return rows


query1 = "SELECT * FROM tasks WHERE user_id = 1;"
result1 = execute_query(query1)
print(result1)

query2 = "SELECT * FROM tasks WHERE user_id = 1 AND status_id = 'new';"
result2 = execute_query(query2)
print(result2)

query3 = "UPDATE tasks SET status_id = 'in progress' WHERE status_id = 'new';"
execute_query(query3)

query4 = "SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);"
result4 = execute_query(query4)
print(result4)

query5 = "INSERT INTO tasks (title, description, status_id, user_id) VALUES ('Task Title', 'Easy Description', 2, 1);"
execute_query(query5)

query6 = "SELECT * FROM tasks WHERE status_id != 'completed';"
result6 = execute_query(query6)
print(result6)

query7 = "DELETE FROM tasks WHERE id = 1;"
execute_query(query7)

query8 = "SELECT * FROM users WHERE email LIKE 'A%';"
result8 = execute_query(query8)
print(result8)

query9 = "UPDATE users SET fullname = 'John' WHERE fullname = 'J%';"
execute_query(query9)

query10 = query = """ SELECT status.name AS status, COUNT(*) AS users FROM users JOIN status ON users.id = status.id GROUP BY status; """
result10 = execute_query(query10)
print(result10)

query11 = "SELECT tasks.* FROM tasks INNER JOIN users ON tasks.user_id = users.id WHERE users.email LIKE '%@gmail.com';"
result11 = execute_query(query11)
print(result11)

query12 = "SELECT tasks.* FROM tasks INNER JOIN users ON tasks.user_id = users.id WHERE tasks.description IS NULL OR tasks.description = '' AND tasks.status_id = 'in progress';"
result12 = execute_query(query12)
print(result12)

query13 = "SELECT users.id, users.fullname, COUNT(tasks.id) AS tasks FROM users LEFT JOIN tasks ON users.id = tasks.user_id GROUP BY users.id;"
result13 = execute_query(query13)
print(result13)
