# test_datameld.py
"""
Tests for DataMeld module.
"""

import unittest
from datameld import DataMeld

class TestDataMeld(unittest.TestCase):
    """Test cases for DataMeld class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = DataMeld()
        self.assertIsInstance(instance, DataMeld)
        
    def test_run_method(self):
        """Test the run method."""
        instance = DataMeld()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
