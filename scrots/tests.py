from django.test import TestCase


class ScrotsTestCase(TestCase):
    def test_index(self):
        res = self.client.get('/')
        self.assertEquals(res.status_code, 200)
        self.assertTemplateUsed(res, 'scrots/index.html')
        self.assertContains(res, 'scrot.io')
