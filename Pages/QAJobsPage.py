import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from Pages.BasePage import BasePage


class QAJobsPage(BasePage):
    # locators of the elements
    QA_JOBS_URL = 'https://useinsider.com/careers/quality-assurance/'
    SEE_ALL_JOBS = (By.CSS_SELECTOR, "a[href='https://useinsider.com/careers/open-positions/?department=qualityassurance']")
    LOCATION_DROPDOWN = (By.ID, "select2-filter-by-location-container")
    DEPARTMENT_DROPDOWN = (By.ID, "select2-filter-by-department-container")
    LOCATION_SELECTION = (By.XPATH, "//li[contains(@id, 'select2-filter-by-location-result') and text()='Istanbul, Turkiye']")
    DEPARTMENTS_LIST = (By.XPATH, "//span[@id='select2-filter-by-department-container")
    POSITIONS_LIST = (By.ID, "jobs-list")
    DEPARTMENT_SELECTION = (By.ID, 'filter-by-department')
    OPEN_POSITION_LIST = (By.CSS_SELECTOR, '#career-position-list .row')
    OPEN_POSITION_CARDS = (By.CSS_SELECTOR, ".position-list-item")
    CARD_POS_TITLE = (By.CSS_SELECTOR, ".position-title")
    CARD_POS_DEPARTMENT = (By.CSS_SELECTOR, ".position-department")
    CARD_POS_LOCATION = (By.CSS_SELECTOR, ".position-location")
    VIEW_ROLE_BUTTON = (By.LINK_TEXT, "View Role")
    VIEW_ROLE_LINKS = (By.XPATH, "//a[contains(@class, 'btn-navy') and text()='View Role']")

    def click_see_all_jobs(self):
        self.click_element(*self.SEE_ALL_JOBS)

    def click_location_from_dropdown(self):
        dropdown_location = self.wait.until(EC.element_to_be_clickable(self.LOCATION_DROPDOWN))
        self.click_element(*self.LOCATION_DROPDOWN)
        location = self.wait.until(EC.element_to_be_clickable(self.LOCATION_SELECTION))
        self.click_element(*self.LOCATION_SELECTION)

    def click_department_from_dropdown(self, department):
        # department
        department_dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.DEPARTMENT_DROPDOWN)
        )
        time.sleep(1)
        department_dropdown.click()
        time.sleep(1)
        select_element = self.driver.find_element(*self.DEPARTMENT_SELECTION)
        select = Select(select_element)
        for option in select.options:
            if option.text == department:
                option.click()
        time.sleep(1)
        department_dropdown.click()
        time.sleep(5)

    def check_job_validity(self, location, department):
        cards = self.driver.find_elements(*self.OPEN_POSITION_CARDS)
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});",
                                   self.driver.find_element(*self.OPEN_POSITION_LIST))
        time.sleep(1)
        for job in cards:
            job_title = job.find_element(*self.CARD_POS_TITLE).text
            job_department = job.find_element(*self.CARD_POS_DEPARTMENT).text
            job_location = job.find_element(*self.CARD_POS_LOCATION).text
            if "Quality Assurance" not in job_title or job_department != department or location not in job_location:
                return False
        return True

    def view_role(self):
        view_role_links = self.wait.until(
            EC.presence_of_all_elements_located(self.VIEW_ROLE_LINKS))
        view_role_links = self.driver.find_elements(*self.VIEW_ROLE_LINKS)
        # Click each "View Role" link (opens new tabs)
        for link in view_role_links:
            link.click()
            time.sleep(2)
            window_handles = self.driver.window_handles
            # switch to second tab
            self.driver.switch_to.window(window_handles[1])
            validation = WebDriverWait(self.driver, 10).until(EC.url_contains("lever.co"))
            if validation is False:
                return False
            else:
                # switch to first tab
                self.driver.switch_to.window(window_handles[0])
                time.sleep(2)
