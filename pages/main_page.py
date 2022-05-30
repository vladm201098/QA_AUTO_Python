from base_page import BasePage


class MainPage(BasePage):
    Login_page = BasePage.Base_page_url.join('login')

    def open_login_page(self):
        self.open(self.Login_page)
