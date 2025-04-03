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
    def __init__(self, methodName='runTest'):  # Change this line
        SeleniumTemplate.__init__(self, timeout=30)
        unittest.TestCase.__init__(self, methodName)  # Add methodName here
        self.base_url = "https://www.geeksforgeeks.org/"

    def test_assert_write(self):  # Changed method name to start with "test_"
        try:
            # Setup the driver first
            self.setup_driver(headless=False)
            
            # Then navigate and perform actions
            self.navigate_to(self.base_url)
           
            # Find the search bar and enter a query
            search_box = self.wait_for_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[3]/input')
            search_box.send_keys("JavaScript")
            search_box.send_keys(Keys.ENTER)
            time.sleep(4)
            
            # Find search results and verify JavaScript content
            search_results = self.wait_for_element(By.CLASS_NAME, "HomePageSearchModal_homePageSearchModalContainer_modal_container_content__drrYe")
            self.assertTrue("JavaScript" in search_results.text, "Search results should contain 'JavaScript'")
            
        except Exception as e:
            print(f"Error performing search: {e}")
            raise  # Raise the exception to fail the test
        
        finally:
            if self.driver:  # Only cleanup if driver exists
                self.cleanup()

    def tearDown(self):
        if self.driver:  # Only cleanup if driver exists
            self.cleanup()