from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest

from selenium.webdriver.support.select import Select


class TestRegistrations(unittest.TestCase):
    browser = None
    url = "https://demo.guru99.com/test/newtours/register.php"
    first_name = 'Vladislav'
    last_name = 'Medvedev'
    phone = '+48793******'
    email = 'vladm201098112@gmail.com'
    address = 'Wejherowska'
    city = 'Wroclaw'
    state = 'PL'
    post_code = '54239'
    user_name = 'vladm'
    passw = '123456Qwer_'

    @classmethod
    def setUpClass(cls) -> None:
        cls.browser = webdriver.Chrome("chromedriver")
        cls.browser.maximize_window()
        cls.browser.get(cls.url)
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.browser.quit()

    def test_registrations_fields(self):
        field_first_name = self.browser.find_element(by=By.NAME,
                                                     value="firstName")
        field_first_name.click()
        field_first_name.send_keys(self.first_name)

        field_last_name = self.browser.find_element(by=By.NAME,
                                                    value="lastName")
        field_last_name.click()
        field_last_name.send_keys(self.last_name)

        field_phone = self.browser.find_element(by=By.NAME, value="phone")
        field_phone.click()
        field_phone.send_keys(self.phone)

        field_email = self.browser.find_element(by=By.ID, value="userName")
        field_email.click()
        field_email.send_keys(self.email)

        field_address = self.browser.find_element(by=By.NAME, value="address1")
        field_address.click()
        field_address.send_keys(self.address)

        field_city = self.browser.find_element(by=By.NAME, value="city")
        field_city.click()
        field_city.send_keys(self.city)

        field_state = self.browser.find_element(by=By.NAME, value="state")
        field_state.click()
        field_state.send_keys(self.state)

        field_postal_code = self.browser.find_element(by=By.NAME,
                                                      value="postalCode")
        field_postal_code.click()
        field_postal_code.send_keys(self.post_code)

        country_field = Select(
            self.browser.find_element(by=By.NAME, value="country"))
        country_field.select_by_value("POLAND")

        field_user_name = self.browser.find_element(by=By.ID, value="email")
        field_user_name.click()
        field_user_name.send_keys(self.user_name)

        field_password = self.browser.find_element(by=By.NAME,
                                                   value="password")
        field_password.click()
        field_password.send_keys(self.passw)

        field_confirm_passw = self.browser.find_element(by=By.NAME,
                                                        value="confirmPassword")
        field_confirm_passw.click()
        field_confirm_passw.send_keys(self.passw)

        submit_button = self.browser.find_element(by=By.XPATH,
                                                  value="//table/tbody/tr[17]/td/input")
        submit_button.click()

        my_account = self.browser.current_url
        self.assertEqual(my_account,
                         "https://demo.guru99.com/test/newtours/register_sucess.php")

    def test_my_names(self):

        my_names = self.browser.find_element(by=By.XPATH,
                                             value="//table/tbody/tr[3]/td/p[1]/font/b").text
        self.assertEqual(my_names, f'Dear {self.first_name} {self.last_name},')

    def test_my_user_name(self):
        my_user_name = self.browser.find_element(by=By.XPATH,
                                                 value="//table/tbody/tr[3]/td/p[3]/font/b").text
        self.assertEqual(my_user_name,
                         f'Note: Your user name is {self.user_name}.')
