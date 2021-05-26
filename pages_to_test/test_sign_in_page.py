import pytest
import assets.urls as urls
from assets.user_data import USER_CREDENTIALS
from objects.sign_in_page_objects import SignInPageObject
from objects.catalog_page_objects import CatalogPageObject
from objects.cookie_banner_objects import CookieBannerObject
from selenium.webdriver import Chrome
from selenium.common.exceptions import NoSuchElementException
from time import sleep


@pytest.fixture(scope="session", autouse=True)
def browser():
    driver = Chrome()
    driver.get(urls.SIGN_IN_URL)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def sign_in_page(browser):
    sign_in_page = SignInPageObject(browser)
    return sign_in_page


@pytest.fixture(scope="session", autouse=True)
def catalog_page(browser):
    catalog_page = CatalogPageObject(browser)
    return catalog_page


@pytest.fixture(scope="session", autouse=True)
def cookie_banner(browser):
    cookie_banner = CookieBannerObject(browser)
    return cookie_banner


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


def test_log_in(browser, sign_in_page, catalog_page):
    print("")
    email_field = sign_in_page.email_field()
    password_field = sign_in_page.password_field()
    email_field.clear()
    email_field.send_keys(USER_CREDENTIALS[0]["EMAIL"])
    password_field.clear()
    password_field.send_keys(USER_CREDENTIALS[0]["PASSWORD"])
    sign_in_page.start_watching_button().click()
    catalog_page.wait_for_the_page_to_be_open_without_auto_playback()

    try:
        if catalog_page.player_container().is_displayed():
            catalog_page.wait_for_the_page_to_be_open_with_auto_playback()
    except NoSuchElementException:
        print("### Account with auto playback disabled")

    try:
        if catalog_page.onboarding_banner().is_displayed():
            catalog_page.onboarding_banner_button().click()
    except NoSuchElementException:
        print("### 'What's New' banner already dismissed")

    assert catalog_page.rails()[0].is_displayed()


def log_in(browser, account_index):
    print("")
    sign_in_page = SignInPageObject(browser)
    catalog_page = CatalogPageObject(browser)
    cookie_banner = CookieBannerObject(browser)
    sign_in_page.wait_for_the_page_to_be_open()
    cookie_banner.wait_for_cookie_banner()
    cookie_banner.accept_all_cookies_button().click()
    sleep(1)

    try:
        if cookie_banner.accept_all_cookies_button().is_displayed():
            cookie_banner.accept_all_cookies_button().click()
            print("### Double cookie banner dismissed")
    except:
        print("### Single cookie banner dismissed")

    email_field = sign_in_page.email_field()
    password_field = sign_in_page.password_field()
    email_field.clear()
    email_field.send_keys(USER_CREDENTIALS[account_index]["EMAIL"])
    password_field.clear()
    password_field.send_keys(USER_CREDENTIALS[account_index]["PASSWORD"])
    sign_in_page.start_watching_button().click()
    catalog_page.wait_for_the_page_to_be_open_without_auto_playback()
    try:
        if catalog_page.player_container().is_displayed():
            catalog_page.wait_for_the_page_to_be_open_with_auto_playback()
    except NoSuchElementException:
        print("### Account with disabled auto playback")
