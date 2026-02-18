import time

from selenium.webdriver.common.by import By


class SearchPage:
    def __init__(self, driver):
        self.driver = driver
        self.itemcards = (By.XPATH, "//div[@class='product-layout product-grid col-lg-3 col-md-3 col-sm-6 col-xs-12']")
        self.cart_button = (By.XPATH, "//button[@class='btn btn-inverse btn-block btn-lg dropdown-toggle']")
        self.view_cart_button = (By.XPATH, "//strong[text()=' View Cart']")


    def addToCart(self, product_name):
        products = self.driver.find_elements(*self.itemcards)

        for product in products:
            productName = product.find_element(By.XPATH, "div/div/div/h4/a").text
            if product_name.lower() in productName.lower() :
                product.find_element(By.XPATH, "div/div/div/button[1]").click()
                time.sleep(2)

    def goToCart(self):
        self.driver.find_element(*self.cart_button).click()
        self.driver.find_element(*self.view_cart_button).click()

