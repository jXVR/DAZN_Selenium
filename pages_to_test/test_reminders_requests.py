import pytest
import Selenium.DAZN.assets.urls as urls
from Selenium.DAZN.objects.catalog_page_objects import CatalogPageObject
from Selenium.DAZN.pages_to_test.test_sign_in_page import log_in
from selenium.webdriver.common.action_chains import ActionChains
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

def test_set_reminders(browser, catalog_page):
    log_in(browser)
    sleep(15)
    catalog_page.wait_for_the_page_to_be_open() # fix

    rail_counter, tile_counter = catalog_page.find_tile_location_with_reminders()

    rail = catalog_page.rails()[rail_counter - 1] # fix, selecting by Id
    tile = catalog_page.tiles_within_rail(rail)[tile_counter]

    ActionChains(browser).move_to_element(rail).perform()
    while not tile.is_displayed():
        catalog_page.rail_next_arrow(rail_counter).click()
        sleep(1)
    tile.click()

    catalog_page.wait_for_reminder_button()
    sleep(5)
    catalog_page.reminder_button_in_pb_container().click()
    sleep(5)

    try:
        if catalog_page.dialog_modal().is_displayed():
            catalog_page.ok_button().click()
            sleep(5)
            catalog_page.reminder_button_in_pb_container().click()
            sleep(3)
    except:
        print("Reminders can be set without the additional modal banner")

    for request in browser.requests:
        if request.headers["Host"] == urls.FAVOURITES_HOST and request.method == "POST": # add endpoint path
            favourites_status_code = request.response.status_code

    assert favourites_status_code == 201
    # wait for element
    assert catalog_page.toast_container_confirmation_banner().is_displayed()
    assert catalog_page.toast_container_dismiss_button().is_displayed()
    sleep(3)
    catalog_page.toast_container_dismiss_button().click()
    sleep(5)

def test_cancel_reminder(browser, catalog_page):
    catalog_page.reminder_button_in_pb_container().click()
    sleep(3)

    for request in browser.requests:
        if request.headers["Host"] == urls.FAVOURITES_HOST and request.method == "DELETE":
            favourites_status_code = request.response.status_code

    assert favourites_status_code == 204
    assert catalog_page.toast_container_confirmation_banner().is_displayed()
    assert catalog_page.toast_container_dismiss_button().is_displayed()

    catalog_page.toast_container_dismiss_button().click()
    sleep(2)

# add test reminders from tiles