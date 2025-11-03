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
from selenium.webdriver.chrome.options import Options

class WhatsappLogin(SeleniumTemplate, unittest.TestCase):
    def __init__(self, methodName='runTest'):
        SeleniumTemplate.__init__(self, timeout=30) 
        unittest.TestCase.__init__(self, methodName)
        self.base_url = "https://web.whatsapp.com/"

    def test_whatsapp_login(self):
        try:
            # Setup the driver first
            self.setup_driver(headless=False)
            
            # Navigate to URL
            print(f"\nNavigating to: {self.base_url}")
            self.driver.get(self.base_url)
            print("Page loaded successfully.")

            # Updated method call
            self.login_first()

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Comment out automatic browser closing to allow manual closing
            if hasattr(self, 'driver') and self.driver:
                self.driver.quit()
                print("Browser closed.")
    
    def login_first(self):
        # Create and inject countdown element
        countdown_js = """
        // Create countdown element if it doesn't exist
        if (!document.getElementById('qr-countdown')) {
            const countdownDiv = document.createElement('div');
            countdownDiv.id = 'qr-countdown';
            countdownDiv.style.cssText = `
                position: fixed;
                top: 20px;
                right: 20px;
                background: #128C7E;
                color: white;
                padding: 15px 25px;
                border-radius: 8px;
                font-size: 18px;
                font-family: sans-serif;
                z-index: 9999;
                box-shadow: 0 2px 5px rgba(0,0,0,0.2);
            `;
            document.body.appendChild(countdownDiv);
        }
        """
        self.driver.execute_script(countdown_js)
        
        # Start 30 second countdown
        total_seconds = 30
        for remaining in range(total_seconds, 0, -1):
            update_countdown_js = f"""
            document.getElementById('qr-countdown').innerHTML = 
                'Scan QR Code<br>Time remaining: {remaining}s';
            """
            self.driver.execute_script(update_countdown_js)
            time.sleep(1)
        
        # Remove countdown element
        self.driver.execute_script("document.getElementById('qr-countdown').remove();")