import pytest
from _pytest.fixtures import FixtureRequest
import time
import dotenv
import os
from ui.pages.vk.login_page import LoginPage
from ui.pages.vk.feed_page import FeedPage


from ui.pages.base_page import BasePage
from ui.locators import locators_vk
from selenium.webdriver.common.keys import Keys



# class BasePageLocators: 
#     LOGIN_LINK = ("class name", "gtm-auth-header-btn")
#     LOGIN_BTN = ("class name", "bLqIKi")
#     LOGIN_SUBMIT_BTN = ("class name", "gmKwFa")


class BaseCase:
    authorize = True

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)
        if self.authorize:
            print('Do something for login')


@pytest.fixture(scope='session')
def credentials():
        # dotenv.load_dotenv()
        # return {"login": os.getenv("LOGIN"), "password": os.getenv("PASSWORD")}

        return {
            "username": "konstantin.galanin@icloud.com",
            "password": "NFQ-V6i-z76-9Tp"
        }   


@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = config.get("driver")
    pass


class MainPage(BasePage):
    url = 'https://education.vk.company/'


class TestLogin(BaseCase):
    authorize = True

    # def test_login(self, credentials):
    #     self.login_page = LoginPage(self.driver)
    #     self.login_page.login(
    #         credentials["username"],
    #         credentials["password"]
    #     )
    #     time.sleep(15)
    #     assert 1 == 1

class TestLK(BaseCase):

    def test_search_classmate(self, credentials):
        self.login_page = LoginPage(self.driver)
        self.login_page.login(
            credentials["username"],
            credentials["password"]
        )

        self.feed_page = FeedPage(self.driver) 
        self.feed_page.search_classmate("Александр Новиков") 
        time.sleep(10)



    def test_search_lesson_info(self, credentials):
        self.login_page = LoginPage(self.driver)
        self.login_page.login(
            credentials["username"],
            credentials["password"]
        )

        self.feed_page = FeedPage(self.driver)
        self.feed_page.click(locators_vk.LoginPageLocators.COURSES_TOGGLE)
        self.feed_page.search_lesson_info()

        time.sleep(10)
