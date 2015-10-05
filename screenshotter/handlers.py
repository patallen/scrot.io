from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from urllib.parse import urlparse
from datetime import datetime
import os
from PIL import Image

from django.conf import settings
from scrots.models import Scrot


class ScrotHandler:
    def __init__(self, url, ext='png', width=1280, height=800):
        self.base_path = settings.MEDIA_ROOT
        self.ext = ext
        self.url = url
        self.width = width
        self.height = height
        self.timestamp = datetime.now()
        self.domain = self._get_domain()
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

    def _get_domain(self):
        parser = urlparse(self.url)
        return parser.netloc

    def _get_fn(self, postfix):
        return '{}_{}.{}'.format(self.basefn, postfix, self.ext)

    def create_scrot(self):
        if not os.path.exists(settings.MEDIA_ROOT):
            os.makedirs(settings.MEDIA_ROOT)

        self.driver.set_window_size(width=self.width, height=self.height)
        self.driver.get(self.url)
        filepath = os.path.join(settings.MEDIA_ROOT, self._get_fn('full'))
        self.driver.save_screenshot(filepath)

    def crop_to_screen(self):
        filepath = os.path.join(self.base_path, self._get_fn('full'))
        img = Image.open(filepath)
        img_width, _ = img.size
        cropped_img = img.crop((0, 0, img_width, self.height))
        new_filepath = os.path.join(self.base_path, self._get_fn('screen'))
        cropped_img.save(new_filepath)

    def create_thumbnail(self):
        filepath = os.path.join(self.base_path, self._get_fn('screen'))
        img = Image.open(filepath)
        img.thumbnail((640, 360))
        img.thumbnail((320, 180), Image.ANTIALIAS)
        filepath = os.path.join(self.base_path, self._get_fn('thumb'))
        img.save(filepath)

    def create_images(self):
        self.create_scrot()
        self.crop_to_screen()
        self.create_thumbnail()

    def save_to_db(self):
        scrot = Scrot.objects.create(
            domain=self.domain,
            scrot_file=self._get_fn('full'),
            width=self.width,
            height=self.height
        )
        return scrot
