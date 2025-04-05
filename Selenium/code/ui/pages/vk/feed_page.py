from ui.pages.base_page import BasePage
from ui.locators import locators_vk
from selenium.webdriver.common.keys import Keys

class FeedPage(BasePage):
    url = 'https://education.vk.company/feed/'

    def search_classmate(self, name):
        self.click(locators_vk.LoginPageLocators.SEARCH_TOGGLE, timeout=10)
        search = self.find(locators_vk.LoginPageLocators.SEARCH_INPUT)
        search.send_keys(name)
        search.send_keys(Keys.ENTER)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.click(locators_vk.LoginPageLocators.CLASSMATE, timeout=10)

    def search_lesson_info(self):
        self.click(locators_vk.LoginPageLocators.QA_COURSE, timeout=10)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.click(locators_vk.LoginPageLocators.LESSON, timeout=10)
        

    