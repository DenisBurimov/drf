import random
from faker import Faker
from users.models import User, Profile


faker = Faker()

TEST_USERS_NUMBER = 10


def fill_db(users_number: int = TEST_USERS_NUMBER):
    for i in range(users_number):
        phone_number = f"{random.randint(1000000000, 9999999999)}"
        user = User.objects.create(
            phone_number=phone_number,
            password=faker.text(max_nb_chars=5),
        )
        Profile.objects.create(
            user=user,
            description=faker.text(max_nb_chars=32),
        )
    print(f"Filled database with {users_number} users.")
