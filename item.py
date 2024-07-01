class Item:
  def __init__(self, name: str, unit_price: int) -> None:
    """
    Represents an item in the supermarket.

    Attributes:
      name (str): The name of the item.
      unit_price (float): The price per unit of the item.
    """
    self.name = name
    self.unit_price = unit_price
