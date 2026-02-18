import json
import time

import pytest

from pages.account import AccountPage
from pages.cart import CartPage
from pages.checkout import CheckOutPage
from pages.home import HomePage
from pages.login import LoginPage
from pages.search import SearchPage
from pages.success import SuccessPage

test_data_path = "testdata/test_e2e.json"
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    driver = browserInstance
    driver.implicitly_wait(10)
    login_page = LoginPage(driver)
    #print(login_Page.getTitle())
    login_page.login(test_list_item["userEmail"],test_list_item["userPassword"])
    #time.sleep(2)
    account_page = AccountPage(driver)
    account_page.clickOpencart()
    home_page = HomePage(driver)
    #time.sleep(2)
    #print(shop_Page.getTitle())
    home_page.searchProduct("Mac")
    #time.sleep(2)
    search_page = SearchPage(driver)
    #time.sleep(2)
    search_page.addToCart("MacBook")
    #time.sleep(2)
    search_page.goToCart()
    #time.sleep(2)
    cart_page = CartPage(driver)
    cart_page.checkoutstart()
    #time.sleep(2)
    checkout_page = CheckOutPage(driver)
    checkout_page.fill_new_billing_address()
    #time.sleep(2)
    checkout_page.fill_existing_delivery_address()
    #time.sleep(2)
    checkout_page.fill_delivery_method()
    #time.sleep(2)
    checkout_page.fill_payment_method()
    #time.sleep(2)
    checkout_page.confirm_order()
    #time.sleep(2)
    success_page = SuccessPage(driver)
    success_page.validate_order()


