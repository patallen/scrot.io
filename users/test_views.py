import tempfile

from django.conf import settings
from django.test import TestCase

from users.models import CustomUser
from scrots.models import Website


class UsersViewsTestCase(TestCase):
    def setUp(self):
        settings.MEDIA_ROOT = tempfile.mkdtemp()
        website, _ = Website.objects.get_or_create(domain="google.com")
        self.user = CustomUser.objects.create_user(username="pat",
                                                   email="pat@pat.com")
        self.user.watched_websites.add(website)

    def test_user_has_websites_in_watchlist(self):
        watched1 = self.user.watched_websites.first()
        self.assertEqual("google.com", watched1.domain)
