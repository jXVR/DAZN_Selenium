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


def test_subscribe_favourites(browser, catalog_page):
    log_in(browser, account_index=1)
    rail_name, tile_name = catalog_page.find_tile_location(catalog_page.find_tile_name_with_fav)
    rail = catalog_page.find_rail_container_by_name(rail_name)
    tile = catalog_page.find_tile_container_by_name(tile_name)
    first_tile = catalog_page.tiles_within_rail(rail)[0]

    ActionChains(browser).move_to_element(rail).perform()
    ActionChains(browser).move_to_element(first_tile).perform()

    while not tile.is_displayed():
        catalog_page.next_arrow_within_rail(rail).click()
        sleep(1)  # just for visibility

    tile.click()
    catalog_page.wait_for_favourite_button()
    catalog_page.favourite_button().click()
    catalog_page.wait_for_favourite_list()

    assert catalog_page.favourite_list().is_displayed()

    catalog_page.favourite_item()[0].click()
    catalog_page.wait_for_toast_container()
    sleep(1)  # because toast container is dynamic object, it needs to slide in fully
    catalog_page.favourite_button().click()

    favourites_status_code = 0
    for request in browser.requests:
        if urls.REMINDERS_ENDPOINT in request.url and request.method == "POST":
            favourites_status_code = request.response.status_code

    assert favourites_status_code == 201
    assert catalog_page.toast_container_confirmation_banner().is_displayed()
    assert catalog_page.toast_container_dismiss_button().is_displayed()

    catalog_page.toast_container_dismiss_button().click()
    sleep(3)  # just for visibility between tests


def test_unsubscribe_favourites(browser, catalog_page):
    catalog_page.favourite_button().click()
    catalog_page.wait_for_favourite_list()

    assert catalog_page.favourite_list().is_displayed()

    catalog_page.favourite_item()[0].click()
    catalog_page.wait_for_toast_container()
    sleep(1)  # because toast container is dynamic object, it needs to slide in fully
    catalog_page.favourite_button().click()

    favourites_status_code = 0
    for request in browser.requests:
        if urls.REMINDERS_ENDPOINT in request.url and request.method == "DELETE":
            favourites_status_code = request.response.status_code

    assert favourites_status_code == 204
    assert catalog_page.toast_container_confirmation_banner().is_displayed()
    assert catalog_page.toast_container_dismiss_button().is_displayed()

    catalog_page.toast_container_dismiss_button().click()
    sleep(1)  # just for visibility

# def test_tiles_video_responses(catalog_page):
#     tile_videos_links = catalog_page.page_links()
#     print("\n")
#     for element in tile_videos_links:
#         url = element.get_attribute('href')
#         if "https://" in url:
#             status_code = requests.get(url).status_code
#             if status_code != 200:
#                 print(status_code, url)
