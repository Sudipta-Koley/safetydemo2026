from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

from pages.base_page import BasePage
from config.config import DASHBOARD_PAGE_URL


class LoginPage(BasePage):
    EMAIL_FIELD = (By.ID, "email")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Login']")
    ERROR_MESSAGE = (By.XPATH, "//*[contains(., 'Invalid email or password')]")

    def enter_email(self, email):
        field = self.wait.until(EC.visibility_of_element_located(self.EMAIL_FIELD))
        field.clear()
        if email:
            field.send_keys(email)

    def enter_password(self, password):
        field = self.wait.until(EC.visibility_of_element_located(self.PASSWORD_FIELD))
        field.clear()
        if password:
            field.send_keys(password)

    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.LOGIN_BUTTON)).click()

    def login(self, email, password):
        self.enter_email(email)
        self.enter_password(password)
        self.click_login()

    def get_error_message(self):
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.ERROR_MESSAGE)
            ).text.strip()
        except TimeoutException:
            return ""

    def is_login_successful(self):
        try:
            self.wait.until(EC.url_contains(DASHBOARD_PAGE_URL))
            return True
        except TimeoutException:
            return False
