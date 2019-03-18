import pytest
from selenium import webdriver
import time


def parsing_color(arg):
    for i in range(len(arg)):
        if arg[i] == "(":
            x = i + 1
        if arg[i] == ")":
            y = i
    return [int(every) for every in arg[x:y].split(',')]

@pytest.fixture(scope="session")
def driver(request):
    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("start-maximized")

    wd = webdriver.Chrome(chrome_options=options)

 #   wd = webdriver.Ie()

 #   wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_styles_on_main_page(driver):
    driver.implicitly_wait(3)
    driver.get("http://localhost/litecart/")
    old_price_element = driver.find_element_by_css_selector("#box-campaigns .regular-price")
    new_price_element = driver.find_element_by_css_selector("#box-campaigns .campaign-price")

    color_old_price = old_price_element.value_of_css_property("color")
    color_new_price = new_price_element.value_of_css_property("color")
    crossed_old_price = old_price_element.value_of_css_property("text-decoration")
    bold_new_price = new_price_element.value_of_css_property("font-weight")

    color_old_parsed = parsing_color(color_old_price)
    color_new_parsed = parsing_color(color_new_price)

    assert ((new_price_element.value_of_css_property("font-size") > old_price_element.value_of_css_property("font-size")
             ), "The old price font is bigger than new one")
    assert color_old_parsed[0] == color_old_parsed[1] == color_old_parsed[2], "The old price color is not grey"
    assert color_new_parsed[1] == color_new_parsed[2] == 0, "The new price color is not red"
    assert crossed_old_price[:12] == 'line-through', "The old price is not crossed"
    assert int(bold_new_price) >= 700, "The new price is not bold"
    print("Values: %s | %s | %s | %s " % (color_old_price, crossed_old_price, color_new_price, bold_new_price))


def test_compare_pages(driver):
    first_item = driver.find_element_by_xpath("//div[@id='box-campaigns']//a")

    name_on_main_page = first_item.find_element_by_css_selector(".name").text
    old_price_on_main_page = first_item.find_element_by_css_selector(".regular-price").text
    new_price_on_main_page = first_item.find_element_by_css_selector(".campaign-price").text

    first_item.click()

    name_on_item_page = driver.find_element_by_xpath("//h1[@itemprop='name']").text
    old_price_on_item_page = driver.find_element_by_css_selector('#box-product .regular-price').text
    new_price_on_item_page = driver.find_element_by_css_selector('#box-product .campaign-price').text

    assert name_on_main_page == name_on_item_page, "The item names is different"
    assert old_price_on_main_page == old_price_on_item_page, " The old prices is different"
    assert new_price_on_main_page == new_price_on_item_page, "The new prices is different "


def test_styles_on_item_page(driver):
    old_price_element = driver.find_element_by_css_selector("#box-product .regular-price")
    new_price_element = driver.find_element_by_css_selector("#box-product .campaign-price")

    color_old_price = old_price_element.value_of_css_property("color")
    color_new_price = new_price_element.value_of_css_property("color")
    crossed_old_price = old_price_element.value_of_css_property("text-decoration")
    bold_new_price = new_price_element.value_of_css_property("font-weight")

    color_old_parsed = parsing_color(color_old_price)
    color_new_parsed = parsing_color(color_new_price)

    assert ((new_price_element.value_of_css_property("font-size") > old_price_element.value_of_css_property("font-size")
             ), "The old price font is bigger than new one")
    assert color_old_parsed[0] == color_old_parsed[1] == color_old_parsed[2], "The old price color is not grey"
    assert color_new_parsed[1] == color_new_parsed[2] == 0, "The new price color is not red"
    assert crossed_old_price[:12] == 'line-through', "The old price is not crossed"
    assert int(bold_new_price) >= 700, "The new price is not bold"
    print("Values: %s | %s | %s | %s " % (color_old_price, crossed_old_price, color_new_price, bold_new_price))

