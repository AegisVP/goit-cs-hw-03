import faker
from random import randint
from connect import create_connect, execute_query

def generate_fake_users(n):
    fake = faker.Faker()
    fake_users = []
    for i in range(n):
        fake_users.append(
            {
                'fullname': fake.name(),
                'email': fake.email(),
            }
        )
    return fake_users

def generate_fake_tasks(n, n_users):
    fake = faker.Faker()
    fake_tasks = []
    for i in range(n):
        fake_tasks.append(
            {
                'title': fake.text(max_nb_chars = randint(20, 60)),
                'description': fake.sentence(nb_words = randint(6, 18)),
                'status_id': randint(1,3),
                'user_id': randint(1, n_users)
            }
        )
    return fake_tasks


def insert_fake_data_to_db(num_users = 50, num_tasks = 500) -> None:
    users = generate_fake_users(num_users)
    tasks = generate_fake_tasks(num_tasks, num_users)
    
    with create_connect() as conn:
        cur = conn.cursor()
        execute_query(conn, 'TRUNCATE users CASCADE;')
        execute_query(conn, 'TRUNCATE tasks CASCADE;')

        sql_stmt = """INSERT INTO users(fullname, email) VALUES (%s, %s);"""
        for i in range(num_users):
            user = tuple(users[i].values())
            cur.execute(sql_stmt, user)

        sql_stmt = """INSERT INTO tasks(title, description, status_id, user_id) VALUES (%s, %s, %s, %s);"""
        for i in range(num_tasks):
            task = tuple(tasks[i].values())
            cur.execute(sql_stmt, task)

        conn.commit()
        

if __name__ == "__main__":
    insert_fake_data_to_db()