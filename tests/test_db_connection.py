"""Test the MongoDB database connection."""

import sys
import os
import unittest

# Add project root to path so imports work
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from db import test_connection


class TestDatabaseConnection(unittest.TestCase):
    """Test cases for MongoDB database connection."""

    def test_connection_successful(self):
        """Test that the database connection returns a connected status."""
        result = test_connection()
        self.assertIn("status", result)
        self.assertEqual(result["status"], "connected")
        self.assertIn("database", result)
        self.assertIsNotNone(result["database"])

    def test_connection_returns_dict(self):
        """Test that the connection result is a dictionary with expected keys."""
        result = test_connection()
        self.assertIsInstance(result, dict)
        self.assertIn("status", result)

    def test_connection_no_error_on_success(self):
        """Test that a successful connection has no error field."""
        result = test_connection()
        if result["status"] == "connected":
            self.assertNotIn("error", result)


if __name__ == "__main__":
    unittest.main()