--SQLite запити в СУБД якщо потрібно буде,в вигляді коду знаходяться в Queries.py

SELECT * FROM tasks WHERE user_id = 1;

SELECT * FROM tasks WHERE user_id = 1 AND status_id = 'new';

UPDATE tasks SET status_id = 'in progress' WHERE status_id = 'new';

SELECT * FROM users WHERE id NOT IN (SELECT DISTINCT user_id FROM tasks);

INSERT INTO tasks (title, description, status_id, user_id) VALUES ('Task Title', 'Easy Description', 2, 1);

SELECT * FROM tasks WHERE status_id != 'completed';

DELETE FROM tasks WHERE id = 1;

SELECT * FROM users WHERE email LIKE 'A%';

UPDATE users SET fullname = 'John' WHERE fullname = 'J%';

SELECT status.name AS status, COUNT(*) AS users FROM users JOIN status ON users.id = status.id GROUP BY status;

SELECT tasks.* FROM tasks INNER JOIN users ON tasks.user_id = users.id WHERE users.email LIKE '%@gmail.com';

SELECT tasks.* FROM tasks INNER JOIN users ON tasks.user_id = users.id WHERE tasks.description IS NULL OR tasks.description = '' AND tasks.status_id = 'in progress';

SELECT users.id, users.fullname, COUNT(tasks.id) AS tasks FROM users LEFT JOIN tasks ON users.id = tasks.user_id GROUP BY users.id;