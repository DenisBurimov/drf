from users.models import User, Profile
from users.serializers import UserSerializer
from main.logger import log


class UsersProfilesManager:
    def get(self, phone_number: str) -> User:
        return User.objects.get(phone_number=phone_number)

    def get_all(self) -> list[User]:
        return User.objects.all()

    def post(
        self,
        phone: str,
        password: str,
        first_name: str,
        last_name: str,
        description: str,
    ) -> tuple[User, Profile]:
        log(
            log.INFO,
            "Creating user: [%s], [%s], [%s], [%s], [%s]",
            phone,
            password,
            first_name,
            last_name,
            description,
        )
        user = User.objects.create(
            phone_number=phone,
            password=password,
        )
        log(
            log.INFO,
            "User created successfully [%s], [%s]",
            user.phone_number,
            user.password,
        )
        profile = Profile.objects.create(
            user=User.objects.get(phone_number=phone),
            first_name=first_name,
            last_name=last_name,
            description=description,
        )
        log(
            log.INFO,
            "Profile created successfully [%s], [%s], [%s]",
            profile.first_name,
            profile.last_name,
            profile.description,
        )
        return user, profile

    def update(
        self,
        user: User,
        phone: str | None = None,
        password: str | None = None,
        first_name: str | None = None,
        last_name: str | None = None,
        description: str | None = None,
    ) -> bool:
        try:
            log(log.INFO, "Updating user: [%s]", user.phone_number)
            user.phone_number = phone
            user.password = password
            user.save()

            user.profile.first_name = first_name
            user.profile.last_name = last_name
            user.profile.description = description
            user.profile.save()

            log(log.INFO, "User updated successfully")
            return True

        except Exception as e:
            log(log.ERROR, f"Failed to update user: {e}")
            return False
