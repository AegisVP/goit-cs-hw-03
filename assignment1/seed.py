import faker
from random import randint
from datetime import datetime

def generate_fake_users(n):
    fake = faker.Faker()
    fake_users = []
    for _ in range(n):
        fake_users.append({
            'fullname':fake.name(),
            'email':fake.email(),})
    return fake_users

def generate_fake_tasks(n):
    fake = faker.Faker()
    fake_tasks = []
    for _ in range(n):
        fake_tasks.append({
            'title':fake.job(),
            'description':fake.text(),
            'status_id':randint(1,3),
        })
    return fake_tasks