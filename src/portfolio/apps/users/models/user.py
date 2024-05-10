from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, Group
from .base_model import BaseModel
from users.managers import UserManager
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class GroupProxy(Group):
    class Meta:
        proxy = True
        app_label = "users"


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    phone_number = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=255, blank=True, null=True)
    USERNAME_FIELD = "phone_number"

    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )

    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_(
            "Designates whether this user should be treated as active. Unselect this instead of deleting accounts."
        ),
    )
    date_joined = models.DateTimeField(default=timezone.now)

    groups = models.ManyToManyField(
        GroupProxy,
        verbose_name=_("groups"),
        blank=True,
        help_text=_(
            "The groups this user belongs to. A user will get all permissions granted to each of their groups."
        ),
        related_name="user_set",
        related_query_name="user",
    )

    def __str__(self):
        return self.phone_number

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
