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

class AlertPrompt(SeleniumTemplate, unittest.TestCase):
    def __init__(self, methodName='runTest'):
        SeleniumTemplate.__init__(self, timeout=30) 
        unittest.TestCase.__init__(self, methodName)
        self.base_url = "https://www.geeksforgeeks.org/"

    def test_alert_prompt(self):
        try:
            # Setup the driver first
            self.setup_driver(headless=False)
            
            # Navigate to URL
            print(f"\nNavigating to: {self.base_url}")
            self.driver.get(self.base_url)
            print("Page loaded successfully.")

             # Updated method call
            self.alert_dismiss()

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Comment out automatic browser closing to allow manual closing
            if hasattr(self, 'driver') and self.driver:
                self.driver.quit()
                print("Browser closed.")
    
    def alert_accept(self):
        try:
            print("Switching to alert...")
            self.driver.execute_script("alert('Test Alert');")
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            
            #Get the text from the alert and print it
            alert_text = alert.text
            print(f"Alert text: {alert_text}")
            time.sleep(3)

            #Accept the alert
            alert.accept()
            print("Alert accepted.")
            time.sleep(3)
        except NoAlertPresentException:
            print("No alert present.")
        except Exception as e:
            print(f"An error occurred while accepting the alert: {e}")


    def alert_dismiss(self):
        try:
            print("Switching to alert...")
            self.driver.execute_script("return window.confirm('Test dismiss alert');")
            WebDriverWait(self.driver, 10).until(EC.alert_is_present())
            alert = self.driver.switch_to.alert
            
            #Get the text from the alert and print it
            alert_text = alert.text
            print(f"Alert text: {alert_text}")
            time.sleep(3)

            #Accept the alert
            alert.dismiss()
            print("Alert dismissed.")
            time.sleep(3)
        except NoAlertPresentException:
            print("No alert present.")
        except Exception as e:
            print(f"An error occurred while accepting the alert: {e}")





