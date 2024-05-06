import random
from faker import Faker
from users.models import D3User, Profile


faker = Faker()

TEST_USERS_NUMBER = 10


def fill_db(users_number: int = TEST_USERS_NUMBER):
    for i in range(users_number):
        phone_number = f"{random.randint(1000000000, 9999999999)}"
        D3User.objects.create(
            phone_number=phone_number,
            password=faker.text(max_nb_chars=5),
        )
        Profile.objects.create(
            user=D3User.objects.get(id=i + 1),
            description=faker.text(max_nb_chars=32),
        )
