import argparse
from typing import Dict, List
from pathlib import Path
from loader import load_items_and_offers_from_json
from item import Item
from offer import Offer
from checkout import Checkout


def calculate_total_price(cart_string: str, items: Dict[str, Item], offers: List[Offer]) -> int:
  """
  Calculates the total price of items in the input string.

  Parameters:
    cart_string (str): The string of item names.
    items (Dict[str, Item]): A dictionary of item names to Item objects.
    offers (List[Offer]): A list of Offer objects.

  Returns:
    int: The total price of the items in the cart string.
  """

  checkout = Checkout(items, offers)

  for item_name in cart_string:
    checkout.add_item(item_name)
  
  return checkout.calculate_total()


def main():
  """
  The main function to run the supermarket checkout system.
  """

  parser = argparse.ArgumentParser(description="Supermarket Checkout System")
  parser.add_argument(
    "cart_string", nargs="?", type=str, default="", help="String of item names to calculate the total price."
  )
  args = parser.parse_args()

  root_path = Path(__file__).parent
  json_file_path = root_path / "items.json"

  try:
    items, offers = load_items_and_offers_from_json(json_file_path)
  except ValueError as e:
    print(e)
    return

  cart_string = args.cart_string.strip().upper()
  stocked_items = set(items.keys())

  print("Welcome to the Supermarket Checkout System!")
  print("Type 'total' to see the current total.")
  print("Type 'exit' to finish and see the final total.")

  while True:
    user_input = input("Enter item(s) or command: ").strip().upper()

    if user_input == 'EXIT':
      break
    elif user_input == 'TOTAL':
      total_price = calculate_total_price(cart_string, items, offers)

      print(f"Current total for items '{cart_string}': {total_price}")
    elif all(char in stocked_items for char in user_input):
      cart_string += user_input

      print(f"Added '{user_input}' to the cart.")
    else:
      print(f"Invalid input. Please enter valid item letters {stocked_items}, 'total', or 'exit'.")

  total_price = calculate_total_price(cart_string, items, offers)
  
  print(f"Final total for items '{cart_string}': {total_price}")
  print("Thank you for using the Supermarket Checkout System!")

if __name__ == "__main__":
  main()
