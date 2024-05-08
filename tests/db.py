import random
from faker import Faker
from users.models import User, Profile
from articles.models import Article


faker = Faker()

TEST_USERS_NUMBER = 10


def fill_db(users_number: int = TEST_USERS_NUMBER):
    for i in range(users_number):
        phone_number = f"{random.randint(1000000000, 9999999999)}"
        user = User.objects.create(
            phone_number=phone_number,
            password=faker.text(max_nb_chars=5),
        )
        first_name = faker.first_name()
        last_name = faker.last_name()
        profile = Profile.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name,
            description=f"Profile {user.phone_number} - {first_name} {last_name}",
        )
        Article.objects.create(
            author=profile,
            title=faker.text(max_nb_chars=50),
            content=faker.text(max_nb_chars=500),
        )
    print(f"Filled database with {users_number} users.")
