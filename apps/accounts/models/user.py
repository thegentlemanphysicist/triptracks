from django.db import models
from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import UserManager
from utils.fields import ShortUUIDField


class User(AbstractBaseUser):

    USERNAME_FIELD = 'email'

    objects = UserManager()

    google_credentials = JSONField()
    email = models.CharField(max_length=256, unique=True)
    is_admin = models.BooleanField(default=False)
    pub_id = ShortUUIDField(prefix="user", max_length=128)

    @property
    def profile_image(self):
        return self.google_credentials.get("picture")

    @property
    def is_staff(self):
        print self.email
        print settings.STAFF_EMAILS
        return self.email in settings.STAFF_EMAILS

    def has_module_perms(self, app):
        return self.is_staff

    def has_perm(self, app):
        return self.is_staff

    def get_short_name(self):
        return self.email

    class Meta:
        app_label = 'accounts'
