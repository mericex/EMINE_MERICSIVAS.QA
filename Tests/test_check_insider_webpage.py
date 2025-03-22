import time

from Pages.CareerPage import CareerPage
from Pages.HomePage import HomePage
from Tests.test_base import BaseTest
from Pages.QAJobsPage import QAJobsPage


class TestCheckInsiderWebpage(BaseTest):
    def test_insider_website(self):
        home_page = HomePage(self.driver)
        # Check Homepage related requirements
        self.assertEqual(self.base_url, home_page.get_current_url(), 'YOU ARE NOT ON INSIDER HOME PAGE')
        home_page.hover_company_menu()
        home_page.click_career_page()
        # check if the blocks are loaded
        career_page = CareerPage(self.driver)
        self.assertTrue(career_page.display_locations(), "Locations section is not visible!")
        self.assertTrue(career_page.display_life_at_insider(), "Life at Insider section is not visible!")
        self.assertTrue(career_page.display_teams(), "Teams section is not visible!")
        # go to qa jobs page
        qa_jobs_page = QAJobsPage(self.driver)
        self.driver.get(qa_jobs_page.QA_JOBS_URL)
        time.sleep(3)
        # click see all jobs
        qa_jobs_page.click_see_all_jobs()
        time.sleep(15)
        # click location dropdown
        qa_jobs_page.click_location_from_dropdown()
        time.sleep(3)
        # click department dropdown
        qa_jobs_page.click_department_from_dropdown('Quality Assurance')
        # check job validity
        qa_jobs_page.check_job_validity('Istanbul, Turkiye', 'Quality Assurance')
        qa_jobs_page.view_role()





