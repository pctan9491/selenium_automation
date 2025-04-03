import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium_utils.template import SeleniumTemplate

class AssertLearn(SeleniumTemplate, unittest.TestCase):
    def __init__(self, methodName='runTest'):  # Change this line
        SeleniumTemplate.__init__(self, timeout=30)
        unittest.TestCase.__init__(self, methodName)  # Add methodName here
        self.base_url = "https://www.geeksforgeeks.org/"

    def test_assert_learn(self):
        # --- Setup WebDriver ---
        try:
            print("Setting up Chrome WebDriver...")
            service = Service(ChromeDriverManager().install())
            options = webdriver.ChromeOptions()
            options.add_argument("--start-maximized")
            options.add_argument("--disable-notifications")
            driver = webdriver.Chrome(service=service, options=options)
            wait = WebDriverWait(driver, 10)
            print("WebDriver setup successful.")
            
            # Use self.base_url instead of hardcoded URL
            url = self.base_url
            
        except Exception as e:
            print(f"Error setting up WebDriver: {e}")
            exit()

        # --- Navigation ---
        try:
            print(f"\nNavigating to: {url}")
            driver.get(url)
            print("Page loaded successfully.")
        except Exception as e:
            print(f"Error navigating to {url}: {e}")
            driver.quit()
            exit()

        # --- Assertions ---
        print("\n--- Starting Assertions ---")

        # 1. Assert Page Title
        print("\n1. Asserting Page Title")
        expected_title = "GeeksforGeeks | A computer science portal for geeks"
        try:
            actual_title = driver.title
            assert actual_title == expected_title
            print(f"   ✅ PASS: Page title is exactly as expected: '{actual_title}'")

            # Example: Assert title contains specific text (less strict)
            assert "GeeksforGeeks" in actual_title
            print(f"   ✅ PASS: Page title contains 'GeeksforGeeks'.")

        except AssertionError:
            actual_title = driver.title # Get title again in case it changed or failed initially
            print(f"   ❌ FAIL: Page title assertion failed!")
            print(f"      Expected: '{expected_title}'")
            print(f"      Actual:   '{actual_title}'")
        except Exception as e:
            print(f"   ❌ FAIL: An unexpected error occurred while checking title: {e}")

        # 2. Assert Current URL
        print("\n2. Asserting Current URL")
        expected_url_part = "geeksforgeeks.org"
        try:
            actual_url = driver.current_url
            assert expected_url_part in actual_url
            print(f"   ✅ PASS: Current URL '{actual_url}' contains '{expected_url_part}'.")
        except AssertionError:
            actual_url = driver.current_url
            print(f"   ❌ FAIL: URL assertion failed!")
            print(f"      Expected URL to contain: '{expected_url_part}'")
            print(f"      Actual URL:            '{actual_url}'")
        except Exception as e:
            print(f"   ❌ FAIL: An unexpected error occurred while checking URL: {e}")


            # 3. Assert Element Presence (e.g., the main logo)
            print("\n3. Asserting Element Presence (GeeksforGeeks Logo)")
            logo_locator = (By.XPATH, "//a[@aria-label='GeeksforGeeks']") # More specific locator
            # Example of a locator that might fail:
            # logo_locator = (By.ID, "non_existent_logo")
        try:
            # Wait until the element is present in the DOM
            logo_element = wait.until(EC.presence_of_element_located(logo_locator))
            assert logo_element is not None # Check if find_element returned something
            print(f"   ✅ PASS: Logo element is present on the page (found by {logo_locator}).")
        except TimeoutException:
            print(f"   ❌ FAIL: Logo element was not found within the wait time (locator: {logo_locator}).")
        except AssertionError:
            print(f"   ❌ FAIL: Logo presence assertion failed (element found was None unexpectedly).")
        except Exception as e:
            print(f"   ❌ FAIL: An unexpected error occurred while checking logo presence: {e}")


            # 4. Assert Element is Visible (e.g., the search bar)
            print("\n4. Asserting Element Visibility (Search Bar)")
            search_bar_locator = (By.NAME, "search")
        try:
            # Wait until the element is not only present but also visible
            search_bar = wait.until(EC.visibility_of_element_located(search_bar_locator))
            assert search_bar.is_displayed() # Verify it's actually displayed
            print(f"   ✅ PASS: Search bar element is visible on the page.")
        except TimeoutException:
            print(f"   ❌ FAIL: Search bar element was not visible within the wait time (locator: {search_bar_locator}).")
        except AssertionError:
            print(f"   ❌ FAIL: Search bar visibility assertion failed (is_displayed() returned False).")
        except Exception as e:
            print(f"   ❌ FAIL: An unexpected error occurred while checking search bar visibility: {e}")


            # 5. Assert Element Text (e.g., a navigation link like "Courses")
            print("\n5. Asserting Element Text ('Courses' link)")
            courses_link_locator = (By.LINK_TEXT, "Courses")
            expected_text = "Courses"
            try:
                courses_link = wait.until(EC.element_to_be_clickable(courses_link_locator))
                actual_text = courses_link.text.strip()
                assert actual_text == expected_text
                print(f"   ✅ PASS: Found element with the exact text '{expected_text}'.")

                # Example: Assert text contains (less strict)
                assert "Course" in actual_text
                print(f"   ✅ PASS: Link text '{actual_text}' contains 'Course'.")

            except TimeoutException:
                print(f"   ❌ FAIL: 'Courses' link element not clickable within the wait time (locator: {courses_link_locator}).")
            except AssertionError:
                actual_text = "Element not found or text mismatch"
                try:
                    element = driver.find_element(*courses_link_locator)
                    actual_text = element.text.strip()
                except NoSuchElementException:
                    actual_text = "Element not found"
                except Exception:
                    actual_text = "Error getting text"
                print(f"   ❌ FAIL: Text assertion failed for 'Courses' link!")
                print(f"      Expected: '{expected_text}'")
                print(f"      Actual:   '{actual_text}'")
            except Exception as e:
                print(f"   ❌ FAIL: An unexpected error occurred while checking 'Courses' link text: {e}")


            # 6. Assert Attribute Value (e.g., Search bar placeholder)
            print("\n6. Asserting Attribute Value (Search bar placeholder)")
            search_bar_locator = (By.NAME, "search")
            expected_placeholder = "Search..."
            try:
                search_bar = wait.until(EC.presence_of_element_located(search_bar_locator))
                actual_placeholder = search_bar.get_attribute("placeholder")
                assert actual_placeholder == expected_placeholder
                print(f"   ✅ PASS: Search bar placeholder attribute is correct: '{actual_placeholder}'.")
            except TimeoutException:
                print(f"   ❌ FAIL: Search bar element not present within the wait time (locator: {search_bar_locator}).")
            except AssertionError:
                actual_placeholder = "Attribute not found or mismatch"
                try:
                    element = driver.find_element(*search_bar_locator)
                    actual_placeholder = element.get_attribute("placeholder")
                except NoSuchElementException:
                    actual_placeholder = "Element not found"
                except Exception:
                    actual_placeholder = "Error getting attribute"
                print(f"   ❌ FAIL: Search bar placeholder assertion failed!")
                print(f"      Expected: '{expected_placeholder}'")
                print(f"      Actual:   '{actual_placeholder}'")
            except Exception as e:
                print(f"   ❌ FAIL: An unexpected error occurred while checking search bar placeholder: {e}")


            # 7. Asserting a Boolean Condition (e.g., Search bar is enabled)
            print("\n7. Asserting Boolean Condition (Search bar is enabled)")
            search_bar_locator = (By.NAME, "search")
        try:
            search_bar = wait.until(EC.visibility_of_element_located(search_bar_locator)) # Ensure visible first
            assert search_bar.is_enabled() is True # Explicitly check for True
            print(f"   ✅ PASS: Search bar is enabled.")
        except TimeoutException:
            print(f"   ❌ FAIL: Search bar element not visible within the wait time (locator: {search_bar_locator}).")
        except AssertionError:
            print(f"   ❌ FAIL: Search bar enabled assertion failed (is_enabled() returned False or element state issues).")
        except Exception as e:
            print(f"   ❌ FAIL: An unexpected error occurred while checking if search bar is enabled: {e}")


            # --- Cleanup ---
            print("\n--- Assertions Complete ---")
            time.sleep(2) # Pause briefly to see the final state (optional)
            driver.quit()
            print("Browser closed.")