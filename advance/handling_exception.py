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
            self.invalid_coordinates_exception()

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
    
    #test exception: ImeActivationFailedException
    def ime_activation_failed_exception(self):
        """Test ImeActivationFailedException - occurs when IME (Input Method Editor) activation fails"""
        try:
            # Find an input field that might require IME activation
            search_box = self.driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
            
            # Try to activate IME for non-Latin text input (this might trigger the exception)
            # Note: This exception is rare and typically occurs on systems with IME support
            search_box.click()
            search_box.clear()
            
            # Attempt to send keys that might require IME activation
            # This could potentially trigger ImeActivationFailedException on some systems
            search_box.send_keys("こんにちは")  # Japanese text that might require IME
            
            print("Successfully sent IME text to the element.")
            
        except ImeActivationFailedException as e:
            print(f"ImeActivationFailedException: Failed to activate IME - {e}")
            print("This typically occurs when:")
            print("- IME is not properly installed or configured")
            print("- System doesn't support the required input method")
            print("- WebDriver cannot communicate with the IME system")
            
        except Exception as e:
            print(f"Other exception occurred: {type(e).__name__}: {e}")
            
        finally:
            print("Finished testing IME activation.")
        
        time.sleep(3)
    
    #test exception:ImeNotAvailableException
    def ime_not_available_exception(self):
        """Test ImeNotAvailableException - occurs when IME (Input Method Editor) is not available"""
        try:
            # Find an input field that might require IME activation
            search_box = self.driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
            
            # Try to activate IME for non-Latin text input (this might trigger the exception)
            # Note: This exception is rare and typically occurs on systems with IME support
            search_box.click()
            search_box.clear()
            
            # Attempt to send keys that might require IME activation
            # This could potentially trigger ImeActivationFailedException on some systems
            search_box.send_keys("こんにちは")  # Japanese text that might require IME
            
            print("Successfully sent IME text to the element.")
            
        except ImeNotAvailableException as e:
            print(f"ImeNotAvailableException: Failed to activate IME - {e}")
            print("This typically occurs when:")
            print("- IME is not properly installed or configured")
            print("- System doesn't support the required input method")
            print("- WebDriver cannot communicate with the IME system")
            
        except Exception as e:
            print(f"Other exception occurred: {type(e).__name__}: {e}")
            
        finally:
            print("Finished testing IME not available.")
        
        time.sleep(3)
    
    #test exception: InsecureCertificateException
    #test exception: InsecureCertificateException (Simulated)
    def insecure_certificate_exception(self):
        """Test InsecureCertificateException - simulate the exception for demonstration"""
        try:
            # Try to access a site with SSL issues
            test_url = "https://self-signed.badssl.com/"
            print(f"Attempting to access: {test_url}")
            
            # Check if the site loads (modern browsers often allow it)
            self.driver.get(test_url)
            
            # Check if we're on an SSL warning page
            page_source = self.driver.page_source.lower()
            if any(warning in page_source for warning in ["not secure", "certificate", "ssl", "security"]):
                print("SSL warning detected - simulating InsecureCertificateException")
                # Manually raise the exception for demonstration
                raise InsecureCertificateException("SSL certificate validation failed - certificate is self-signed")
            
            print("Site loaded without SSL issues (or browser ignored them)")
            
        except InsecureCertificateException as e:
            print(f"InsecureCertificateException: {e}")
            print("This exception occurs when:")
            print("- SSL certificate is self-signed or invalid")
            print("- Certificate has expired")
            print("- Certificate hostname doesn't match")
            print("- Certificate chain is broken")
            print("- WebDriver is configured to reject invalid certificates")
            
        except Exception as e:
            print(f"Other exception: {type(e).__name__}: {e}")
            
        finally:
            print("Finished testing insecure certificate.")
        
        time.sleep(3)

    
    #test exception: InvalidArgumentException
    def invalid_argument_exception(self):
        #true element: //*[@id="comp"]/div[2]/div[1]/div[2]/input (search box in geeks to geeks)
        
        try:
            element = self.driver.find_element('By.XPATH', '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
            # Intentionally wrong XPath
            element.send_keys("Hello, World!")
            print("Successfully sent keys to the element.")
        except InvalidArgumentException:
            print("InvalidArgumentException: Invalid argument.")
        finally:
            print("Finished testing.")
        
        time.sleep(3)


   #test exception: InvalidCookieDomainException
    def invalid_cookie_domain_exception(self):
        #true element: //*[@id="comp"]/div[2]/div[1]/div[2]/input (search box in geeks to geeks)
        
        try:
            #Define a cookie for a COMPLETELY DIFFERENT domain
            print("Attempting to add a cookie for the domain 'google.com'...")
            invalid_cookies = {
                'name': 'testing',
                'value': '12345',
                'domain': '.google.com'
            }
            self.driver.add_cookie(invalid_cookies)
        except InvalidCookieDomainException:
            print("InvalidCookiesDomainException: Invalid cookies domain.")
        finally:
            print("Finished testing.")
        
        time.sleep(3)


    #test exception: InvalidCoordinatesException
    def invalid_coordinates_exception(self):
        #true element: //*[@id="comp"]/div[2]/div[1]/div[2]/input (search box in geeks to geeks)
        
        try:
            self.driver.set_window_size(800,600)
            #element = self.driver.find_element('By.XPATH', '//*[@id="comp"]/div[2]/div[1]/div[2]/input')

            print("Attempting to move to the element that is out of view...")
            action = ActionChains(self.driver)

            action.move_by_offset(10000, 10000).perform()
        except InvalidCoordinatesException:
            print("InvalidCoordinatesException: Invalid coordinates.")
        finally:
            print("Finished testing.")
        
        time.sleep(3)


    #test exception: InvalidElementStateException
    def invalid_element_state_exception(self):
        #true element: //*[@id="comp"]/div[2]/div[1]/div[2]/input (search box in geeks to geeks)
        
        try:
            element = self.driver.find_element(By.XPATH, '//*[@id="topMainHeader"]/div/a/div/img')
            print("Attempting to type into the disable input field...")
            element.send_keys("Hello, World!")

        except InvalidElementStateException:
            print("InvalidElementStateException: Element is not enabled.")
        finally:
            print("Finished testing.")
        
        time.sleep(3)


    #test exception: InvalidSelectorException
    def invalid_selector_exception(self):
        #true element: //*[@id="comp"]/div[2]/div[1]/div[2]/input (search box in geeks to geeks)
        
        try:
            print("Attempting to find element with invalid xpath")
            element = self.driver.find_element(By.XPATH, '#comp > div.index_homePageContainer__H8GJD > div.HomePageSearchContainer_homePageSearchContainer__bNc8c > div.HomePageSearchContainer_homePageSearchContainer_container__vWZMD > input')
            element.send_keys("Hello, World!")

        except InvalidSelectorException:
            print("InvalidSelectorException: Element is not enabled.")
        finally:
            print("Finished testing.")
        
        time.sleep(3)


    # cannot perform seems
    #test exception: InvalidSessionIdException
    def invalid_session_id_exception(self):
        #true element: //*[@id="comp"]/div[2]/div[1]/div[2]/input (search box in geeks to geeks)
        
        try:
            print(f"Initial page title: {self.driver.title}")
            element = self.driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
            print("Quitting the driver session...")
            session_id = self.driver.session_id
            self.driver.quit()
            
            from selenium.webdriver.remote.webdriver import WebDriver
            temp_driver = WebDriver(command_executor=self.driver.command_executor, desired_capabilities={})
            temp_driver.session_id = session_id
            final_title = temp_driver.title

        except InvalidSessionIdException:
            print("InvalidSessionIdException: Session ID is invalid.")
        except Exception as e:
            print(f"Other exception: {type(e).__name__}: {e}")
        finally:
            print("Finished testing.")
        
        time.sleep(3)


     #test exception: InvalidSwitchToTargetException  
   
    def invalid_switch_to_target_exception(self):
        # Try to switch to a non-existent frame by name
        self.driver.switch_to.frame("non_existent_frame")
        print("Successfully switched to frame (this shouldn't happen)")
        
        try:
            self.driver.switch_to.frame("non_existent_frame")
            print("Successfully switched to frame (this shouldn't happen)")
        except InvalidSwitchToTargetException:
            print("InvalidSwitchToTargetException: Switch to target element is invalid.")
        except Exception as e:
            print(f"Other exception: {type(e).__name__}: {e}")
        finally:
            print("Finished testing.")
        # Make sure to switch back to default content
        try:
            self.driver.switch_to.default_content()
        except:
            pass


    #test exception: NoAlertPresentException
    def no_alert_present_exception(self):
        #true element: //*[@id="comp"]/div[2]/div[1]/div[2]/input (search box in geeks to geeks)
        
        try:
            self.driver.switch_to.alert
            print(f"Alert text: {alert.text}")
            alert.accept()
            print("Alert handled successfully (this shouldn't happen)")

        except NoAlertPresentException:
            print("NoAlertPresentException: No alert is present.")
        except Exception as e:
            print(f"Other exception: {type(e).__name__}: {e}")
        finally:
            print("Finished testing.")
        
        time.sleep(3)


    #test exception:NoSuchCookieException
    def no_such_cookie_exception(self):
        #true element: //*[@id="comp"]/div[2]/div[1]/div[2]/input (search box in geeks to geeks)
        
        try:
            print("Attempting to delete a cookie that does not exist...")
            cookie_name = "session_id"
            cookie = self.driver.get_cookie(cookie_name)

            if cookie is None:
                raise NoSuchCookieException(f"Cookie '{cookie_name}' not found")

            self.driver.delete_cookie(cookie_name)
            print("Cookie deleted successfully")

        except NoSuchCookieException as e:
            print("NoSuchCookieException: Cookie is not found.")
        except Exception as e:
            print(f"Other exception: {type(e).__name__}: {e}")
        finally:
            print("Finished testing.")
        
        time.sleep(3)


    #test exception:StaleElementReferenceException
    def stale_element_reference_exception(self):
        #true element: //*[@id="comp"]/div[2]/div[1]/div[2]/input (search box in geeks to geeks)
        
        try:
            element = self.driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[3]/a[1]')
            print(f"Initially found item with text: {element.text}")
            
            print("List has been refreshed")
            self.driver.refresh()

            print("Attempting to click the element using old reference...")
            element.click()

        except StaleElementReferenceException:
            print("StaleElementReferenceException: Element is not found.")
        except Exception as e:
            print(f"Other exception: {type(e).__name__}: {e}")
        finally:
            print("Finished testing.")
        
        time.sleep(3)


  #test exception: TimeoutException
    def timeout_exception(self):
        #true element: //*[@id="comp"]/div[2]/div[1]/div[2]/input (search box in geeks to geeks)
        wait = WebDriverWait(self.driver, 0.01)

        try:
            element = self.driver.find_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[3]/a[2]')
            element.click()
            print("Waiting for the result container to appear...")
            results = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="__next"]/div/div[4]/div[1]/section[1]/div[2]/div/div[2]/div[3]/div[2]')))

        except TimeoutException as e:
            print("TimeoutException: Element is not found.")
        except Exception as e:
            print(f"Other exception: {type(e).__name__}: {e}")
        finally:
            print("Finished testing.")
        
        time.sleep(3)


#test exception: UnableToSetCookieException
    def unable_to_set_cookie_exception(self):
        #true element: //*[@id="comp"]/div[2]/div[1]/div[2]/input (search box in geeks to geeks)

        try:
            print("Set cookie...")
            cookie = {
            "name": "test", 
            "value": "123",
            "domain": "invalid-domain.com"  # Different domain than current page
        }
            self.driver.add_cookie(cookie)
            print("Cookie set successfully (this shouldn't happen)")

        except UnableToSetCookieException as e:
            print("UnableToSetCookieException: Cookie is not set.")
        except Exception as e:
            print(f"Other exception: {type(e).__name__}: {e}")
        finally:
            print("Finished testing.")
        
        time.sleep(3)

