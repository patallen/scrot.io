from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import PermissionsMixin

from scrots.models import Website


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(blank=False, unique=True)
    username = models.CharField(max_length=32, blank=False, unique=True)
    date_joined = models.DateField(default=timezone.now)

    first_name = models.CharField(max_length=128, blank=True)
    last_name = models.CharField(max_length=128, blank=True)

    watched_websites = models.ManyToManyField(
        Website, related_name='users_watching'
    )

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    REQUIRED_FIELDS = ['username', ]
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def get_full_name(self):
        """
        Returns the first name plus the last name with a space in between.
        """
        full_name = '{} {}'.format(self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        return self.first_name.strip()

    def likes_website(self, website):
        """
        Given a Website, return True if user is watching the Website.
        """
        watched_websites = self.watched_websites.all()
        if website in watched_websites:
            return True
        return False
