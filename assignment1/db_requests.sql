-- Отримати всі завдання певного користувача
 SELECT * FROM tasks WHERE user_id = 1;

-- Вибрати завдання за певним статусом
 SELECT * FROM tasks JOIN status ON tasks.status_id = status.id WHERE status.name = 'new';

-- Оновити статус конкретного завдання
 UPDATE tasks SET status_id = 1 WHERE id = 1;

-- Отримати список користувачів, які не мають жодного завдання
 SELECT * FROM users WHERE id NOT IN (SELECT user_id FROM tasks);

-- Додати нове завдання для конкретного користувача
 INSERT INTO tasks (title, description, status_id, user_id) VALUES ('title', 'description', 1, 1);

-- Отримати всі завдання, які ще не завершено
 SELECT * FROM tasks WHERE NOT (status_id = 3);

-- Видалити конкретне завдання
 DELETE FROM tasks WHERE id = 1;

-- Знайти користувачів з певною електронною поштою
 SELECT * FROM users WHERE email LIKE '%@example.com';

-- Оновити ім'я користувача
 UPDATE users SET fullname = 'name' WHERE id = 1;

-- Отримати кількість завдань для кожного статусу
SELECT status.name, COUNT(tasks.id) AS count FROM tasks JOIN status ON tasks.status_id = status.id GROUP BY status.name;

-- Отримати завдання, які призначені користувачам з певною доменною частиною електронної пошти
 SELECT * FROM tasks JOIN users ON tasks.user_id = users.id WHERE email LIKE '%@example.com';

-- Отримати список завдань, що не мають опису
 SELECT * FROM tasks WHERE description IS NULL;

-- Вибрати користувачів та їхні завдання, які є у статусі 'in progress'
 SELECT * FROM users JOIN tasks ON users.id = tasks.user_id JOIN status ON tasks.status_id = status.id WHERE status.name = 'in progress' ORDER BY users.fullname;

-- Отримати користувачів та кількість їхніх завдань
 SELECT users.fullname, COUNT(tasks.id) AS count FROM users JOIN tasks ON users.id = tasks.user_id GROUP BY users.fullname ORDER BY users.fullname;