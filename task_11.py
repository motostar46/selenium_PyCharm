from selenium import webdriver
import pytest
import time


@pytest.fixture
def driver(request):
#    options = webdriver.ChromeOptions()
#    options.binary_location = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
#    options.add_argument("start-maximized")

#    wd = webdriver.Chrome(chrome_options=options)
#    wd.implicitly_wait(3)

    wd = webdriver.Ie()

 #   wd = webdriver.Firefox()
    request.addfinalizer(wd.quit)
    return wd


def test_creating_account(driver):
    driver.get("http://litecart.stqa.ru/en/create_account")
    driver.find_element_by_css_selector("[name=firstname]").send_keys("oleg")
    driver.find_element_by_css_selector("[name=lastname]").send_keys("svistunov")
    driver.find_element_by_css_selector("[name=address1]").send_keys("Baker street 221b")
    driver.find_element_by_css_selector("[name=postcode]").send_keys("12345")
    driver.find_element_by_css_selector("[name=city]").send_keys("London")
    driver.find_element_by_css_selector(".select2-selection__rendered").click()
    driver.find_element_by_css_selector("[name=country_code] [value=US]").click()
    driver.find_element_by_css_selector("select[name=zone_code]").click()
    driver.find_element_by_css_selector("[name=zone_code] [value=AZ]").click()
    email = str(int(time.time())) + "@mail.ru"
    driver.find_element_by_css_selector("[name=email]").send_keys(email)
    driver.find_element_by_css_selector("[name=phone]").send_keys("+799999999")
    driver.find_element_by_css_selector("[name=password]").send_keys("Password123")
    driver.find_element_by_css_selector("[name=confirmed_password]").send_keys("Password123")
    driver.find_element_by_css_selector("[name=create_account]").click()
    driver.find_element_by_link_text("Logout").click()

    driver.find_element_by_css_selector("[name=email]").send_keys(email)
    driver.find_element_by_css_selector("[name=password]").send_keys("Password123")
    driver.find_element_by_css_selector("[name=login]").click()
    driver.find_element_by_link_text("Logout").click()
