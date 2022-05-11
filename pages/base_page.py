from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    Base_page_url = 'https://www.google.com/'

    def __init__(self):
        self.url = None
        self.driver = webdriver.Chrome("chromedriver.exe")

    def open(self, url):
        self.driver.get(url)

    def open_main_page(self, Base_page_url):
        self.driver.get(Base_page_url)

    def find_element(self, element_locator):
        element = self.driver.find_element(element_locator)
        WebDriverWait(self.driver, 10).until(element)
        return element
