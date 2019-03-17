import pytest
from selenium import webdriver
import test_example
import time


@pytest.fixture(scope="session")
def driver(request):
    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("start-maximized")

    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_sorting(driver):
    test_example.test_login(driver)
    driver.implicitly_wait(3)
    driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")
    all_rows = driver.find_elements_by_xpath("//form[@name='countries_form']//tr[@class='row']")
    all_countries = []
    countries_zones = []

    for i in range(len(all_rows)):
        all_countries.append(all_rows[i].find_element_by_css_selector('a:not([title])').text)
        if all_rows[i].find_element_by_xpath('td[6]').text != '0':
            countries_zones.append(i + 1)

    all_countries_sorted = all_countries.copy()
    all_countries_sorted.sort()
    assert(all_countries == all_countries_sorted), 'List of countries is not sorted'

    for i in range(len(countries_zones)):
        xpath_country_with_zones = "//form[@name='countries_form']//tr[@class='row'][" + str(countries_zones[i]) + "]"
        element = driver.find_element_by_xpath(xpath_country_with_zones)
        element.find_element_by_css_selector('a:not([title])').click()
        zones_elements = driver.find_elements_by_css_selector(".dataTable [name*=name][type=hidden]")

        zones = []
        for j in range(len(zones_elements)):
            zones.append(zones_elements[j].get_attribute("value"))
        zones_sorted = zones.copy()
        zones_sorted.sort()
        assert (zones_sorted == zones), 'List of zones is not sorted'
        driver.get("http://localhost/litecart/admin/?app=countries&doc=countries")



