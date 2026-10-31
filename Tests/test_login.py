import pytest

from pages.login_page import LoginPage
from config.config import EMAIL, PASSWORD


@pytest.fixture
def login_page(driver):
    page = LoginPage(driver)
    page.open()
    return page


class TestLogin:
    @pytest.mark.negative
    def test_invalid_password(self, login_page):
        login_page.login(EMAIL, "WrongPassword@99")
        assert login_page.get_error_message(), "Expected an error for wrong password."

    @pytest.mark.negative
    def test_invalid_username(self, login_page):
        login_page.login("notregistered@example.com", PASSWORD)
        assert login_page.get_error_message(), "Expected an error for unknown email."

    @pytest.mark.negative
    def test_empty_credentials(self, login_page):
        login_page.click_login()
        assert not login_page.is_login_successful()

    @pytest.mark.negative
    def test_empty_username(self, login_page):
        login_page.enter_password(PASSWORD)
        login_page.click_login()
        assert not login_page.is_login_successful()

    @pytest.mark.negative
    def test_empty_password(self, login_page):
        login_page.enter_email(EMAIL)
        login_page.click_login()
        assert not login_page.is_login_successful()

    @pytest.mark.smoke
    def test_valid_login(self, login_page):
        if not EMAIL or not PASSWORD:
            pytest.skip("Set SAFETY_EMAIL and SAFETY_PASSWORD environment variables.")
        login_page.login(EMAIL, PASSWORD)
        assert login_page.is_login_successful(), "Dashboard was not displayed."
