from ui.pages.base_page import BasePage
from ui.locators import locators_vk
from selenium.webdriver.common.keys import Keys

class FeedPage(BasePage):
    url = 'https://education.vk.company/feed/'

    def search_classmate(self, name, classmate_id):
        self.click(locators_vk.MainPageLocators.SEARCH_TOGGLE, timeout=10)
        search = self.find(locators_vk.MainPageLocators.SEARCH_INPUT)
        search.send_keys(name)
        search.send_keys(Keys.ENTER)
        self.click(locators_vk.classmate_locator(classmate_id), timeout=10)

    def search_lesson_info(self, lesson_id):
        self.click(locators_vk.MainPageLocators.COURSES_TOGGLE)
        self.click(locators_vk.MainPageLocators.QA_COURSE, timeout=10)
        self.driver.switch_to.window(self.driver.window_handles[-1])
        self.click(locators_vk.lesson_locator(lesson_id), timeout=10)
        

    