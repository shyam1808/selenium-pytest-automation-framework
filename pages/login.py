from selenium import webdriver
from selenium.webdriver.common.by import By

from pages.account import AccountPage
from utils.browserUtils import BrowserUtils


class LoginPage(BrowserUtils): # Make LoginPage inherit BrowserUtils so that we can reuse functions in tests
    def __init__(self,driver):
        self.driver = driver
        self.username_input = (By.ID,"input-email")
        self.password_input = (By.ID,"input-password")
        self.login_button = (By.XPATH,"//input[@type='submit']")


    def login(self,username,password):
        self.driver.find_element(*self.username_input).send_keys(username)
        self.driver.find_element(*self.password_input).send_keys(password)
        self.driver.find_element(*self.login_button).click()
        account_Page = AccountPage(self.driver)
        return account_Page


