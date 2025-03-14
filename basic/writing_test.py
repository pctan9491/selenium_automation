import os
import sys
import unittest
# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_utils.template import SeleniumTemplate
import time

class WritingTest(SeleniumTemplate, unittest.TestCase):
    def __init__(self, timeout=30):
        super().__init__(timeout)
        self.base_url = "https://www.geeksforgeeks.org/"

    def assert_write_test(self):
        try:
            # Setup the driver first
            self.setup_driver(headless=False)
            
            # Then navigate and perform actions
            self.navigate_to(self.base_url)
           
            # Find the search bar and enter a query
            search_box = self.wait_for_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
            search_box.send_keys("JavaScript")
            search_box.send_keys(Keys.ENTER)
            time.sleep(4)
            assert "No results found." not in self.driver.page_source
            
        except Exception as e:
            print(f"Error performing search: {e}")
            # return False
        
        finally:
            if self.driver:  # Only cleanup if driver exists
                self.cleanup()

    def tearDown(self):
        if self.driver:  # Only cleanup if driver exists
            self.cleanup()