import pytest
import Selenium.DAZN.assets.urls as urls
from Selenium.DAZN.objects.sports_page_objects import SportsPageObject
from Selenium.DAZN.objects.catalog_page_objects import CatalogPageObject
from Selenium.DAZN.objects.competition_page_objects import CompetitionPageObject
from Selenium.DAZN.pages_to_test.test_sign_in_page import log_in
from selenium.webdriver import Chrome


@pytest.fixture(scope="session", autouse=True)
def browser():
    driver = Chrome()
    driver.get(urls.SIGN_IN_URL)
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_go_to_competition_page(browser):
    log_in(browser)
    catalog_page = CatalogPageObject(browser)
    sports_page = SportsPageObject(browser)
    competition_page = CompetitionPageObject(browser)

    catalog_page.sports_dropdown().click()
    catalog_page.wait_for_the_sports_dropdown()
    for sport in catalog_page.sports_dropdown_items():
        if sport.get_attribute("innerText") == "Football":
            sport.click()
            break
    sports_page.wait_for_the_page_to_be_open()

    assert sports_page.page_title().is_displayed()
    assert sports_page.page_title().get_attribute("innerText") == "FOOTBALL"

    for competition in sports_page.competitions_tiles():
        if competition.get_attribute("innerText") == "Bundesliga":
            competition.click()
            break

    assert competition_page.page_title().is_displayed()
    assert competition_page.page_title().get_attribute("innerText") == "BUNDESLIGA"

def test_sportsdata_menu(browser):
    competition_page = CompetitionPageObject(browser)

    assert competition_page.sports_data_menu().is_displayed()
    assert competition_page.watch_button().is_displayed()
    assert competition_page.standings_button().is_displayed()
    assert competition_page.matches_button().is_displayed()

def test_follow_button(browser):
    competition_page = CompetitionPageObject(browser)

    assert competition_page.follow_button().is_displayed()
    # test popup message
    # test if the call was sent