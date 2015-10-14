import tempfile
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_user_can_enter_url_and_get_snapshot(self):
        # Jane navigties to http://scrot.io/ in her web browser.
        self.browser.get('http://localhost:8000/')

        # She is presented with an input that will allow her to enter any url.
        self.assertIn('Scrot.io', self.browser.title)

        # She enters the URL http://google.com/ and hits enter
        input = self.browser.find_element_by_id('id_url')
        input.send_keys('http://google.com/')
        input.send_keys(Keys.ENTER)

        # Soon enough, she is redirected to a page that displays a
        # screenshot of the URL she requested.
        body = self.browser.find_element_by_tag_name('body')
        images = body.find_elements_by_tag_name('img')
        self.assertIn('full.png', images[0].get_attribute('src'))


if __name__ == '__main__':
    unittest.main()
