import pytest
import Selenium.DAZN.assets.urls as urls
from Selenium.DAZN.objects.sports_page_objects import SportsPageObject
from Selenium.DAZN.objects.catalog_page_objects import CatalogPageObject
from Selenium.DAZN.pages_to_test.test_sign_in_page import log_in
from selenium.webdriver import Chrome


@pytest.fixture(scope="session", autouse=True)
def browser():
    driver = Chrome()
    driver.get(urls.SIGN_IN_URL)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

# @pytest.fixture(scope="session", autouse=True)
# def sports_page(browser):
#     sports_page = SportsPageObject(browser)
#     return sports_page
#
# @pytest.fixture(scope="session", autouse=True)
# def catalog_page(browser):
#     catalog_page = CatalogPageObject(browser)
#     return catalog_page


def test_go_to_sports_page(browser):
    log_in(browser)
    catalog_page = CatalogPageObject(browser)
    sports_page = SportsPageObject(browser)

    catalog_page.sports_dropdown().click()
    catalog_page.wait_for_the_sports_dropdown()
    catalog_page.sports_dropdown_items()[0].click()
    sports_page.wait_for_the_page_to_be_open()

    assert sports_page.page_title().is_displayed()
    assert sports_page.page_title().get_attribute("innerText") == "FOOTBALL"

def test_first_rail_name(browser):
    sports_page = SportsPageObject(browser)
    assert sports_page.rail_names()[0].get_attribute("innerText") == "Competitions"

def test_first_competition_name(browser):
    sports_page = SportsPageObject(browser)
    assert sports_page.competitions_tiles()[0].get_attribute("innerText") == "Copa Del Rey"
