from typing import Dict, List
from item import Item
from special_offer import Offer


class Checkout:
  """
  Represents a checkout process in the supermarket.

  Attributes:
    cart (Dict[str, int]): The cart as a dictionary of item names to their counts.
    items (Dict[str, Item]): A dictionary of item names to Item objects.
    offers (List[Offer]): A list of Offer objects.

  Methods:
    add_item(item_name: str):
      Adds an item to the cart.
    calculate_best_offer(item: Item) -> int:
      Calculates the best offer for an item in the cart.
    calculate_total() -> int:
      Calculates the total price of the items in the cart.
  """

  def __init__(self, items: Dict[str, Item], offers: List[Offer]) -> None:
    """
    Initializes a Checkout instance.

    Parameters:
      items (Dict[str, Item]): A dictionary of item names to Item objects.
      offers (List[Offer]): A list of Offer objects.
    """

    self.cart: Dict[str, int] = {}
    self.items = items
    self.offers = offers
  

  def add_item(self, item_name: str) -> None:
    """
    Adds an item to the cart.

    Parameters:
      item_name (str): The name of the item to add to the cart.
    """

    if item_name in self.cart:
      self.cart[item_name] += 1
    else:
      self.cart[item_name] = 1
  

  def calculate_best_offer(self, item: Item) -> int:
    """
    Calculates the best offer for an item in the cart.

    Parameters:
      item (Item): The item for which to calculate the best offer.

    Returns:
      int: The total price after applying the best offer.
    """

    applicable_offers = [offer for offer in self.offers if offer.item.name == item.name]
    item_count = self.cart[item.name]
    min_price = item_count * item.unit_price

    for offer in applicable_offers:
      min_price = min(min_price, offer.apply_offer(self.cart))
    
    return min_price


  def calculate_total(self) -> int:
    """
    Calculates the total price of the items in the cart.

    Returns:
      int: The total price of the items in the cart.
    """

    total = 0

    for item_name, count in self.cart.items():
      item = self.items[item_name]
      total += self.calculate_best_offer(item)
    
    return total
