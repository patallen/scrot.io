import tempfile

from django.conf import settings
from django.core.urlresolvers import reverse
from django.test import TestCase

from scrots.models import Website


class ScrotsViewsTestCase(TestCase):
    def setUp(self):
        settings.MEDIA_ROOT = tempfile.mkdtemp()
        google, _ = Website.objects.get_or_create(domain="google.com")
        so, _ = Website.objects.get_or_create(domain="stackoverflow.com")
        google.add_snapshot()
        so.add_snapshot()

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
        self.assertEquals(res.status_code, 200)
        self.assertEquals(len(ctx['object_list']), 2)

    def test_detail(self):
        res = self.client.get(reverse("website_detail", kwargs={'pk': '1'}))
        ctx = res.context
        obj = ctx['object']
        self.assertEqual(obj.domain, 'google.com')
        self.assertIn('google', str(obj.latest_snapshot().img_full))
