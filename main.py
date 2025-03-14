import os
import sys
# Add the project root directory to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from tests.geeks_to_geeks import GeeksToGeeksSearch
from tests.geeks_login import geeksLogin
from basic.writing_test import WritingTest

import time


def main():
    # Create instance of GeeksToGeeksSearch
    geeks_bot = None
    try:
        geeks_bot = GeeksToGeeksSearch() 
        
        # Setup the driver
        geeks_bot.setup_driver(headless=False)
        
        # Perform the search
        success = geeks_bot.perform_search("Data Structure")
        
        if success:
            print("Search completed successfully!")
            # Add delay before cleanup
            time.sleep(3)
            
    except Exception as e:
        print(f"An error occurred: {e}")
        
    finally:
        # Always cleanup if bot was created
        if geeks_bot:
            geeks_bot.cleanup()


if __name__ == "__main__":
    writing_test = WritingTest()
    writing_test.assert_write_test()
