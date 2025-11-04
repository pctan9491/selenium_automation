import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def clear_whatsapp_session():
    """
    This script launches a Chrome browser with the specified user data directory,
    navigates to WhatsApp Web, clears localStorage and sessionStorage to log out,
    and then closes the browser.
    """
    print("Initializing browser to clear WhatsApp session...")

    # --- Configuration ---
    # This MUST match the user_data_dir used in your selenium_utils/template.py
    user_data_dir = os.path.join(os.path.dirname(__file__), "chrome_data")
    whatsapp_url = "https://web.whatsapp.com/"

    # --- Setup Chrome Options ---
    options = webdriver.ChromeOptions()
    options.add_argument(f"user-data-dir={user_data_dir}")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--start-maximized")
    # options.add_argument("--headless")  # Optional: run in headless mode

    # --- Initialize Driver ---
    try:
        service = Service(ChromeDriverManager().install())
        driver = webdriver.Chrome(service=service, options=options)
        print("Browser started successfully.")
    except Exception as e:
        print(f"Error initializing browser: {e}")
        return

    try:
        # --- Navigate and Clear Session ---
        print(f"Navigating to {whatsapp_url}...")
        driver.get(whatsapp_url)
        
        # Wait a moment for the page to start loading its scripts
        time.sleep(5)

        print("Executing script to clear localStorage and sessionStorage...")
        driver.execute_script("window.localStorage.clear(); window.sessionStorage.clear();")
        print("Session data cleared.")

        # Refresh the page to apply the changes (will force a new QR code)
        print("Refreshing the page...")
        driver.refresh()
        
        # Wait to observe the result
        print("Waiting for 5 seconds to show the logged-out state...")
        time.sleep(5)

    except Exception as e:
        print(f"An error occurred during session clearing: {e}")
    finally:
        # --- Cleanup ---
        print("Closing the browser.")
        driver.quit()
        print("Process complete.")

if __name__ == "__main__":
    clear_whatsapp_session()