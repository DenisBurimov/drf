from django.contrib import admin
from django.contrib.auth.models import Group
from .models import D3User, Profile, GroupProxy


# Register your models here.
admin.site.unregister(Group)
admin.site.register(D3User)
admin.site.register(Profile)
admin.site.register(GroupProxy)
