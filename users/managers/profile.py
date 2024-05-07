from users.models import D3User, Profile


class UserProfileManager:
    def create_user_with_profile(
        self,
        phone: str,
        password: str,
        first_name: str,
        last_name: str,
        description: str,
    ):
        user = D3User.objects.create(
            phone_number=phone,
            password=password,
        )
        profile = Profile.objects.create(
            user=D3User.objects.get(phone_number=phone),
            first_name=first_name,
            last_name=last_name,
            description=description,
        )
        return user, profile

    def get_profile(self):
        return self.profile
