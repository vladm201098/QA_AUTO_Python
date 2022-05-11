from base_page import BasePage

class LoginPage(BasePage):

    # *LoginPageLocator - нужно создать файл с локаторами и оттуда доставать *LoginPageLocator.user_field /pass_field/Login_button
    def user_field(self,user):
        field = self.find_element(*LoginPageLocator.user_field)
        field.send_keys(user)
        return field

    def pass_field(self, password):
        field = self.find_element(*LoginPageLocator.pass_field)
        field.send_keys(password)
        return field

    def login_button(self):
        button = self.find_element(*LoginPageLocator.login_button)
        return button

    def click_login_button(self):
        self.login_button().click()

    def login(self, user, password):
        self.user_field(user)
        self.pass_field(password)
        self.login_button()
