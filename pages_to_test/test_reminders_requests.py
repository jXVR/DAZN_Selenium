import pytest
import assets.urls as urls
from objects.catalog_page_objects import CatalogPageObject
from pages_to_test.test_sign_in_page import log_in
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


@pytest.fixture(scope="session", autouse=True)
def tile_with_reminders(browser, catalog_page):
    rail_name, tile_name = catalog_page.find_tile_location(catalog_page.find_tile_name_with_reminders)
    return rail_name, tile_name


def test_set_reminders_from_rail(browser, catalog_page, tile_with_reminders):
    log_in(browser, account_index=1)

    rail_name, tile_name = tile_with_reminders
    rail = catalog_page.find_rail_container_by_name(rail_name)
    tile = catalog_page.find_tile_container_by_name(tile_name)
    first_tile = catalog_page.tiles_within_rail(rail)[0]

    ActionChains(browser).move_to_element(rail).perform()
    ActionChains(browser).move_to_element(first_tile).perform()

    while not catalog_page.reminder_button_within_tile(tile).is_displayed():
        # changed "while" statement because is_displayed is referring to top left corner and the reminder icon
        # is located in top right corner - edge case when tile is on last place in first block of tiles
        catalog_page.next_arrow_within_rail(rail).click()
        sleep(1)  # just for visibility

    ActionChains(browser).move_to_element(tile).perform()
    catalog_page.reminder_button_within_tile(tile).click()

    try:
        sleep(2)  # because wait for element TimeOut is too long
        if catalog_page.dialog_modal().is_displayed():
            catalog_page.ok_button().click()
            sleep(2)  # just for visibility
            catalog_page.reminder_button_within_tile(tile).click()
    except:
        print("### Reminders can be set without the additional modal banner")
    catalog_page.wait_for_toast_container()
    sleep(1)  # because toast container is dynamic object, it needs to slide in fully

    reminders_status_code = 0
    for request in browser.requests:
        if urls.REMINDERS_ENDPOINT in request.url and request.method == "POST":
            reminders_status_code = request.response.status_code
            print(f"### REMINDERS STATUS CODE {reminders_status_code}")

    assert reminders_status_code == 201
    assert catalog_page.toast_container_confirmation_banner().is_displayed()
    assert catalog_page.toast_container_dismiss_button().is_displayed()

    catalog_page.toast_container_dismiss_button().click()
    sleep(1)  # just for visibility between the tests


def test_cancel_reminder_from_rail(browser, catalog_page, tile_with_reminders):
    rail_name, tile_name = tile_with_reminders
    tile = catalog_page.find_tile_container_by_name(tile_name)

    catalog_page.reminder_button_within_tile(tile).click()
    catalog_page.wait_for_toast_container()
    sleep(1)  # because toast container is dynamic object, it needs to slide in fully

    reminders_status_code = 0
    for request in browser.requests:
        if urls.REMINDERS_ENDPOINT in request.url and request.method == "DELETE":
            reminders_status_code = request.response.status_code

    assert reminders_status_code == 204
    assert catalog_page.toast_container_confirmation_banner().is_displayed()
    assert catalog_page.toast_container_dismiss_button().is_displayed()

    catalog_page.toast_container_dismiss_button().click()
    sleep(1)  # just for visibility


def test_set_reminders(browser, catalog_page, tile_with_reminders):
    rail_name, tile_name = tile_with_reminders
    tile = catalog_page.find_tile_container_by_name(tile_name)
    tile.click()

    catalog_page.wait_for_the_page_to_be_open_without_auto_playback()
    catalog_page.wait_for_reminder_button()
    catalog_page.reminder_button().click()
    catalog_page.wait_for_toast_container()
    sleep(2)  # because toast container is dynamic object, it needs to slide in fully

    reminders_status_code = 0
    for request in browser.requests:
        if urls.REMINDERS_ENDPOINT in request.url and request.method == "POST":
            reminders_status_code = request.response.status_code

    assert reminders_status_code == 201
    assert catalog_page.toast_container_confirmation_banner().is_displayed()
    assert catalog_page.toast_container_dismiss_button().is_displayed()

    catalog_page.toast_container_dismiss_button().click()
    sleep(1)  # just for visibility between the tests


def test_cancel_reminder(browser, catalog_page):
    catalog_page.reminder_button().click()
    catalog_page.wait_for_toast_container()
    sleep(2)  # because toast container is dynamic object, it needs to slide in fully

    reminders_status_code = 0
    for request in browser.requests:
        if urls.REMINDERS_ENDPOINT in request.url and request.method == "DELETE":
            reminders_status_code = request.response.status_code

    assert reminders_status_code == 204
    assert catalog_page.toast_container_confirmation_banner().is_displayed()
    assert catalog_page.toast_container_dismiss_button().is_displayed()

    catalog_page.toast_container_dismiss_button().click()
    sleep(1)  # just for visibility
