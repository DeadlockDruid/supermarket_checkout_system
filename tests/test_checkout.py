import unittest
import sys
import os

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, parent_dir)

from item import Item
from special_offer import SpecialOffer
from checkout import Checkout
from loader import load_items_and_offers_from_json
from pathlib import Path



class TestCheckoutSystem(unittest.TestCase):

  def setUp(self):
    json_file_path = "items.json"

    self.items, self.offers = load_items_and_offers_from_json(json_file_path)


  def calculate_total_price(self, cart_string: str) -> int:
    checkout = Checkout(self.items, self.offers)

    for item_name in cart_string:
      checkout.add_item(item_name)
    
    return checkout.calculate_total()


  def test_empty_cart(self):
    self.assertEqual(self.calculate_total_price(""), 0)


  def test_single_item(self):
    self.assertEqual(self.calculate_total_price("A"), 50)
    self.assertEqual(self.calculate_total_price("B"), 30)


  def test_multiple_items(self):
    self.assertEqual(self.calculate_total_price("AB"), 80)
    self.assertEqual(self.calculate_total_price("CDBA"), 115)


  def test_repeated_items(self):
    self.assertEqual(self.calculate_total_price("AA"), 100)
    self.assertEqual(self.calculate_total_price("AAA"), 130)
    self.assertEqual(self.calculate_total_price("AAAA"), 180)
    self.assertEqual(self.calculate_total_price("AAAAA"), 230)
    self.assertEqual(self.calculate_total_price("AAAAAA"), 260)


  def test_combinations(self):
    self.assertEqual(self.calculate_total_price("AAAB"), 160)
    self.assertEqual(self.calculate_total_price("AAABB"), 175)
    self.assertEqual(self.calculate_total_price("AAABBD"), 190)
    self.assertEqual(self.calculate_total_price("DABABA"), 190)


  def test_invalid_items(self):
    with self.assertRaises(KeyError):
      self.calculate_total_price("XYZ")


if __name__ == '__main__':
  unittest.main()
