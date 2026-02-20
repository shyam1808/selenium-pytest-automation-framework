import json

import pytest

from pages.account import AccountPage
from pages.cart import CartPage
from pages.checkout import CheckOutPage
from pages.home import HomePage
from pages.login import LoginPage
from pages.search import SearchPage
from pages.success import SuccessPage
from pathlib import Path

# BASE_DIR dynamically resolves the folder where this test file exists.
# This avoids hardcoding absolute paths and makes project portable.
BASE_DIR = Path(__file__).parent

# Build test data path relative to project structure.
# Improves CI/CD compatibility which runs on Linux
test_data_path = BASE_DIR / "../testData/test_e2e.json"

# Load external test data once at import time.
with open(test_data_path) as f:
    test_data = json.load(f)
    test_list = test_data["data"]


@pytest.mark.parametrize("test_list_item", test_list)
def test_e2e(browserInstance, test_list_item):
    # browserInstance is a pytest fixture that provides WebDriver setup/teardown.
    driver = browserInstance
    login_page = LoginPage(driver)
    print(login_page.getTitle()) #coming from BrowserUtils class as login page has inherit it
    login_page.login(test_list_item["userEmail"],test_list_item["userPassword"])
    account_page = AccountPage(driver)
    account_page.clickOpencart()
    home_page = HomePage(driver)
    print(home_page.getTitle())
    home_page.searchProduct("Mac")
    search_page = SearchPage(driver)
    search_page.addToCart("MacBook")
    search_page.goToCart()
    cart_page = CartPage(driver)
    cart_page.checkoutstart()
    checkout_page = CheckOutPage(driver)
    checkout_page.fill_new_billing_address()
    checkout_page.fill_existing_delivery_address()
    checkout_page.fill_delivery_method()
    checkout_page.fill_payment_method()
    checkout_page.confirm_order()
    success_page = SuccessPage(driver)
    success_page.validate_order()


