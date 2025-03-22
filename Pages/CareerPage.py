from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class CareerPage(BasePage):
    LOCATIONS = (By.CSS_SELECTOR, "#career-our-location")
    LIFE_AT_INSIDER = (By.CSS_SELECTOR, ".elementor-section .elementor-widget-heading h2")
    TEAMS = (By.CSS_SELECTOR, ".job-item")

    # display locations
    def display_locations(self):
        return self.is_object_visible(self.LOCATIONS)

    # display life at insider
    def display_life_at_insider(self):
        return self.is_object_visible(self.LIFE_AT_INSIDER)

    # display teams
    def display_teams(self):
        return self.is_object_visible(self.TEAMS)
