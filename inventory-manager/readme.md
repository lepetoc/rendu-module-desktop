# Inventory Manager

## Overview

The Simple Inventory Manager is a user-friendly desktop application designed to help small businesses and individuals manage their inventory efficiently. Built with Python and PySide6, it offers an intuitive graphical user interface (GUI) that allows users to add, update, and delete inventory items with ease. This document serves as a guide to installing, running, and utilizing the basic features of the Simple Inventory Manager.

## Features

- **Add Product:** Users can add new products to the inventory by specifying details such as product name, quantity, price, and description.
- **Add Supplier:** Enables the addition of suppliers, including their name, contact details, and associated products.
- **View Inventory:** Displays a list of all inventory items along with their details.
- **View Products:** Shows detailed information about each product, including available stock levels.
- **View Inventory History:** Displays a log of inventory changes, including incoming and outgoing products.
- **View Product History:** Provides a history of transactions (incoming and outgoing) for a specific product.
- **View Suppliers:** Lists all suppliers with their detailed information.
- **View Sales:** Displays sales records, including total price.
- **View Purchases:** Shows purchase records, including total price.

## Prerequisites

Before installing the Simple Inventory Manager, ensure that you have the following prerequisites installed on your system:

- Python 3.6 or newer
- pip (Python package installer)

## Installation

1. **Clone the Repository:**
   First, clone the repository to your local machine.

   Navigate into the project directory:
   ```
   cd simple-inventory-manager
   ```

2. **Install Dependencies:**
   Install the required Python packages including PySide6 by running:
   ```
   pip install -r requirements.txt
   ```

## Running the Application

To run the Simple Inventory Manager, execute the following command in the project directory:
```
python main.py
```
This will launch the application's GUI, from which you can start managing your inventory.

## Acknowledgements

- **PySide6:** For providing a comprehensive set of tools to build the GUI.
- **Python:** The programming language used to develop this application.

This README reflects an updated version that includes additional features such as adding suppliers, viewing sales and purchases with total prices, and detailed inventory and product history tracking.