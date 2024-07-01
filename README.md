# Supermarket Checkout System

This project is a supermarket checkout system that calculates the total price of items added to the cart by the customer. The system supports individual pricing and special offers.

## Prerequisites

- Docker

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/anshu1992/supermarket_checkout_system.git
cd supermarket_checkout
```

### 2. Build the Docker Image

```bash
docker build -t supermarket_checkout .
```

### 3. Run the Application

To run the application interactively, use the following command:

```bash
docker run -it --rm supermarket_checkout
```

You can also pass an initial cart string as an argument:

```bash
docker run -it --rm supermarket_checkout python main.py "AABCD"
```

### 4. Run the Tests

To run the tests, use the following command:

```bash
docker run --rm supermarket_checkout python -m unittest discover -s tests
```

## Project Structure

- `Dockerfile`: The Dockerfile to build the application image.
- `requirements.txt`: The list of Python dependencies.
- `items.json`: The JSON file containing the item data and special offers.
- `main.py`: The main entry point of the application.
- `item.py`: Contains the `Item` class.
- `offer.py`: Contains the `Offer` base class.
- `special_offer.py`: Contains the `SpecialOffer` class.
- `checkout.py`: Contains the `Checkout` class.
- `schema.py`: Defines JSON schemas for validating item data and offer data.
- `validator.py`: Provides a function to validate JSON data against a schema.
- `loader.py`: Provides a function to load items and offers from a JSON file.
- `tests/`: Directory containing test files for the project.

## Usage

When running the application, you will be prompted to enter item names or commands:

- Enter item names (e.g., `AAB`, `cdd`) to add them to the cart.
- Type `total` to see the current total.
- Type `exit` to finish and see the final total.

Example:

```bash
$ docker run -it --rm supermarket-checkout

Welcome to the Supermarket Checkout System!
Type 'total' to see the current total.
Type 'exit' to finish and see the final total.
Enter item(s) or command: aBdd
Added 'ABDD' to the cart.
Enter item(s) or command: total
Current total for items 'ABDD': 110
Enter item(s) or command: CDA
Added 'CDA' to the cart.
Enter item(s) or command: total
Current total for items 'ABDDCDA': 195
Enter item(s) or command: exit
Final total for items 'ABDDCDA': 195
Thank you for using the Supermarket Checkout System!
```
