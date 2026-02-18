from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_bar = (By.CSS_SELECTOR, "#search > input")
        self.search_button = (By.CSS_SELECTOR, "#search > span")


    def searchProduct(self, product_name):
        print(product_name)
        self.driver.find_element(*self.search_bar).send_keys(product_name)
        self.driver.find_element(*self.search_button).click()

