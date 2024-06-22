# tests/test_jzon.py

import unittest
from jzon import son

class TestJSONHandler(unittest.TestCase):
    def test_to_json(self):
        data = {
            "example.com": ["user@example.com", "password123"]
        }
        handler = son(data)
        handler.to_json("test_output.json")

if __name__ == "__main__":
    unittest.main()
