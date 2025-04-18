from selenium.webdriver.common.by import By


class LoginPageLocators:
    LOGIN_LINK = (By.CLASS_NAME, "gtm-auth-header-btn")
    LOGIN_BTN = (By.XPATH,'//button[@type="reset" and contains(@class, "gtm-signup-modal-link")]')
    LOGIN_SUBMIT_BTN = (By.XPATH, '//button[@type="submit" and text()="Войти с паролем"]')
    LOGIN_INPUT = (By.NAME, "email")
    PASSWORD_INPUT = (By.NAME, "password")


class MainPageLocators(LoginPageLocators):
    SEARCH_TOGGLE = (By.XPATH, '//div[@aria-label="Открыть поиск"]')
    SEARCH_INPUT = (By.CLASS_NAME, "global-search__SSearchInput-gCuMck")
    WEB_COURSE = (By.XPATH, '//a[@href="/curriculum/program/904/"]')
    QA_COURSE = (By.XPATH, '//a[@href="/curriculum/program/discipline/2459/"]')
    SCHEDULE_LINK =(By.XPATH, '//a[@href="/schedule/"]')
    COURSES_TOGGLE = (By.CLASS_NAME, "styles__SArrowIconContainer-ioQVmZ")
    USER_NAME = (By.CLASS_NAME, "profile-username")
    LESSON_NAME = (By.CLASS_NAME, "styleslesson__SLessonHeaderTitle-bWsegH")

def lesson_locator(lesson_id):
    return (By.XPATH, f'//a[@href="/curriculum/program/lesson/{lesson_id}/"]')

def classmate_locator(classmate_id):
    return (By.XPATH, f'//a[contains(@href, "/{classmate_id}/")]')