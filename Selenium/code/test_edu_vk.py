import pytest
from _pytest.fixtures import FixtureRequest
import dotenv
import os
from ui.pages.vk.login_page import LoginPage
from ui.pages.vk.feed_page import FeedPage
from ui.pages.base_page import BasePage


class BaseCase:
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, driver, config, request: FixtureRequest):
        self.driver = driver
        self.config = config

        self.login_page = LoginPage(driver)
        self.main_page = MainPage(driver)


@pytest.fixture(scope='session')
def credentials():
        dotenv.load_dotenv()
        return {"login": os.getenv("LOGIN"), "password": os.getenv("PASSWORD")}


@pytest.fixture(scope='session')
def cookies(credentials, config):
    driver = config.get("driver")


class MainPage(BasePage):
    url = 'https://education.vk.company/'


class TestLogin(BaseCase):
    def test_login(self, credentials):
        self.login_page.login(
            credentials["username"],
            credentials["password"]
        )

class TestLK(BaseCase):
    def test_search_classmate(self, credentials):
        self.login_page.login(
            credentials["username"],
            credentials["password"]
        )

        self.feed_page = FeedPage(self.driver) 

        username = "Александр Новиков"
        self.feed_page.search_classmate(username, "user_189524")
        assert username == self.feed_page.get_user_name()

    def test_search_lesson_info(self, credentials):
        self.login_page.login(
            credentials["username"],
            credentials["password"]
        )

        self.feed_page = FeedPage(self.driver)
        lesson_info = self.feed_page.search_lesson_info(30921)
        assert "Семинар 2. End-to-End тесты на Python" in lesson_info.text, "название занятия не совпадает"
