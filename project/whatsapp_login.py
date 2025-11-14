from argparse import Action
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
            self.find_inbox()

            #send message
            message_word = "Send message with current date:" + time.strftime("%Y-%m-%d %H:%M:%S")
            self.send_message(message_word)
            file_path = r"C:\Users\User\Documents\Example.docx"
            self.attach_file(file_path)
            time.sleep(3)

        except Exception as e:
            print(f"An unexpected error occurred: {e}")
        finally:
            # Comment out automatic browser closing to allow manual closing
            if hasattr(self, 'driver') and self.driver:
                self.driver.quit()
                print("Browser closed.")
    
    def login_first(self):
        try:
            # Wait up to 10 seconds for the main chat pane to appear
            print("Checking for existing WhatsApp login session...")
            self.set_explicit_wait(EC.presence_of_element_located, (By.XPATH, '//*[@id="side"]/div[1]/div/div[2]/div/div/div[1]/p'), timeout=10)
            print("✅ Already logged in to WhatsApp.")
            # Now you can proceed with your tests for a logged-in user
            time.sleep(5)
            
        except TimeoutException:
            print("No active session found. Please scan the QR code.")
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
            total_seconds = 50
            for remaining in range(total_seconds, 0, -1):
                update_countdown_js = f"""
                document.getElementById('qr-countdown').innerHTML = 
                    'Scan QR Code<br>Time remaining: {remaining}s';
                """
                self.driver.execute_script(update_countdown_js)
                time.sleep(1)
            
            # Remove countdown element
            self.driver.execute_script("document.getElementById('qr-countdown').remove();")

    def send_message(self, message):
        print("Send message")
        
    def find_inbox(self):
        self.login_first()
        timeout = 30
        inbox_path ='//*[@id="pane-side"]/div[1]/div/div/div[2]/div/div/div/div[2]'
        search_content ='0199130949'
        search_box_path = '//*[@id="side"]/div[1]/div/div[2]/div/div/div[1]/p'

        try:
            search_box = WebDriverWait(self.driver, 5).until(
                EC.presence_of_element_located((By.XPATH, search_box_path))
            )
            search_box.clear()
            search_box.send_keys(search_content)
            time.sleep(2)

        except TimeoutException:
            print("Search box not found.")
            return None
        
        start_time = time.time()
        while time.time() - start_time < timeout:
            try:
                inbox_element = WebDriverWait(self.driver, 5).until(
                    EC.presence_of_element_located((By.XPATH, inbox_path))
                )
                print("Inbox element found")
                inbox_element.click()
                time.sleep(5)
                return inbox_element
            except TimeoutException:
                print("Inbox element not found yet. Retrying...")
                self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
            
            raise TimeoutException(f"Inbox element not found after {timeout} scrolling")

    def send_message(self, message):
        print("Send message")
        message_box_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[3]/div[1]/p'
        message_box = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, message_box_path))
        )
        message_box.click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).send_keys(Keys.BACKSPACE).perform()
        time.sleep(3)
        message_box.send_keys(message)
        time.sleep(3)
        #message_box.send_keys(Keys.ENTER)
        print("message sent")
    
    def attach_file(self, file_path):
        print("Attach file")
        self.plus_button_action()
        self.attachment_button_action()
        print("Attach filed completed")

    

    def plus_button_action(self):
        whatsapp_plus_button_path = '//*[@id="main"]/footer/div[1]/div/span/div/div[2]/div/div[1]/button/span'
        whatsapp_plus_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, whatsapp_plus_button_path))
        )
        whatsapp_plus_button.click()
        print("Whatsapp plus button clicked")
        time.sleep(2)

    
    def attachment_button_action(self):
        whatsapp_attachment_button_path = '//*[@id="app"]/div[1]/div/span[6]/div/ul/div/div/div[1]/li/div/span'
        whatsapp_attachment_button = WebDriverWait(self.driver, 5).until(
            EC.presence_of_element_located((By.XPATH, whatsapp_attachment_button_path))
        )
        whatsapp_attachment_button.click()
        print("Whatsapp attachment button clicked")
        time.sleep(2)





