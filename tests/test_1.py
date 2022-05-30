from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class TestMyStore(unittest.TestCase):
    browser = None
    url = "http://automationpractice.com/index.php?controller=authentication&back=my-account"
    mail = 'alesia_94@bk.ru'
    password = 'Qwe123456!'

    @classmethod
    def setUpClass(cls) -> None:
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--disable-gpu')
        cls.browser = webdriver.Chrome(chrome_options=chrome_options, executable_path='/home/alesya/les/homework/tests/chromedriver')
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
