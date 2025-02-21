import os
import sys
# Add the project root directory to Python path
project_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, project_root)

from tests.geeks_to_geeks import GeeksToGeeksLogin
import time

def geeksLogin():
    # Create instance of GeeksToGeeksSearch
    geeks_bot = None
    try:
        geeks_bot = GeeksToGeeksLogin() 
        
        # Setup the driver
        geeks_bot.setup_driver(headless=False)
        
        # Perform the search
        success = geeks_bot.login()

        if success:
            print("Login completed successfully!")
            time.sleep(3)  # Add delay before cleanup
            
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # Always cleanup if bot was created
        if geeks_bot:
            geeks_bot.cleanup()

if __name__ == "__main__":
    geeksLogin()
