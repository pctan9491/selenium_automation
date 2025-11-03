import os
import sys
import unittest
import requests  # Add this import

# Add the project root directory to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from tests.geeks_to_geeks import GeeksToGeeksSearch
from tests.geeks_login import geeksLogin
from basic.writing_test import WritingTest
from basic.assert_learn import AssertLearn
from basic.wait import ExAndInWait
from basic.action_chain import ActionChainTest
from advance.handling_exception import HandlingException
from advance.special_key import SpecialKey
from advance.alert_prompt import AlertPrompt
from advance.adding_deleting_cookies import AddingDeletingCookies
from advance.assert_testing import AssertTesting
from advance.pom_reuse import PomTesting
from project.whatsapp_login import WhatsappLogin



def check_internet_connectivity(url="https://www.geeksforgeeks.org/", timeout=5):
    """
    Check if the specified URL is accessible.
    Returns True if accessible, False otherwise.
    """
    try:
        response = requests.get(url, timeout=timeout)
        return response.status_code == 200
    except (requests.RequestException, requests.ConnectionError, requests.Timeout):
        return False

if __name__ == "__main__":
    # Check connectivity first
    print("Checking internet connectivity...")
    if check_internet_connectivity():
        print("✅ Internet connection is working")
    else:
        print("❌ Internet connection issue detected")
        print("Please check your network connection and try again.")
        sys.exit(1)
    
    # Run tests
    suite = unittest.TestLoader().loadTestsFromTestCase(WhatsappLogin)

    unittest.TextTestRunner(verbosity=2).run(suite)