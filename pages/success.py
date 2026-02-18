from selenium.webdriver.common.by import By


class SuccessPage:
    def __init__(self, driver):
        self.driver = driver
        self.success_message = (By.CLASS_NAME, 'col-sm-12')
        self.continue_button = (By.XPATH, '//div/a[@class="btn btn-primary"]')



    def validate_order(self):
        successText = self.driver.find_element(*self.success_message).text
        print(successText)
        assert "successfully processed!" in successText.lower()
        self.driver.find_element(*self.continue_button).click()