import pytest
import assets.urls as urls
from objects.cookie_banner_objects import CookieBannerObject
from objects.sign_up_page_objects import SignInPageObject
from objects.catalog_page_objects import CatalogPageObject
from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import uuid


@pytest.fixture(scope="session", autouse=True)
def browser():
    driver = Chrome()
    driver.get(urls.MAIN_URL)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture(scope="session", autouse=True)
def cookie_banner(browser):
    cookie_banner = CookieBannerObject(browser)
    return cookie_banner


@pytest.fixture(scope="session", autouse=True)
def sign_up_page(browser):
    sign_up_page = SignInPageObject(browser)
    return sign_up_page


@pytest.fixture(scope="session", autouse=True)
def catalog_page(browser):
    catalog_page = CatalogPageObject(browser)
    return catalog_page


def test_sign_up(browser, cookie_banner, sign_up_page, catalog_page):
    sign_up_page.sign_up_button().click()
    sign_up_page.wait_for_the_select_subscription_plan_page_to_be_open()

    cookie_banner.wait_for_cookie_banner()
    cookie_banner.accept_all_cookies_button().click()
    sleep(1)

    try:
        if cookie_banner.accept_all_cookies_button().is_displayed():
            cookie_banner.accept_all_cookies_button().click()
            print("### Double cookie banner dismissed")
    except:
        print("### Single cookie banner dismissed")

    ActionChains(browser).move_to_element(sign_up_page.monthly_plan_container()).perform()
    sign_up_page.monthly_plan_regular_button().click()

    sign_up_page.wait_for_the_create_account_page_to_be_open()
    first_name_field = sign_up_page.first_name_field()
    last_name_field = sign_up_page.last_name_field()
    email_field = sign_up_page.email_field()
    email_confirmation_field = sign_up_page.email_confirmation_field()
    password_field = sign_up_page.password_field()

    first_name_field.clear()
    first_name_field.send_keys("Test")
    last_name_field.clear()
    last_name_field.send_keys("Matatas")
    account_sufix = uuid.uuid4().hex
    email_field.clear()
    email_field.send_keys(f"xpdazn+selenium{account_sufix}@gmail.com")
    email_confirmation_field.clear()
    email_confirmation_field.send_keys(f"xpdazn+selenium{account_sufix}@gmail.com")
    password_field.clear()
    password_field.send_keys("12345a")
    sleep(2)
    sign_up_page.create_account_button().click()

    sign_up_page.wait_for_the_select_payment_page_to_be_open()

    try:
        if sign_up_page.free_trial_banner().is_displayed():
            sign_up_page.free_trial_dismiss_button().click()
            print("### Free Trial used")
    except:
        print("### Free Trial granted")

    sign_up_page.select_credit_card_payment_method().click()
    sleep(3)

    browser.switch_to.frame(sign_up_page.credit_card_number_frame())
    credit_card_number_field = sign_up_page.credit_card_number_field()
    credit_card_number_field.clear()
    credit_card_number_field.send_keys("4111111111111111")
    browser.switch_to.default_content()

    browser.switch_to.frame(sign_up_page.credit_card_expiry_month_frame())
    credit_card_expiry_month_field = sign_up_page.credit_card_expiry_month_field()
    credit_card_expiry_month_field.clear()
    credit_card_expiry_month_field.send_keys("03")
    browser.switch_to.default_content()

    browser.switch_to.frame(sign_up_page.credit_card_expiry_year_frame())
    credit_card_expiry_year_field = sign_up_page.credit_card_expiry_year_field()
    credit_card_expiry_year_field.clear()
    credit_card_expiry_year_field.send_keys("30")
    browser.switch_to.default_content()

    browser.switch_to.frame(sign_up_page.credit_card_security_code_frame())
    credit_card_security_number_field = sign_up_page.credit_card_security_code_field()
    credit_card_security_number_field.clear()
    credit_card_security_number_field.send_keys("737")
    browser.switch_to.default_content()

    credit_card_street_field = sign_up_page.credit_card_street_field()
    credit_card_street_field.clear()
    credit_card_street_field.send_keys("Street")

    credit_card_house_number_field = sign_up_page.credit_card_house_number_field()
    credit_card_house_number_field.clear()
    credit_card_house_number_field.send_keys("Number")

    credit_card_postal_code_field = sign_up_page.credit_card_postal_code_field()
    credit_card_postal_code_field.clear()
    credit_card_postal_code_field.send_keys("Code")

    credit_card_city_field = sign_up_page.credit_card_city_field()
    credit_card_city_field.clear()
    credit_card_city_field.send_keys("City")

    sleep(1)
    sign_up_page.credit_card_submit_button().click()

    sign_up_page.wait_for_the_sign_up_confirmation_page_to_be_open()
    sign_up_page.sign_up_confirmation_button().click()
    catalog_page.wait_for_the_page_to_be_open_without_auto_playback()
