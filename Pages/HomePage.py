from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class HomePage(BasePage):
    # locators of the elements
    COMPANY_MENU = (By.CSS_SELECTOR, ".navbar-nav > li:nth-of-type(6) > a")
    CAREER_PAGE = (By.CSS_SELECTOR, ".new-menu-dropdown-layout-6-mid-container a:nth-of-type(2)")

    # hover over the company menu
    def hover_company_menu(self):
        self.hover_element(*self.COMPANY_MENU)

    # click on the career page
    def click_career_page(self):
        self.click_element(*self.CAREER_PAGE)

