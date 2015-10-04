from django.test import TestCase
from scrots.models import Scrot
from django.core.urlresolvers import reverse


class ScrotsViewsTestCase(TestCase):
    def setUp(self):
        Scrot.objects.get_or_create(domain="google.com",
                                    scrot_file="google.png",
                                    width=1600, height=900)
        Scrot.objects.get_or_create(domain="abc.com",
                                    scrot_file="abc.png",
                                    width=1600, height=900)

    def test_index(self):
        res = self.client.get('/')
        form_url = '<input id="id_url" name="url" type="text" />'
        self.assertEquals(res.status_code, 200)
        self.assertTemplateUsed(res, 'scrots/index.html')
        self.assertContains(res, 'scrot.io')
        self.assertContains(res, form_url)

    def test_recent_list(self):
        res = self.client.get(reverse("recent_list"))
        ctx = res.context
        self.assertEquals(res.status_code, 200)
        self.assertEquals(len(ctx['object_list']), 2)

    def test_detail(self):
        res = self.client.get(reverse("scrot_detail", kwargs={'pk': '1'}))
        ctx = res.context
        self.assertContains(res, 'google.png')
        self.assertIn(ctx['object'].domain, 'google.com')
