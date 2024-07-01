from typing import List, Tuple
from offer import Offer
from item import Item


class SpecialOffer(Offer):
  """
  Represents a special offer for an item.

  Attributes:
    item (Item): The item to which the offer applies.
    offers (List[Tuple[int, float]]): A list of tuples, each containing the quantity required and the discounted price.
  
  Methods:
    apply_offer(cart: dict, item: Item) -> float:
      Applies the special offer to the cart item and returns the total price after the offer.
  """
  
  def __init__(self, item: Item, offers: List[Tuple[int, int]]) -> None:
    """
    Initializes a SpecialOffer instance.

    Parameters:
      item (Item): The item to which the offer applies.
      offers (List[Tuple[int, float]]): A list of tuples, each containing the quantity required and the discounted price.
    """
    
    self.item = item
    self.offers = offers
  

  def apply_offer(self, cart: dict) -> int:
    """
    Applies the special offer to the cart.

    Parameters:
      cart (dict): The cart as a dictionary of item names to their counts.

    Returns:
      float: The total price after the offer is applied. Applies the best one if multiple offers are present.
    """

    item_name = self.item.name

    if item_name in cart:
      item_count = cart[item_name]
      min_price = item_count * self.item.unit_price

      for quantity_required, discounted_price in self.offers:
        num_discounts = item_count // quantity_required
        remainder = item_count % quantity_required
        total_price = num_discounts * discounted_price + remainder * self.item.unit_price
        min_price = min(min_price, total_price)

      return min_price

    return 0
