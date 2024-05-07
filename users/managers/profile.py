from users.models import User, Profile


def create_user_with_profile(
    phone: str,
    password: str,
    first_name: str,
    last_name: str,
    description: str,
):
    user = User.objects.create(
        phone_number=phone,
        password=password,
    )
    profile = Profile.objects.create(
        user=User.objects.get(phone_number=phone),
        first_name=first_name,
        last_name=last_name,
        description=description,
    )
    return user, profile
