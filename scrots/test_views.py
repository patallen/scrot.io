import tempfile

from django.test import TestCase
from scrots.models import Snapshot, Website
from django.core.urlresolvers import reverse
from django.conf import settings


class ScrotsViewsTestCase(TestCase):
    def setUp(self):
        settings.MEDIA_ROOT = tempfile.mkdtemp()
        google, _= Website.objects.get_or_create(domain="google.com")
        stackoverflow, _= Website.objects.get_or_create(domain="stackoverflow.com")
        google.add_snapshot()
        stackoverflow.add_snapshot()

    def test_index(self):
        res = self.client.get('/')
        ctx = res.context
        form_url = 'id="id_url" name="url" type="text"'
        self.assertEquals(res.status_code, 200)
        self.assertTemplateUsed(res, 'scrots/index.html')
        self.assertContains(res, 'Scrot.io')
        self.assertContains(res, form_url)
        self.assertEquals(len(ctx['object_list']), 2)

    def test_recent_list(self):
        res = self.client.get(reverse("recent_list"))
        ctx = res.context
        for x in ctx['object_list']: print(x)
        self.assertEquals(res.status_code, 200)
        self.assertEquals(len(ctx['object_list']), 2)

    def test_detail(self):
        res = self.client.get(reverse("website_detail", kwargs={'pk': '1'}))
        ctx = res.context
        self.assertEqual(ctx['object'].domain, 'google.com')
