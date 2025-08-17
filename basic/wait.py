import time
import unittest
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium_utils.template import SeleniumTemplate

class ExAndInWait(SeleniumTemplate, unittest.TestCase):
    def __init__(self, methodName='runTest'):
        SeleniumTemplate.__init__(self, timeout=30) 
        unittest.TestCase.__init__(self, methodName)
        self.base_url = "https://www.geeksforgeeks.org/"

    def test_wait(self):
        try:
            # Setup the driver first
            self.setup_driver(headless=False)
            wait = WebDriverWait(self.driver, 10)
            
            # Navigate to URL
            print(f"\nNavigating to: {self.base_url}")
            self.driver.get(self.base_url)
            print("Page loaded successfully.")

            self.set_implicit_wait(4)
            search_box = self.wait_for_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
            search_box.send_keys('implicit wait for 4s')
            print('implicit wait for 4s')
            
            self.set_implicit_wait(5)
            # Navigate to GeeksforGeeks and interact with JavaScript section
            print("\nNavigating to JavaScript section...")
            # Wait for and click JavaScript link
            javascript_link = self.set_explicit_wait(
                EC.element_to_be_clickable,
                (By.XPATH, "//*[@id='secondarySubHeader']/ul/li[7]/a")
            )
            javascript_link.click()
            print("Clicked JavaScript link")

             # Wait for page to load
            time.sleep(4)
            # Smart scroll to find and click fundamentals link
            fundamentals_intro_link = self.smart_scroll_to_element(
                By.XPATH, "//*[@id='post-1109174']/div[3]/ul[3]/li[1]/a/span"
            )
            print("Found and clicked Fundamentals Intro link")
            fundamentals_intro_link.click()
            print("Clicked Fundamentals introduction link")

            
            print("Navigation completed successfully!")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Comment out automatic browser closing to allow manual closing
            # if hasattr(self, 'driver') and self.driver:
            #     self.driver.quit()
            #     print("Browser closed.")
            print("Script completed. Browser left open for manual closing.")