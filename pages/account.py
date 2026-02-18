from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.home import HomePage


class AccountPage():
    def __init__(self,driver):
        self.driver = driver
        self.opencart_logo = (By.XPATH,"//a/img[@class='img-responsive']")


    def clickOpencart(self):
        self.driver.find_element(*self.opencart_logo).click()



