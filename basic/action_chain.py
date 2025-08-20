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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class ActionChainTest(SeleniumTemplate, unittest.TestCase):
    def __init__(self, methodName='runTest'):
        SeleniumTemplate.__init__(self, timeout=30) 
        unittest.TestCase.__init__(self, methodName)
        self.base_url = "https://www.geeksforgeeks.org/"

    def test_action_chain(self):
        try:
            # Setup the driver first
            self.setup_driver(headless=False)
            
            # Navigate to URL
            print(f"\nNavigating to: {self.base_url}")
            self.driver.get(self.base_url)
            print("Page loaded successfully.")

             # Updated method call
            self.action_chain_click_and_hold()

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Comment out automatic browser closing to allow manual closing
            if hasattr(self, 'driver') and self.driver:
                self.driver.quit()
                print("Browser closed.")
    
    #---------------------------------------------------------------------------
    #test action chain: clicked
    def action_chain_clicked(self):
        # Click method
        click_element = self.wait_for_clickable(By.XPATH, '//*[@id="topMainHeader"]/div/ul/li[1]/span/div')
        action = ActionChains(self.driver)
        action.click(click_element).perform()
        print("Successfully perform action chain for click!")
        # Wait a bit to see the result
        time.sleep(3)
    
    #test action chain: click and hold
    def action_chain_click_and_hold(self):
        # Click method
        click_and_hold_element = self.wait_for_clickable(By.XPATH, '//*[@id="topMainHeader"]/div/a/div/img')
        target = self.wait_for_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')

        action = ActionChains(self.driver)
        action.click_and_hold(click_and_hold_element)
        action.move_to_element(target)
        action.release(target)
        action.perform()
        target.send_keys(Keys.RETURN)

        print("Successfully perform action chain for click and hold!")
        # Wait a bit to see the result
        time.sleep(3)
