import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time


url = "http://localhost:3000/"

class TestLogin(unittest.TestCase):
    def setUp(self):
        PATH = "/home/nayanprasad/chromedriver_linux64/chromedriver"
        self.driver = webdriver.Chrome(PATH)

    def get_element_wait(self, element_id, timeout=3):
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located((By.ID, element_id)))
        except TimeoutException:
            err = 'Element with id {} could not be found!'
            raise Exception(err.format(element_id))

    def test_login_success(self):
        self.driver.get(url)

        # get elements
        email = self.get_element_wait('t-email')
        password = self.get_element_wait('t-password')

        # set values
        email.send_keys('hades@gmail.com')
        password.send_keys('hades123')
        email.send_keys(Keys.RETURN)

        # verify that page was loaded
        profile = self.get_element_wait('t-profile')
        header = self.get_element_wait('header')
        assert header.text == u'Profile status'

    def test_login_failed(self):
        self.driver.get(url)

        # get elements
        email = self.get_element_wait('t-email')
        password = self.get_element_wait('t-password')

        # set values
        email.send_keys('erroruser')
        password.send_keys('error1234')
        email.send_keys(Keys.RETURN)

        # verify that alert message is shown
        header = self.get_element_wait('header-notfound')
        assert header.text == u'User not found'

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
