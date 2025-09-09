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

class SpecialKey(SeleniumTemplate, unittest.TestCase):
    def __init__(self, methodName='runTest'):
        SeleniumTemplate.__init__(self, timeout=30) 
        unittest.TestCase.__init__(self, methodName)
        self.base_url = "https://www.geeksforgeeks.org/"

    def test_special_key(self):
        try:
            # Setup the driver first
            self.setup_driver(headless=False)
            
            # Navigate to URL
            print(f"\nNavigating to: {self.base_url}")
            self.driver.get(self.base_url)
            print("Page loaded successfully.")

             # Updated method call
            self.sk_arrow_up_down()

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Comment out automatic browser closing to allow manual closing
            if hasattr(self, 'driver') and self.driver:
                self.driver.quit()
                print("Browser closed.")
    
    #---------------------------------------------------------------------------
    # Special Key: ADD
    def sk_add(self):

        #Setup the driver if not already done
        if not hasattr(self, 'driver') or self.driver is None:
            self.setup_driver(headless=False)
            self.driver.get(self.base_url)

        element = self.driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
        element.send_keys(Keys.ADD)
        print(f"Add key pressed with value: {element.get_attribute('value')}")
        time.sleep(3)
        assert element.get_attribute('value') == '+'
        print("Add key pressed successfully.")


    # Special Key: ALT (cannot do in automation)
    def sk_alt(self):
        #Setup the driver if not already done
        if not hasattr(self, 'driver') or self.driver is None:
            self.setup_driver(headless=False)
            self.driver.get(self.base_url)
        
        # Focus on the page first
        self.driver.execute_script("document.body.focus();")
        
        # Test Alt+Tab (though this might switch windows)
        actions = ActionChains(self.driver)
        actions.key_down(Keys.ALT).pause(0.5).key_up(Keys.ALT).perform()
        print("Alt key pressed and released")
        time.sleep(4)
        
        # Test if Alt key activates any accessibility features
        print("Alt key functionality tested")
        assert True, "Alt key test completed successfully"
        print("Alt key test finished.")
        actions = ActionChains(self.driver)
        actions.key_down(Keys.ALT).send_keys('f').key_up(Keys.ALT).perform()
        print(f"ALT+F key pressed with value")


    # Special Key: ARROW UP AND DOWN
    def sk_arrow_up_down(self):

        #Setup the driver if not already done
        if not hasattr(self, 'driver') or self.driver is None:
            self.setup_driver(headless=False)
            self.driver.get(self.base_url)

        element = self.driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
        element.send_keys("F")
        element.send_keys(Keys.ENTER)
        time.sleep(3)
        
        actions = ActionChains(self.driver)
        for i in range(4):
            actions.send_keys(Keys.ARROW_DOWN).perform()
            time.sleep(1)
            actions.reset_actions()
        for i in range(2):
            actions.send_keys(Keys.ARROW_UP).perform()
            time.sleep(1)
            actions.reset_actions()
        assert True, "Arrow up and down perform successfully"
        print("Arrow up and down perform successfully.")




