import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
#    options = webdriver.IeOptions()
#    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
#    options.add_argument("start-maximized")

    wd = webdriver.Ie()
    request.addfinalizer(wd.quit)
    return wd


def test_example(driver):
    driver.get("http://google.com")
