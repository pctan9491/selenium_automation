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

class AddingDeletingCookies(SeleniumTemplate, unittest.TestCase):
    def __init__(self, methodName='runTest'):
        SeleniumTemplate.__init__(self, timeout=30) 
        unittest.TestCase.__init__(self, methodName)
        self.base_url = "https://www.geeksforgeeks.org/"

    def test_adding_deleting_cookies(self):
        try:
            # Setup the driver first
            self.setup_driver(headless=False)
            
            # Navigate to URL
            print(f"\nNavigating to: {self.base_url}")
            self.driver.get(self.base_url)
            print("Page loaded successfully.")

             # Updated method call
            self.set_cookies()

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Comment out automatic browser closing to allow manual closing
            if hasattr(self, 'driver') and self.driver:
                self.driver.quit()
                print("Browser closed.")
    
    def set_cookies(self):
        try:
            #Add Cookies
            add_cookies = {'name':'cookie_name', 'value':'12345', 'domain': 'www.geeksforgeeks.org'}
            self.driver.add_cookie(add_cookies)
            print("Cookie added successfully.")

            #Get Cookies
            gett_cookies = self.driver.get_cookies()
            print("Cookies: ", gett_cookies)

            #Get cookies by name
            get_cookie_by_name = self.driver.get_cookie('cookie_name')
            print("Cookie by name: ", get_cookie_by_name)

            #Delete Cookies
            self.driver.delete_cookie('www.geeksforgeeks.org')
            print("Cookie deleted successfully.")

            #Get Cookies after deletion
            gett_cookies_after_deletion = self.driver.get_cookies()
            print("Cookies after deletion: ", gett_cookies_after_deletion)
        except Exception as e:
            print(f"Error: {e}")