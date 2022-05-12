from selenium.webdriver.chrome.options import Options
from selenium.webdriver import Chrome
import pytest


class DriverCreator(Chrome):

    def __init__(self):
        options = Options()
        options.add_argument("--no-sandbox")
        options.headless = True
        options.add_experimental_option("useAutomationExtension", False)
        options.add_argument("start-maximized")
        options.add_argument("disable-infobars")
        options.add_argument("--disable-extensions")
        options.add_argument("--disable-gpu")
        options.add_argument("--disable-dev-shm-usage")
        super().__init__(options=options, executable_path="/usr/local/bin/chromedriver")


# @pytest.fixture(scope="session", autouse=True)
# def browser(url):
#     options = Options()
#     options.add_argument("--no-sandbox")
#     options.headless = True
#     options.add_experimental_option("useAutomationExtension", False)
#     options.add_argument("start-maximized")
#     options.add_argument("disable-infobars")
#     options.add_argument("--disable-extensions")
#     options.add_argument("--disable-gpu")
#     options.add_argument("--disable-dev-shm-usage")
#     driver = Chrome(options=options)
#     driver.get(url)
#     driver.implicitly_wait(5)
#     yield driver
#     driver.quit()
