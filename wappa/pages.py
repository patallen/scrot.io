from selenium import webdriver
from urlparse import urlparse
from datetime import datetime

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

