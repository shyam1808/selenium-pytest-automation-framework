
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# "Explicit waits should return WebElements so page actions can be
# chained without additional element lookup."
class WaitUtils:

    def __init__(self, driver, timeout=10):
        # Store driver reference so ExpectedConditions can internally
        # call driver.find_element() during polling.
        self.driver = driver
        # Create a reusable WebDriverWait instance.
        # Centralizing timeout here avoids hardcoding waits in page objects.
        self.wait = WebDriverWait(driver, timeout)

    def visible(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def clickable(self, locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def presence(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))