from asyncio.windows_events import NULL
from re import A
import time
import unittest
import sys
import os
import pyperclip
from selenium.webdriver.common import desired_capabilities


# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementClickInterceptedException, ElementNotInteractableException, ElementNotVisibleException, ImeActivationFailedException, ImeNotAvailableException, InsecureCertificateException, InvalidArgumentException, InvalidCookieDomainException, InvalidCoordinatesException, InvalidElementStateException, InvalidSelectorException, InvalidSessionIdException, InvalidSwitchToTargetException, NoAlertPresentException, NoSuchAttributeException, NoSuchCookieException, StaleElementReferenceException, TimeoutException, NoSuchElementException, UnableToSetCookieException
from selenium_utils.template import SeleniumTemplate
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

class AssertTesting(SeleniumTemplate, unittest.TestCase):
    def __init__(self, methodName='runTest'):
        SeleniumTemplate.__init__(self, timeout=30) 
        unittest.TestCase.__init__(self, methodName)
        self.base_url = "https://www.geeksforgeeks.org/"

    def test_assertions_testng(self):
        try:
            # Setup the driver first
            self.setup_driver(headless=False)
            
            # Navigate to URL
            print(f"\nNavigating to: {self.base_url}")
            self.driver.get(self.base_url)
            print("Page loaded successfully.")

             # Updated method call
            self.assert_is_not_none_testing()

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Comment out automatic browser closing to allow manual closing
            if hasattr(self, 'driver') and self.driver:
                self.driver.quit()
                print("Browser closed.")


    def assert_equal_testing(self):
        try:
            word_element = self.driver.find_element(By.XPATH, "//*[@id='comp']/div[2]/div[1]/div[1]")
            # Assert equal
            self.assertEqual(word_element.text, "Hello, What Do You Want To Learn?")
            print("Assert equal passed.")
        except AssertionError as e:
            print(f"Assert equal failed: {e}")


    def assert_true_testing(self):
        try:
            page_title = self.driver.title
            word_element = self.driver.find_element(By.XPATH, "//*[@id='comp']/div[2]/div[1]/div[1]")
            # Assert true
            self.assertTrue("GeeksforGeeks" in page_title, f"Page title does not contain 'GeeksforGeeks': {page_title}")
            print("Assert true passed.")
        except AssertionError as e:
            print(f"Assert true failed: {e}")
    
    def assert_false_testing(self):
        try:
            page_title = self.driver.title
            word_element = self.driver.find_element(By.XPATH, "//*[@id='comp']/div[2]/div[1]/div[1]")
            # Assert false
            self.assertFalse("TutorialPoint" in page_title, f"Expected 'TutorialsPoint' not to be in title, but it was found in '{page_title}'")
            print("Assert false passed.")
        except AssertionError as e:
            print(f"Assert false failed: {e}")


    def assert_is_none_testing(self):
        try:
            page_title = self.driver.title
            word_element = self.driver.find_element(By.XPATH, "//*[@id='comp']/div[2]/div[1]/div[1]")
            word_element = None
            # Assert is none
            self.assertIsNone(word_element, f"Expected word_element to be None, but it was found: {word_element}")
            print("Assert is none passed.")
        except AssertionError as e:
            print(f"Assert is none failed: {e}")


    def assert_is_not_none_testing(self):
        try:
            page_title = self.driver.title
            word_element = self.driver.find_element(By.XPATH, "//*[@id='comp']/div[2]/div[1]/div[1]")
            # Assert is not none
            self.assertIsNotNone(word_element, f"Expected word_element to be not None, but it was found: {word_element}")
            print("Assert is not none passed.")
        except AssertionError as e:
            print(f"Assert is not none failed: {e}")







