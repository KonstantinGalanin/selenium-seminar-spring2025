from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_LINK = (By.CLASS_NAME, "gtm-auth-header-btn")
    LOGIN_BTN = (By.CLASS_NAME, "bLqIKi")
    LOGIN_SUBMIT_BTN = (By.CLASS_NAME, "gmKwFa")
    LOGIN_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")


class MainPageLocators(LoginPageLocators):
    SEARCH_TOGGLE = (By.CLASS_NAME, "gmTwDZ")
    SEARCH_INPUT = (By.CLASS_NAME, "global-search__SSearchInput-gCuMck")
    WEB_COURSE = (By.XPATH, '//a[@href="/curriculum/program/904/"]')
    QA_COURSE = (By.XPATH, '//a[@href="/curriculum/program/discipline/2459/"]')
    SCHEDULE_LINK =(By.XPATH, '//a[@href="/schedule/"]')
    COURSES_TOGGLE = (By.CLASS_NAME, "styles__SArrowIconContainer-ioQVmZ")

def lesson_locator(lesson_id):
    return (By.XPATH, f'//a[@href="/curriculum/program/lesson/{lesson_id}/"]')

def classmate_locator(classmate_id):
    return (By.XPATH, f'//a[contains(@href, "/{classmate_id}/")]')