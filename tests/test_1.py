from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestMyStore(unittest.TestCase):
    browser = None
    url = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
    mail = 'vladm201098112@gmail.com'
    password = '123456Qwer_'

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome(
            "chromedriver")
        cls.browser.maximize_window()
        cls.browser.get(cls.url)
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()

    def test_authorization(self):
        email = self.browser.find_element(by=By.ID, value="email")
        email.click()
        email.send_keys(self.mail)

        password = self.browser.find_element(by=By.ID, value="passwd")
        password.click()
        password.send_keys(self.password)

        submit_button = self.browser.find_element(by=By.ID,
                                                  value="SubmitLogin")
        submit_button.submit()

        my_account = self.browser.current_url
        self.assertEqual(my_account,
                         "http://automationpractice.com/index.php?controller=authentication")
