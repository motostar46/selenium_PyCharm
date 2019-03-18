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


def test_prices(driver):
    driver.implicitly_wait(3)
    driver.get("http://localhost/litecart/")
    first_item = driver.find_element_by_xpath("//div[@id='box-campaigns']//a")
    old_price_element = first_item.find_element_by_css_selector(".regular-price")
    new_price_element = first_item.find_element_by_css_selector(".campaign-price")

    name_on_main_page = first_item.find_element_by_css_selector(".name").text
    old_price_on_main_page = old_price_element.text
    new_price_on_main_page = new_price_element.text

    color_old_price_main_page = old_price_element.value_of_css_property("color")
    color_new_price_main_page = new_price_element.value_of_css_property("color")
    crossed_old_main_page = old_price_element.value_of_css_property("text-decoration")
    bold_new_main_page = new_price_element.value_of_css_property("font-weight")

    assert ((new_price_element.value_of_css_property("font-size") > old_price_element.value_of_css_property("font-size"))
            , "The old price font is bigger than new one")
    print("Values:  ", name_on_main_page, old_price_on_main_page, new_price_on_main_page, color_old_price_main_page,
          crossed_old_main_page, color_new_price_main_page, bold_new_main_page)
