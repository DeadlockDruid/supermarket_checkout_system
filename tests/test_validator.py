import unittest
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from validator import validate_json
from schema import item_schema, data_schema


class TestValidateJson(unittest.TestCase):
  """
  Tests JSON schema validator
  """

  def test_valid_data(self):
    data = {
      "items": [
        {
          "name": "A",
          "unit_price": 50,
          "special_offers": [
            {"quantity_required": 3, "discounted_price": 130}
          ]
        },
        {
          "name": "B",
          "unit_price": 30,
          "special_offers": [
            {"quantity_required": 2, "discounted_price": 45}
          ]
        }
      ]
    }

    is_valid, error_message = validate_json(data, data_schema)

    self.assertTrue(is_valid)
    self.assertIsNone(error_message)


  def test_missing_required_field(self):
    data = {
      "items": [
        {
          "unit_price": 50,  # Missing 'name' field
          "special_offers": [
            {"quantity_required": 3, "discounted_price": 130}
          ]
        }
      ]
    }

    is_valid, error_message = validate_json(data, data_schema)
    
    self.assertFalse(is_valid)
    self.assertIsNotNone(error_message)


  def test_invalid_field_type(self):
    data = {
      "items": [
        {
          "name": "A",
          "unit_price": "50",  # 'unit_price' should be a number
          "special_offers": [
            {"quantity_required": 3, "discounted_price": 130}
          ]
        }
      ]
    }

    is_valid, error_message = validate_json(data, data_schema)

    self.assertFalse(is_valid)
    self.assertIsNotNone(error_message)


  def test_empty_special_offers(self):
    data = {
      "items": [
        {
          "name": "A",
          "unit_price": 50,
          "special_offers": []  # Empty special offers array
        }
      ]
    }

    is_valid, error_message = validate_json(data, data_schema)
    
    self.assertTrue(is_valid)
    self.assertIsNone(error_message)


  def test_invalid_special_offer(self):
    data = {
      "items": [
        {
          "name": "A",
          "unit_price": 50,
          "special_offers": [
            { "quantity_required": "three", "discounted_price": 130 }  # Invalid type for quantity_required
          ]
        }
      ]
    }

    is_valid, error_message = validate_json(data, data_schema)

    self.assertFalse(is_valid)
    self.assertIsNotNone(error_message)


if __name__ == '__main__':
  unittest.main()
