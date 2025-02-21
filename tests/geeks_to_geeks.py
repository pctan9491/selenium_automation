import os
import sys
# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium_utils.template import SeleniumTemplate
import time

class GeeksToGeeksSearch(SeleniumTemplate):
    def __init__(self, timeout=30):
        super().__init__(timeout)
        self.base_url = "https://www.geeksforgeeks.org/"
    
    def perform_search(self, search_term):
        """Perform a search on GeeksForGeeks"""
        try:
            # Navigate to GeeksForGeeks
            self.navigate_to(self.base_url)
            
            # Add a small delay to ensure page is loaded
            time.sleep(2)
            
            # Find and fill the top search box
            enter_text = self.wait_for_element(By.XPATH, '//*[@id="comp"]/div[2]/div[1]/div[2]/input')
            self.fill_form(enter_text, search_term)
            enter_text.send_keys(Keys.RETURN)
            
            # Add delay to ensure search results load
            time.sleep(2)
            
            # Wait for search results
            self.wait_for_element(By.ID, "search")
            
            # Add delay before returning
            time.sleep(1)
            return True
            
        except Exception as e:
            print(f"Search failed: {e}")
            return False
            

class GeeksToGeeksLogin(SeleniumTemplate):
    def __init__(self, timeout=30):
        super().__init__(timeout)
        self.base_url = "https://www.geeksforgeeks.org/"
        # Define available accounts
        self.accounts = {
            "Account 1": {"email": "pctan9491@gmail.com", "password": "Pctan494499@"},
            "Account 2": {"email": "another@email.com", "password": "anotherpassword"},
            # Add more accounts as needed
        }

    def select_account(self):
        """Open a simple GUI to select an account"""
        import tkinter as tk
        from tkinter import ttk

        result = {"selected": None}

        def on_select():
            result["selected"] = combo.get()
            root.quit()

        # Create the main window
        root = tk.Tk()
        root.title("Select Account")
        root.geometry("300x150")

        # Create and pack a label
        label = ttk.Label(root, text="Select an account to login:")
        label.pack(pady=20)

        # Create and pack the combobox
        combo = ttk.Combobox(root, values=list(self.accounts.keys()))
        combo.set("Select an account")  # Set default text
        combo.pack(pady=10)

        # Create and pack the button
        button = ttk.Button(root, text="Login", command=on_select)
        button.pack(pady=10)

        # Center the window
        root.eval('tk::PlaceWindow . center')

        root.mainloop()
        root.destroy()

        return result["selected"]

    def login(self):
        try:
            # Get selected account
            selected = self.select_account()
            if not selected or selected not in self.accounts:
                print("No account selected or invalid selection")
                return False

            credentials = self.accounts[selected]
            
            # Navigate to GeeksForGeeks
            self.navigate_to(self.base_url)

            # Add a small delay to ensure page is loaded
            time.sleep(2)

            # Find and click the login button
            login_button = self.wait_for_element(By.XPATH, '//*[@id="topMainHeader"]/div/div/button')
            login_button.click()

            # Add delay to ensure login page is loaded
            time.sleep(2)

            # Find and fill the login form
            email_input = self.wait_for_element(By.XPATH, '//*[@id="login"]/div/div[2]/div/div[3]/div[1]/input')
            self.fill_form(email_input, credentials["email"])

            # Find and fill the password input
            password_input = self.wait_for_element(By.XPATH, '//*[@id="login"]/div/div[2]/div/div[3]/div[2]/input')
            self.fill_form(password_input, credentials["password"])

            time.sleep(2)
            # Find and click the login button
            login_button = self.wait_for_element(By.XPATH, '//*[@id="login"]/div/div[2]/div/div[3]/button/span')
            login_button.click()

            # Check if reCAPTCHA is present before handling it
            if self.element_exists(By.CSS_SELECTOR, 'iframe[title="reCAPTCHA"]'):
                try:
                    # Wait for iframe to be present
                    time.sleep(2)
                    iframe = self.wait_for_element(By.CSS_SELECTOR, 'iframe[title="reCAPTCHA"]')
                    
                    # Switch to the reCAPTCHA iframe
                    self.driver.switch_to.frame(iframe)
                    
                    # Wait and click the checkbox
                    checkbox = self.wait_for_element(By.CSS_SELECTOR, '.recaptcha-checkbox-border')
                    self.safe_click(checkbox)
                    
                    # Switch back to default content
                    self.driver.switch_to.default_content()
                    
                    # Wait for verification and challenge to complete
                    time.sleep(10)  # Increased wait time for challenge completion

                                # Wait for reCAPTCHA challenge to be gone before clicking signup
                    time.sleep(5)

                    # Find and click the login button
                    login_button = self.wait_for_element(By.XPATH, '//*[@id="login"]/div/div[2]/div/div[3]/button/span')
                    login_button.click()
                    
                except Exception as e:
                    print(f"reCAPTCHA handling failed: {e}")
                    self.driver.switch_to.default_content()
            else:
                print("No reCAPTCHA detected, continuing with login...")

            # Add delay to wait for potential error message
            time.sleep(2)

            # Check for error message
            try:
                # Try to find error message element
                if self.element_exists(By.XPATH, '//*[@id="login"]/div/div[2]/div/div[3]/div[1]/div'):
                    error_text = self.get_text(By.XPATH, '//*[@id="login"]/div/div[2]/div/div[3]/div[1]/div')
                    if error_text and "Incorrect login credentials" in error_text:
                        print("Detected incorrect credentials, attempting signup...")
                        return self.signup()
                    elif error_text:
                        print(f"Login Error: {error_text}")
                        return False
                
                # No error found means successful login
                print("No error message found, login successful")
                return True
                
            except Exception as e:
                print(f"Error checking failed: {e}")
                # If we can't check for errors, assume login was successful
                return True

            # Add delay to ensure login is successful
            time.sleep(2)

            return True
        except Exception as e:
            print(f"Login failed: {e}")
            return False

    def signup(self):
        """Sign up for a new GeeksForGeeks account"""
        try:         
            # Find and click the login button to open the auth modal
            sign_up_page = self.wait_for_element(By.XPATH, '//*[@id="login"]/div/div[2]/div/div[2]')
            sign_up_page.click()
            
            # Add delay for modal to load
            time.sleep(2)
            
            # Fill in the registration form
            email_signup = self.wait_for_element(By.XPATH, '//*[@id="login"]/div/div[2]/div/div[3]/div[1]/input')
            self.fill_form(email_signup, "pctan9491@gmail.com")
            
            password_signup = self.wait_for_element(By.XPATH, '//*[@id="login"]/div/div[2]/div/div[3]/div[2]/input')
            self.fill_form(password_signup, "Pctan494499@")

            institution_signup = self.wait_for_element(By.XPATH, '//*[@id="login"]/div/div[2]/div/div[3]/div[3]/div/div/input')
            self.fill_form(institution_signup, "University")

            # Wait for and click the institution option
            institution_option = self.wait_for_clickable(By.XPATH, '//*[@id="login"]/div/div[2]/div/div[3]/div[3]/div/div[2]/div[1]')
            self.safe_click(institution_option)

            # Handle reCAPTCHA
            try:
                # Wait for iframe to be present
                time.sleep(2)
                iframe = self.wait_for_element(By.CSS_SELECTOR, 'iframe[title="reCAPTCHA"]')
                
                # Switch to the reCAPTCHA iframe
                self.driver.switch_to.frame(iframe)
                
                # Wait and click the checkbox
                checkbox = self.wait_for_element(By.CSS_SELECTOR, '.recaptcha-checkbox-border')
                self.safe_click(checkbox)
                
                # Switch back to default content
                self.driver.switch_to.default_content()
                
                # Wait for verification and challenge to complete
                time.sleep(10)  # Increased wait time for challenge completion
                
            except Exception as e:
                print(f"reCAPTCHA handling failed: {e}")
                self.driver.switch_to.default_content()
                pass

            # Wait for reCAPTCHA challenge to be gone before clicking signup
            time.sleep(5)
            
            # Use JavaScript to click the signup button to avoid interception
            signup_button = self.wait_for_element(By.XPATH, '//*[@id="login"]/div/div[2]/div/div[3]/button')
            self.driver.execute_script("arguments[0].click();", signup_button)
            
            # Add delay to wait for potential error message
            time.sleep(2)
            
            # Check for error message
            try:
                error_message = self.wait_for_element(By.XPATH, '//div[contains(@class, "error-message")]')
                if error_message:
                    print(f"Signup Error: {error_message.text}")
                    return False
            except:
                pass  # No error message found, signup might be successful
            
            # Add delay to ensure signup is complete
            time.sleep(2)
            
            return True
            
        except Exception as e:
            print(f"Signup failed: {e}")
            return False
