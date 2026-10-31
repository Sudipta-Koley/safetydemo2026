from selenium.webdriver.support.ui import WebDriverWait
from config.config import LOGIN_PAGE_URL, EXPLICIT_WAIT


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, EXPLICIT_WAIT)

    def open(self):
        self.driver.get(LOGIN_PAGE_URL)
