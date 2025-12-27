import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from data import Language as L, Urls as U


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='ru',
                     help=f"Set default language: {L.langs}")


@pytest.fixture
def browser(request):
    user_language = request.config.getoption("language")
    if user_language not in L.langs:
        raise pytest.UsageError(f"Invalid language. Choose language from: {L.langs}")
    options = Options()
    options.add_experimental_option("prefs", {"intl.accept_languages": user_language})
    browser = webdriver.Chrome(options=options)
    yield browser
    browser.get(U.link)
    time.sleep(30)
    browser.quit()

