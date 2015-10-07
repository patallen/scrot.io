from unittest import TestCase
from .handlers import ScrotHandler
from django.core.exceptions import ValidationError


class ScrotHandlerTestCase(TestCase):
    def setUp(self):
        self.scrot = ScrotHandler('stackoverflow.com')
        self.scrot.load()
        self.scrot.crop()

    def test_scrot_normalize_url(self):
        self.assertEqual(self.scrot.domain, 'stackoverflow.com')

    def test_bad_urls_raise_validationerror(self):
        with self.assertRaises(ValidationError):
            ScrotHandler('zz://google.com/')
        with self.assertRaises(ValidationError):
            ScrotHandler('http://google')

    def test_load_method_loads_png(self):
        self.scrot.load()
        self.assertTrue(self.scrot.screenshot)

    def test_crop_method_crops_img(self):
        s = (self.scrot.width, self.scrot.height)
        self.assertEqual(s, self.scrot.cropped.size)

    def test_thumb_resizes_cropped(self):
        self.scrot.thumb()
        self.assertEqual(self.scrot.thumb.size[0], 320)
