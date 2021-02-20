import pytest
import Selenium.DAZN.assets.urls as urls
from Selenium.DAZN.assets.user_data import USER_CREDENTIALS
from Selenium.DAZN.objects.sign_in_page_objects import SignInPageObject
from Selenium.DAZN.objects.landing_page_objects import LandingPageObject
from Selenium.DAZN.objects.catalog_page_objects import CatalogPageObject
from Selenium.DAZN.objects.cookie_banner_objects import CookieBannerObject
from selenium.webdriver import Chrome
from time import sleep
from selenium.common.exceptions import NoSuchElementException

@pytest.fixture(scope="session", autouse=True)
def browser():
    driver = Chrome()
    driver.get(urls.SIGN_IN_URL)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_sign_in_page_is_displayed(browser):
    sign_in_page = SignInPageObject(browser)
    sign_in_page.wait_for_the_page_to_be_open()
    assert sign_in_page.sign_in_page_title().is_displayed()

def test_sign_in_page_cookie_banner_is_displayed(browser):
    cookie_banner = CookieBannerObject(browser)
    cookie_banner.wait_for_cookie_banner()
    assert cookie_banner.cookie_banner().is_displayed()

def test_sign_in_page_accept_cookie_button_is_dissmissed(browser):
    cookie_banner = CookieBannerObject(browser)
    assert cookie_banner.accept_all_cookies_button().is_displayed()
    cookie_banner.accept_all_cookies_button().click()

def test_log_in(browser):
    sign_in_page = SignInPageObject(browser)
    catalog_page = CatalogPageObject(browser)
    email_field = sign_in_page.email_field()
    password_field = sign_in_page.password_field()
    email_field.clear()
    email_field.send_keys(USER_CREDENTIALS[0]["EMAIL"])
    password_field.clear()
    password_field.send_keys(USER_CREDENTIALS[0]["PASSWORD"])
    sign_in_page.start_watching_button().click()
    catalog_page.wait_for_the_page_to_be_open()
    try:
        if catalog_page.onboarding_banner().is_displayed():
            catalog_page.onboarding_banner_button().click()
    except NoSuchElementException:
        print("### 'What's New' banner already dismissed")
    assert catalog_page.rails()[0].is_displayed()


def log_in(browser):
    sign_in_page = SignInPageObject(browser)
    catalog_page = CatalogPageObject(browser)
    cookie_banner = CookieBannerObject(browser)
    sign_in_page.wait_for_the_page_to_be_open()
    cookie_banner.wait_for_cookie_banner()
    cookie_banner.accept_all_cookies_button().click()
    email_field = sign_in_page.email_field()
    password_field = sign_in_page.password_field()
    email_field.clear()
    email_field.send_keys(USER_CREDENTIALS[0]["EMAIL"])
    password_field.clear()
    password_field.send_keys(USER_CREDENTIALS[0]["PASSWORD"])
    sign_in_page.start_watching_button().click()
    catalog_page.wait_for_the_page_to_be_open()
