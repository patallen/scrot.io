from PIL import Image
from datetime import datetime
from urllib.parse import urlparse, urlunparse
import os
import io

from django.conf import settings
from django.core.validators import URLValidator
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class ScrotHandler:
    def __init__(self, url, ext='png', width=1366, height=768):
        self.base_path = settings.MEDIA_ROOT
        self.ext = ext
        self.url = self._get_url(url)
        self.width = width
        self.height = height
        self.timestamp = datetime.now()
        self.basefn = '%s%s' % (self.domain, self.timestamp.strftime('%s'))
        self.user_agent = (
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) " +
            "AppleWebKit/537.36 (KHTML, like Gecko) " +
            "Chrome/45.0.2454.101 Safari/537.36"
        )
        dcap = dict(DesiredCapabilities.PHANTOMJS)
        dcap["phantomjs.page.settings.userAgent"] = self.user_agent
        self.driver = webdriver.PhantomJS(desired_capabilities=dcap,
                                          service_args=['--ssl-protocol=any'])

    def _get_url(self, url):
        valid_url = url
        if url[:4] != 'http':
            valid_url = 'http://' + url
        val = URLValidator()
        val(valid_url)
        p = urlparse(valid_url)
        self.domain = p.netloc
        return urlunparse((p.scheme, p.netloc, '/', '', '', ''))

    def _get_fn(self, postfix):
        return '{}_{}.{}'.format(self.basefn, postfix, self.ext)

    def load(self):
        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)

        self.driver.set_window_size(width=self.width, height=self.height)
        self.driver.get(self.url)
        self.full_fn = self._get_fn('full')
        filepath = os.path.join(settings.MEDIA_ROOT, self.full_fn)
        stream = io.BytesIO(self.driver.get_screenshot_as_png())
        self.screenshot = Image.open(stream)
        self.screenshot.save(filepath)

    def crop(self):
        self.screen_fn = self._get_fn('screen')
        self.cropped = self.screenshot.crop((0, 0, self.width, self.height))
        filepath = os.path.join(self.base_path, self.screen_fn)
        self.cropped.save(filepath)

    def thumb(self):
        self.thumb_fn = self._get_fn('thumb')
        self.thumb = self.cropped
        self.thumb.thumbnail((320, 180))
        filepath = os.path.join(self.base_path, self.thumb_fn)
        self.thumb.save(filepath)

    def create_images(self):
        self.load()
        self.crop()
        self.thumb()
