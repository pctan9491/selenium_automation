import time
import unittest
import sys
import os
import pyperclip


# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, ElementNotVisibleException, TimeoutException, NoSuchElementException
from selenium_utils.template import SeleniumTemplate
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class HandlingException(SeleniumTemplate, unittest.TestCase):
    def __init__(self, methodName='runTest'):
        SeleniumTemplate.__init__(self, timeout=30) 
        unittest.TestCase.__init__(self, methodName)
        self.base_url = "https://www.geeksforgeeks.org/"

    def test_handling_exception(self):
        try:
            # Setup the driver first
            self.setup_driver(headless=False)
            
            # Navigate to URL
            print(f"\nNavigating to: {self.base_url}")
            self.driver.get(self.base_url)
            print("Page loaded successfully.")

             # Updated method call
            self.element_not_visible_exception()

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Comment out automatic browser closing to allow manual closing
            if hasattr(self, 'driver') and self.driver:
                self.driver.quit()
                print("Browser closed.")
    
    #---------------------------------------------------------------------------
    #test exception: no such element
    def no_such_element_exception(self):
        #true element: //*[@id="comp"]/div[2]/div[1]/div[2]/input (search box in geeks to geeks)
        
        try:
            element = self.driver.find_element(By.XPATH, '//*[@id="com"]/div[2]/div[1]/div[2]/input')
            # Intentionally wrong XPath
            element.send_keys("Hello, World!")
            print("Successfully sent keys to the element.")
        except NoSuchElementException:
            print("Element not found.")
        finally:
            print("Finished testing.")
        
        time.sleep(3)
    
    #test exception: ElementClickInterceptedException
    def element_click_intercepted_exception(self):
        
        try:
            element = self.driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[2]/div/div[2]/a[1]')
            element.click()
            print("Successfully clicked the element.")
        except ElementClickInterceptedException:
            print("Element click intercepted.")
        finally:
            print("Finished testing.")
        
        time.sleep(3)
    
    #test exception: ElementNotInteractableException
    def element_not_interactable_exception(self):
        #example, this method unable to run successfully
        try:
            # First, let's find a hidden or non-interactable element
            # Example 1: Try to click on a hidden element or one that's not visible
            # This XPath targets an element that might be present but not interactable
            hidden_element = self.driver.find_element(By.XPATH, '//input[@type="hidden"]')
            hidden_element.click()  # This should trigger ElementNotInteractableException
            print("Successfully clicked the hidden element.")
        except ElementNotInteractableException:
            print("ElementNotVisibleException: Element is not visible.")
        finally:
            print("Finished testing.")
        
        time.sleep(3)
    
    #test exception: ElementNotSelectableException
    def element_not_selectable_exception(self):
        print("Go see the example of geeks to geeks, here not suitable to demo. Link: https://www.geeksforgeeks.org/python/exceptions-selenium-python/")

    #test exception: ElementNotVisibleException
    def element_not_visible_exception(self):
        #Not suitable to test, because the element is not visible
        try:
            element = self.driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[2]/div/div[2]/a[8]')
            element.click()  # This should trigger ElementNotInteractableException
            print("Successfully clicked the element.")
        except ElementNotVisibleException:
            print("ElementNotVisibleException: Element is not visible.")
        finally:
            print("Finished testing.")
        
        time.sleep(3)
    
    #test exception: ElementNotVisibleException
    def element_not_visible_exception(self):
        #Not suitable to test, because the element is not visible
        try:
            element = self.driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[2]/div/div[2]/a[8]')
            element.click()  # This should trigger ElementNotInteractableException
            print("Successfully clicked the element.")
        except ElementNotVisibleException:
            print("ElementNotVisibleException: Element is not visible.")
        finally:
            print("Finished testing.")
        
        time.sleep(3)
    




