import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class BaseTest(unittest.TestCase):
    base_url = 'https://useinsider.com/'

    def setUp(self):
        chrome_options = Options()
        chrome_options.add_argument("--disable-notifications")
        self.driver = webdriver.Chrome(chrome_options)
        self.driver.maximize_window()
        self.driver.get('https://useinsider.com/')
        self.driver.implicitly_wait(15)

    def tearDown(self):
        self.driver.quit()
