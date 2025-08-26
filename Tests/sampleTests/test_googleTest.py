import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from Pages.google_page import GooglePage


@pytest.fixture
def browser():
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=chrome_options
    )
    yield driver
    driver.quit()


def test_google_search(browser):
    google = GooglePage(browser)
    google.open()
    google.search("Selenium Python")
    assert "Selenium" in browser.title
