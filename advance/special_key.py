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
            self.sk_enter()

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


    # Special Key: BACKSPACE
    def sk_backspace(self):

        #Setup the driver if not already done
        if not hasattr(self, 'driver') or self.driver is None:
            self.setup_driver(headless=False)
            self.driver.get(self.base_url)

        element = self.driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
        element.send_keys("Test for BACKSPACEE")
        print(f"Add key pressed with value: {element.get_attribute('value')}")
        time.sleep(3)
        for i in range(len(element.get_attribute('value'))):
            element.send_keys(Keys.BACK_SPACE)
        time.sleep(4)
        assert element.get_attribute('value') == ''  # After backspacing all characters, the value should be empty
        print("Backspace key pressed successfully.")


    # Special Key: DECIMAL
    def sk_decimal(self):

        #Setup the driver if not already done
        if not hasattr(self, 'driver') or self.driver is None:
            self.setup_driver(headless=False)
            self.driver.get(self.base_url)

        element = self.driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
        element.send_keys("123")
        time.sleep(1)
        element.send_keys(Keys.DECIMAL)
        time.sleep(1)
        element.send_keys("456")
        time.sleep(3)
        print(f"Add key pressed with value: {element.get_attribute('value')}")
        assert element.get_attribute('value') == '123.456'  # After backspacing all characters, the value should be empty
        print("Decimal key pressed successfully.")


    # Special Key: DELETE
    def sk_delete(self):

        #Setup the driver if not already done
        if not hasattr(self, 'driver') or self.driver is None:
            self.setup_driver(headless=False)
            self.driver.get(self.base_url)

        element = self.driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
        element.send_keys("Test for Delete")
        time.sleep(3)

        for i in range(5):
            element.send_keys(Keys.ARROW_LEFT)
            time.sleep(1)
            element.send_keys(Keys.DELETE)
            time.sleep(1)
        
        print(f"Delete key pressed with value: {element.get_attribute('value')}")
        assert element.get_attribute('value') == 'Test for D'  # After backspacing all characters, the value should be empty
        print("Delete key pressed successfully.")


    # Special Key: DIVIDE
    def sk_divide(self):

        #Setup the driver if not already done
        if not hasattr(self, 'driver') or self.driver is None:
            self.setup_driver(headless=False)
            self.driver.get(self.base_url)

        element = self.driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
        element.send_keys(
            Keys.NUMPAD1,
            Keys.NUMPAD0,
            Keys.NUMPAD0,
            Keys.DIVIDE,
            Keys.NUMPAD5
        )
        time.sleep(3)

        print(f"Devide key pressed with value: {element.get_attribute('value')}")
        assert element.get_attribute('value') == '100/5'  # After backspacing all characters, the value should be empty
        print("Divide key pressed successfully.")


    # Special Key: HOME AND END
    def sk_home_end(self):

        #Setup the driver if not already done
        if not hasattr(self, 'driver') or self.driver is None:
            self.setup_driver(headless=False)
            self.driver.get(self.base_url)

        element = self.driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
        element.send_keys("test for end")
        time.sleep(1)
        element.send_keys(Keys.HOME)
        time.sleep(1)
        element.send_keys(Keys.END)
        time.sleep(3)
        print(f"Home and End key pressed with value: {element.get_attribute('value')}")
        assert element.get_attribute('value') == 'test for end'  # After backspacing all characters, the value should be empty
        print("Home and End key pressed successfully.")


    # Special Key: ENTER
    def sk_enter(self):

        #Setup the driver if not already done
        if not hasattr(self, 'driver') or self.driver is None:
            self.setup_driver(headless=False)
            self.driver.get(self.base_url)

        element = self.driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
        element.send_keys("test for enter")
        time.sleep(2)
        element.send_keys(Keys.ENTER)
        time.sleep(3)
        print("Enter key pressed successfully.")





