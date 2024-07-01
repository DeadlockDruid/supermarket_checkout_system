import json
from typing import Tuple, Dict, List
from pathlib import Path
from schema import data_schema
from validator import validate_json
from item import Item
from special_offer import SpecialOffer


def load_items_and_offers_from_json(file_path: Path) -> Tuple[Dict[str, Item], List[SpecialOffer]]:
  """
  Loads items and offers from a JSON file.

  Parameters:
    file_path (Path): The path to the JSON file.
  
  Returns:
    Tuple[Dict[str, Item], List[SpecialOffer]]: A tuple containing a dictionary of items and a list of offers.
  
  Raises:
    ValueError: If the JSON data is invalid or duplicate.
  """
  
  with open(file_path, "r") as file:
    data = json.load(file)

  is_valid, error_message = validate_json(data, data_schema)
  items: Dict[str, Item] = {}
  offers: List[SpecialOffer] = []

  if not is_valid:
    raise ValueError(f"Invalid JSON data: {error_message}")
  
  for item_data in data["items"]:
    item_name = item_data["name"]

    if item_name in items:
      raise ValueError(f"Duplicate item found: {item_name}")
    
    item = Item(item_name, item_data["unit_price"])
    items[item_name] = item

    if item_data["special_offers"]:
      special_offers = [(offer["quantity_required"], offer["discounted_price"]) for offer in item_data["special_offers"]]
      offers.append(SpecialOffer(item, special_offers))
  
  return items, offers
