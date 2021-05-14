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

def test_subscribe_favourites(browser, catalog_page):
    log_in(browser)
    catalog_page.wait_for_the_page_to_be_open()

    rail_counter, tile_counter = catalog_page.find_tile_location_with_fav()

    rail = catalog_page.rails()[rail_counter]
    tile = catalog_page.tiles_within_rail(rail)[tile_counter]

    ActionChains(browser).move_to_element(rail).perform()
    while not tile.is_displayed():
        catalog_page.rail_next_arrow(rail_counter).click()
        sleep(1)
    tile.click()

    catalog_page.wait_for_favourite_button()
    catalog_page.favourite_button().click()

    assert catalog_page.favourite_list().is_displayed()
    catalog_page.favourite_item()[0].click()
    sleep(5) # sleep to give time to process the request
    catalog_page.favourite_button().click()

    for request in browser.requests:
        if request.headers["Host"] == urls.FAVOURITES_HOST and request.method == "POST":
            favourites_status_code = request.response.status_code

    assert favourites_status_code == 201
    assert catalog_page.toast_container_confirmation_banner().is_displayed()
    assert catalog_page.toast_container_dismiss_button().is_displayed()

    catalog_page.toast_container_dismiss_button().click()
    sleep(1)

def test_unsubscribe_favourites(browser, catalog_page):
    catalog_page.favourite_button().click()

    assert catalog_page.favourite_list().is_displayed()
    catalog_page.favourite_item()[0].click()
    sleep(5) # sleep to give time to process the request
    catalog_page.favourite_button().click()

    for request in browser.requests:
        if request.headers["Host"] == urls.FAVOURITES_HOST and request.method == "DELETE":
            favourites_status_code = request.response.status_code

    assert favourites_status_code == 204
    assert catalog_page.toast_container_confirmation_banner().is_displayed()
    assert catalog_page.toast_container_dismiss_button().is_displayed()

    catalog_page.toast_container_dismiss_button().click()
    sleep(2)

# def test_tiles_video_responses(catalog_page):
#     tile_videos_links = catalog_page.page_links()
#     print("\n")
#     for element in tile_videos_links:
#         url = element.get_attribute('href')
#         if "https://" in url:
#             status_code = requests.get(url).status_code
#             if status_code != 200:
#                 print(status_code, url)
