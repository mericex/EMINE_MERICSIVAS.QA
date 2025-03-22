from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class BasePage(object):
    # Initialize the driver and wait
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 5)

    # Find element by locator
    def find_element(self, *locator):
        return self.driver.find_element(*locator)

        # Get current url
    def get_current_url(self):
         return self.driver.current_url

    # Click element by locator
    def click_element(self, *locator):
        self.driver.find_element(*locator).click()

    # Hover element by locator
    def hover_element(self, *locator):
        element = self.find_element(*locator)
        hover = ActionChains(self.driver).move_to_element(element)
        hover.perform()

    # Displayed element by locator
    def is_object_visible(self, locator):
        try:
            element = self.find_element(*locator)
            return element.is_displayed()
        except:
            return False

    def wait_element(self, method, message=''):
        return self.wait.until(ec.element_to_be_clickable(method), message)

    def wait_until_element_is_visible(self, *locator):
        return self.wait.until(ec.visibility_of_element_located(*locator))

    def wait_until_element_is_clickable(self, *locator):
        return self.wait.until(ec.element_to_be_clickable(*locator))