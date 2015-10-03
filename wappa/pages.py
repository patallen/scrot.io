from selenium import webdriver
from urllib.parse import urlparse
from datetime import datetime
from django.conf import settings
from scrots.models import Scrot
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


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


def get_screenshot_from_url(url, width=1280, height=800):
    user_agent = (
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) " +
        "AppleWebKit/537.36 (KHTML, like Gecko) " +
        "Chrome/45.0.2454.101 Safari/537.36"
    )

    dcap = dict(DesiredCapabilities.PHANTOMJS)
    dcap["phantomjs.page.settings.userAgent"] = user_agent
    driver = webdriver.PhantomJS(desired_capabilities=dcap)

    if not os.path.exists(settings.MEDIA_ROOT):
        os.makedirs(settings.MEDIA_ROOT)
    parser = urlparse(url)
    domain = parser.netloc
    filename = '{}{}.png'.format(domain, datetime.now().strftime('%s'))
    driver.set_window_size(width=width, height=height)
    driver.get(url)
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    driver.save_screenshot(filepath)

    # Create Scrot in DB
    scrot = Scrot.objects.create(
        domain=domain,
        scrot_file=filename,
        width=width,
        height=height
    )
    return scrot
