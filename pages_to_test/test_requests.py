import pytest
import Selenium.DAZN.assets.urls as urls
from Selenium.DAZN.objects.catalog_page_objects import CatalogPageObject
from Selenium.DAZN.pages_to_test.test_sign_in_page import log_in
from selenium.common.exceptions import NoSuchElementException
from seleniumwire.webdriver import Chrome
from time import sleep


@pytest.fixture(scope="session", autouse=True)
def browser():
    driver = Chrome()
    driver.get(urls.SIGN_IN_URL)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

@pytest.fixture(scope="session", autouse=True)
def catalog_page(browser):
    catalog_page = CatalogPageObject(browser)
    return catalog_page

def test_subscribe_favourites(browser, catalog_page):
    log_in(browser)
    catalog_page.wait_for_the_page_to_be_open()
    catalog_page.wait_for_favourite_button()
    catalog_page.favourite_button().click()

    try:
        assert catalog_page.favourite_list().is_displayed()
        catalog_page.favourite_item()[0].click()
        sleep(1) # sleep to give time to process the request
        catalog_page.favourite_button().click()

    except NoSuchElementException:
        print("Only one favourite available")

    for request in browser.requests:
        if request.headers["Host"] == urls.FAVOURITES_HOST and request.method == "POST":
            favourites_status_code = request.response.status_code

    assert favourites_status_code == 201
    assert catalog_page.favourite_confirmation_banner().is_displayed()
    assert catalog_page.favourite_confirmation_banner_dismiss_button().is_displayed()

    catalog_page.favourite_confirmation_banner_dismiss_button().click()
    sleep(1)

def test_unsubscribe_unsubscribe_favourites(browser, catalog_page):
    catalog_page.favourite_button().click()

    try:
        assert catalog_page.favourite_list().is_displayed()
        catalog_page.favourite_item()[0].click()
        sleep(1) # sleep to give time to process the request
        catalog_page.favourite_button().click()

    except NoSuchElementException:
        print("Only one favourite available")

    for request in browser.requests:
        if request.headers["Host"] == urls.FAVOURITES_HOST and request.method == "DELETE":
            favourites_status_code = request.response.status_code

    assert favourites_status_code == 204
    assert catalog_page.favourite_confirmation_banner().is_displayed()
    assert catalog_page.favourite_confirmation_banner_dismiss_button().is_displayed()

    catalog_page.favourite_confirmation_banner_dismiss_button().click()
    sleep(2)
