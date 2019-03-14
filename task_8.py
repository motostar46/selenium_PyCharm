import pytest
from selenium import webdriver
import time


@pytest.fixture
def driver(request):
    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("start-maximized")

    wd = webdriver.Chrome(chrome_options=options)
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.implicitly_wait(3)
    driver.get("http://localhost/litecart/")
    duckling_elements = driver.find_elements_by_css_selector("[class='product column shadow hover-light']")
    for duck in duckling_elements:
        sticker = duck.find_elements_by_css_selector("[class^='sticker']")
        if len(sticker) == 1:
            True
        else:
            return False

 #   time.sleep(2)