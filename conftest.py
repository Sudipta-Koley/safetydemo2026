import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture
def driver():
    options = Options()
    if os.getenv("CI"):
        options.add_argument("--headless=new")
        options.add_argument("--window-size=1920,1080")

    driver = webdriver.chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()
