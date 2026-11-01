import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    if os.getenv("HEADLESS", "0") == "1":
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    browser = webdriver.chrome(options=options)
    browser.maximize_window()
    yield browser
    browser.quit()
