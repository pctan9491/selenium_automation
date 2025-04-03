import os
import sys
import unittest
# Add the project root directory to Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

from tests.geeks_to_geeks import GeeksToGeeksSearch
from tests.geeks_login import geeksLogin
from basic.writing_test import WritingTest
from basic.assert_learn import AssertLearn

if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(WritingTest)
    unittest.TextTestRunner(verbosity=2).run(suite)
