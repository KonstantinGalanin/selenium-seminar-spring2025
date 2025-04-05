from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_LINK = (By.CLASS_NAME, "gtm-auth-header-btn")
    LOGIN_BTN = (By.CLASS_NAME, "bLqIKi")
    LOGIN_SUBMIT_BTN = (By.CLASS_NAME, "gmKwFa")
    LOGIN_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")
    SEARCH_TOGGLE = (By.CLASS_NAME, "gmTwDZ")
    SEARCH_INPUT = (By.CLASS_NAME, "global-search__SSearchInput-gCuMck")
    CLASSMATE = (By.XPATH, "//a[contains(@href, '/user_189524/')]") 

    WEB_COURSE = (By.XPATH, '//a[@href="/curriculum/program/904/"]')
    QA_COURSE = (By.XPATH, '//a[@href="/curriculum/program/discipline/2459/"]')
    SCHEDULE_LINK =(By.XPATH, '//a[@href="/schedule/"]')
    COURSES_TOGGLE = (By.CLASS_NAME, "styles__SArrowIconContainer-ioQVmZ")
    LESSON = (By.XPATH, '//a[@href="/curriculum/program/lesson/30921/"]')


class MainPageLocators(LoginPageLocators):
    pass

def lesson_locator(lesson_id):
    return (By, f'//a[@href="/curriculum/program/lesson/{lesson_id}/"]')
