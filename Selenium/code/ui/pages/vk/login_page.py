from ui.pages.base_page import BasePage
from ui.locators import locators_vk

class LoginPage(BasePage):
    url = 'https://education.vk.company/'

    def login(self, email, password):
        self.click(locators_vk.LoginPageLocators.LOGIN_LINK, timeout=10)
        self.click(locators_vk.LoginPageLocators.LOGIN_BTN, timeout=10)
        self.find(locators_vk.LoginPageLocators.LOGIN_INPUT).send_keys(email)
        self.find(locators_vk.LoginPageLocators.PASSWORD_INPUT).send_keys(password)
        self.click(locators_vk.LoginPageLocators.LOGIN_SUBMIT_BTN, timeout=10)