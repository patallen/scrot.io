from django.test import TestCase
from scrots.forms import UrlScrotForm


class ScrotsTestCase(TestCase):
    def setUp(self):
        self.res = self.client.get('/')

    def test_index(self):
        self.assertEquals(self.res.status_code, 200)
        self.assertTemplateUsed(self.res, 'scrots/index.html')
        self.assertContains(self.res, 'scrot.io')

    def test_form_on_page(self):
        form_url = '<input id="id_url" name="url" type="text" />'
        self.assertContains(self.res, form_url)


class UrlScrotFormTestCase(TestCase):
    def setUp(self):
        self.url = 'http://google.com/'

    def test_initial_value_typeerror(self):
        with self.assertRaises(TypeError):
            UrlScrotForm(url=self.url)
