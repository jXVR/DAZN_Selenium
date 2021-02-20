import pytest
import Selenium.DAZN.assets.urls as urls
from Selenium.DAZN.objects.landing_page_objects import LandingPageObject
from Selenium.DAZN.objects.sign_in_page_objects import SignInPageObject
from Selenium.DAZN.objects.cookie_banner_objects import CookieBannerObject
from selenium.webdriver import Chrome

@pytest.fixture(scope="session", autouse=True)
def browser():
    driver = Chrome()
    driver.get(urls.MAIN_URL)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# setup or class with Object initialization, referred in test functions through "self"

def test_landing_page_is_displayed(browser):
    landing_page = LandingPageObject(browser)
    landing_page.wait_for_the_page_to_be_open()
    assert landing_page.landing_page_as_open_browse().is_displayed()

def test_landing_page_cookie_banner_is_displayed(browser):
    cookie_banner = CookieBannerObject(browser)
    cookie_banner.wait_for_cookie_banner()
    assert cookie_banner.cookie_banner().is_displayed()

def test_landing_page_accept_cookie_button_is_dissmissed(browser):
    cookie_banner = CookieBannerObject(browser)
    assert cookie_banner.accept_all_cookies_button().is_displayed()
    cookie_banner.accept_all_cookies_button().click()

# how to check if the cookie banner is dismissed or no longer displayed?

def test_landing_page_sign_in_button_redirection(browser):
    landing_page = LandingPageObject(browser)
    sign_in_page = SignInPageObject(browser)
    landing_page.landing_page_sign_in_button().click()
    sign_in_page.wait_for_the_page_to_be_open()
    assert sign_in_page.sign_in_page_title().is_displayed()
