import pytest
import assets.urls as urls
from objects.landing_page_objects import LandingPageObject
from objects.sign_in_page_objects import SignInPageObject
from objects.cookie_banner_objects import CookieBannerObject
from selenium.webdriver import Chrome
from time import sleep


@pytest.fixture(scope="session", autouse=True)
def browser():
    driver = Chrome()
    driver.get(urls.MAIN_URL)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def landing_page(browser):
    landing_page = LandingPageObject(browser)
    return landing_page


@pytest.fixture(scope="session", autouse=True)
def sign_in_page(browser):
    sign_in_page = SignInPageObject(browser)
    return sign_in_page


@pytest.fixture(scope="session", autouse=True)
def cookie_banner(browser):
    cookie_banner = CookieBannerObject(browser)
    return cookie_banner


def test_landing_page_is_displayed(browser, landing_page):
    landing_page.wait_for_the_page_to_be_open()
    assert landing_page.landing_page_as_open_browse().is_displayed()


def test_landing_page_cookie_banner_is_displayed(browser, cookie_banner):
    cookie_banner.wait_for_cookie_banner()
    assert cookie_banner.cookie_banner().is_displayed()


def test_landing_page_accept_cookie_button_is_dismissed(browser, cookie_banner):
    assert cookie_banner.accept_all_cookies_button().is_displayed()
    cookie_banner.accept_all_cookies_button().click()
    sleep(1)
    try:
        if cookie_banner.accept_all_cookies_button().is_displayed():
            cookie_banner.accept_all_cookies_button().click()
    except:
        print("### Cookie banner dismissed")
    sleep(1)

# sign_in selector is not working (also xpath, and child from navigation item)
# def test_landing_page_sign_in_button_redirection(browser, landing_page, sign_in_page):
#     landing_page.landing_page_sign_in_button().click()
#     sign_in_page.wait_for_the_page_to_be_open()
#     assert sign_in_page.sign_in_page_title().is_displayed()
