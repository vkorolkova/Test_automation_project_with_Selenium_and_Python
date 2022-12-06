import pytest
from selenium import webdriver
from selenium.webdriver import ChromeOptions
from selenium.webdriver.firefox.options import Options


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default="chrome",
                 help="Choose browser: chrome or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language")

@pytest.fixture(scope="function")
def browser(request):
    browser = None
    browser_name = request.config.getoption("browser_name")
    language = request.config.getoption("language")
    if browser_name == "chrome":
        options_chrome = ChromeOptions()
        options_chrome.add_experimental_option('prefs', {'intl.accept_languages': language})
        print("\nstart chrome browser for test..")
        browser = webdriver.Chrome(options=options_chrome)
    elif browser_name == "firefox":
        options_firefox = Options()
        options_firefox.set_preference("intl.accept_languages", language)
        browser = webdriver.Firefox(options=options_firefox)
        print("\nstart firefox browser for test..")
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()
