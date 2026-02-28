# test_uidrift.py
"""
Tests for UiDrift module.
"""

import unittest
from uidrift import UiDrift

class TestUiDrift(unittest.TestCase):
    """Test cases for UiDrift class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = UiDrift()
        self.assertIsInstance(instance, UiDrift)
        
    def test_run_method(self):
        """Test the run method."""
        instance = UiDrift()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
