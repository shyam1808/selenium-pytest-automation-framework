from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select



class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver
        self.newaddress_radio = (By.XPATH,'(//input[@value="new"])[1]')
        self.first_name_field = (By.XPATH, '//input[@name="firstname"]')
        self.last_name_field = (By.XPATH, '//input[@name="lastname"]')
        self.address_field = (By.XPATH, '//input[@name="address_1"]')
        self.city_field = (By.XPATH, '//input[@name="city"]')
        self.postal_code_field = (By.XPATH, '//input[@name="postcode"]')
        self.country_dropdown = (By.ID, 'input-payment-country')
        self.region_dropdown = (By.ID, 'input-payment-zone')
        self.billing_continue_button = (By.ID, 'button-payment-address')
        self.shipping_continue_button = (By.ID, 'button-shipping-address')
        self.delivery_method_continue_button = (By.ID, 'button-shipping-method')
        self.terms_check_box = (By.XPATH, '//input[@name="agree"]')
        self.payment_method_continue_button = (By.ID, 'button-payment-method')
        self.confirm_order_continue_button = (By.ID,'button-confirm')


    def fill_new_billing_address(self):
        self.driver.find_element(*self.newaddress_radio).click()
        self.driver.find_element(*self.first_name_field).send_keys("Shyamal")
        self.driver.find_element(*self.last_name_field).send_keys("Srivastava")
        self.driver.find_element(*self.address_field).send_keys("Dummy address 12992")
        self.driver.find_element(*self.city_field).send_keys("test city")
        self.driver.find_element(*self.postal_code_field).send_keys("80111")
        country = self.driver.find_element(*self.country_dropdown)
        selectcountry = Select(country)
        selectcountry.select_by_visible_text("United States")

        region = self.driver.find_element(*self.region_dropdown)
        selectregion = Select(region)
        selectregion.select_by_visible_text("Texas")
        self.driver.find_element(*self.billing_continue_button).click()

    def fill_existing_delivery_address(self):
        self.driver.find_element(*self.shipping_continue_button).click()


    def fill_delivery_method(self):
        self.driver.find_element(*self.delivery_method_continue_button).click()

    def fill_payment_method(self):
        self.driver.find_element(*self.terms_check_box).click()
        self.driver.find_element(*self.payment_method_continue_button).click()


    def confirm_order(self):
        self.driver.find_element(*self.confirm_order_continue_button).click()








