import time
import test_example
import pytest

from selenium import webdriver


@pytest.fixture(scope="session")
def driver(request):
    options = webdriver.ChromeOptions()
    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
    options.add_argument("start-maximized")

    wd = webdriver.Chrome(chrome_options=options)
    wd.implicitly_wait(3)
    request.addfinalizer(wd.quit)
    return wd


def test_logs(driver):
    test_example.test_login(driver)
    driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")
    all_items = driver.find_elements_by_css_selector("[href*=product][title=Edit]")
    for item in range(len(all_items)):
        all_items = driver.find_elements_by_css_selector("[href*=product][title=Edit]")
        all_items[item].click()
        if driver.get_log("browser"):
            for l in driver.get_log("browser"):
                print("here is logs: ", l)
        else:
            print("There are no errors")
        driver.get("http://localhost/litecart/admin/?app=catalog&doc=catalog&category_id=1")