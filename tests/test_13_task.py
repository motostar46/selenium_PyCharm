from pages.main_page import MainPage
from pages.item_page import ItemPage
from pages.cart_page import CartPage
import time


def test_creating_account(driver):
    main_page = MainPage(driver)
    item_page = ItemPage(driver)
    cart_page = CartPage(driver)

    for i in range(3):
        main_page.open()
        main_page.choose_first_item()

        item_page.choose_small_item_size()
        item_page.add_to_cart()

    item_page.checkout()
    cart_page.remove_all_items_in_cart()