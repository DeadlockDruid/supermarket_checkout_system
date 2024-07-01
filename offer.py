from abc import ABC, abstractmethod
from item import Item


class Offer(ABC):
  """
  A base class for offers.

  Methods:
    apply_offer(cart: str, item: Item) -> float:
      Applies the offer to the cart and returns the total price after the offer.
  """
  
  @abstractmethod
  def apply_offer(self, cart: dict) -> int:
    """
    Applies the offer to the cart.

    Parameters:
      cart (dict): The cart as a dictionary of item names to thier counts.
    
    Returns:
      float: The total price after the offer is applied.
    """
    pass
