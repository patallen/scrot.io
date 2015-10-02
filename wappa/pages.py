from selenium import webdriver
from urllib.parse import urlparse
from datetime import datetime
from django.conf import settings
from scrots.models import Scrot
import os
class BasePage(object):

    def __init__(self, url=None):
        self.dims = {'width': 1280, 'height': 800}
        self.url = url

    def get_filename(self):
        if not self.url:
            raise ValueError("URL not specified.")
        parser = urlparse(self.url)
        domain = parser.netloc
        return '{}-{}.png'.format(domain, datetime.now())

    def capture_screenshot(self):
        driver = webdriver.PhantomJS()
        driver.get(self.url)
        driver.set_window_size(**self.dims)
        driver.get_screenshot_as_file(self.get_filename())
        return self.get_filename()


def get_screenshot_from_url(url, width=1200, height=724):
    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)
    parser = urlparse(url)
    domain = parser.netloc
    filename = '{}-{}.png'.format(domain, datetime.now())
    driver = webdriver.PhantomJS()
    driver.get(url)
    driver.set_window_size(width=width, height=height)
    driver.get_screenshot_as_file(os.path.join(settings.MEDIA_ROOT, filename))
    return filename
