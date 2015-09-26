from wappa.pages import *

def capture_screenshot(url, dims):
    driver = webdriver.PhantomJS()
    driver.get(url)
    driver.set_window_size(**dims)
    driver.get_screenshot_as_file('crayon.co.png')
    print(driver.title)

if __name__ == '__main__':
    page = BasePage('http://google.com/')
    print page.capture_screenshot()
