"""
Defines JSON schemas for validating item data and offer data.
"""

item_schema = {
  "type": "object",
  "properties": {
    "name": {"type": "string", "pattern": "^[A-Za-z]$"},
    "unit_price": {"type": "number", "minimum": 0},
    "special_offers": {
      "type": "array",
      "items": {
        "type": "object",
        "properties": {
          "quantity_required": {"type": "number", "minimum": 1},
          "discounted_price": {"type": "number", "minimum": 0}
        },
        "required": ["quantity_required", "discounted_price"]
      }
    }
  },
  "required": ["name", "unit_price", "special_offers"]
}

data_schema = {
  "type": "object",
  "properties": {
    "items": {
      "type": "array",
      "items": item_schema
    }
  },
  "required": ["items"]
}
