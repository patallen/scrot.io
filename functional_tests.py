from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.PhantomJS()
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_user_can_enter_url_and_receive_collection(self):
        # Jane navigties to http://scrot.io/ in her web browser.
        self.browser.get('http://localhost:5000')

        # She is presented with an input that will allow her to enter any url.
        self.assertIn('scrot.io', self.browser.title)

        # She enters the URL http://google.com/ and hits enter
        input = self.browser.find_element_by_id('id_url')
        self.fail("Finish the tests!.")

        # She is then presented with a spinner indicating that she should wait.
        # Soon enough, the spinner stops and she is redirected to a page that displays (X) screenshots of the URL she requested.

if __name__ == '__main__':
    unittest.main()