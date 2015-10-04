from django.test import TestCase
from scrots.forms import UrlScrotForm


class ScrotsFormsTestCase(TestCase):
    def setUp(self):
        self.url = 'http://google.com/'

    def test_url_form(self):
        blank_form = UrlScrotForm(data={'url': ''})
        full_form = UrlScrotForm(data={'url': self.url})
        self.assertFalse(blank_form.is_valid())
        self.assertTrue(full_form.is_valid())
