# ********RoostGPT********
"""
Test generated by RoostGPT for test python-oop-test using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=tambah_item_ab3c7163fb
ROOST_METHOD_SIG_HASH=tambah_item_86b63dc9da


```
Scenario 1: Adding a single item to the shopping cart
Details:
  TestName: test_tambah_item_single
  Description: This test is intended to verify that a single item can be successfully added to the shopping cart.
Execution:
  Arrange: Initialize a ShoppingCart object with a given nama_pembeli.
  Act: Invoke the tambah_item function on the ShoppingCart object, passing in a product name, price, and quantity of 1.
  Assert: The shopping cart should contain a dictionary representing the added item, which includes the product name, price, quantity, and total cost.
Validation:
  This test is important because it verifies the basic functionality of the tambah_item function. The expected result aligns with the function's specifications and the requirement to add items to the shopping cart.

Scenario 2: Adding multiple items to the shopping cart
Details:
  TestName: test_tambah_item_multiple
  Description: This test is intended to verify that multiple items can be successfully added to the shopping cart.
Execution:
  Arrange: Initialize a ShoppingCart object with a given nama_pembeli.
  Act: Invoke the tambah_item function on the ShoppingCart object multiple times, each time passing in a different product name, price, and quantity.
  Assert: The shopping cart should contain multiple dictionaries, each representing one of the added items.
Validation:
  This test is important because it verifies that the shopping cart can handle multiple items. The expected result aligns with the function's specifications and the requirement to support multiple purchases.

Scenario 3: Adding an item with a quantity greater than 1
Details:
  TestName: test_tambah_item_quantity
  Description: This test is intended to verify that an item with a quantity greater than 1 can be successfully added to the shopping cart, and that the total cost is calculated correctly.
Execution:
  Arrange: Initialize a ShoppingCart object with a given nama_pembeli.
  Act: Invoke the tambah_item function on the ShoppingCart object, passing in a product name, price, and a quantity greater than 1.
  Assert: The shopping cart should contain a dictionary representing the added item, with the correct total cost (quantity * price).
Validation:
  This test is important because it verifies that the tambah_item function can correctly handle quantities greater than 1. The expected result aligns with the function's specifications and the requirement to calculate the total cost of each item.

Scenario 4: Adding an item with a zero quantity
Details:
  TestName: test_tambah_item_zero_quantity
  Description: This test is intended to verify the behavior of the tambah_item function when an item with zero quantity is added.
Execution:
  Arrange: Initialize a ShoppingCart object with a given nama_pembeli.
  Act: Invoke the tambah_item function on the ShoppingCart object, passing in a product name, price, and a quantity of zero.
  Assert: The shopping cart should contain a dictionary representing the added item, with a total cost of zero.
Validation:
  This test is important because it checks how the tambah_item function handles edge cases. The expected result aligns with the function's specifications and the requirement to calculate the total cost of each item.
```
"""

# ********RoostGPT********
import pytest
from Contoh import ShoppingCart

class Test_ShoppingCartTambahItem:

    def test_tambah_item_single(self):
        # Arrange
        keranjang_ku = ShoppingCart('Juragan')
        # Act
        keranjang_ku.tambah_item('Laptop Acer', 1200, 1)
        # Assert
        assert keranjang_ku.keranjang == [{'produk': 'Laptop Acer', 'harga': 1200, 'jumlah': 1, 'total': 1200}]

    def test_tambah_item_multiple(self):
        # Arrange
        keranjang_ku = ShoppingCart('Juragan')
        # Act
        keranjang_ku.tambah_item('Laptop Acer', 1200, 2)
        keranjang_ku.tambah_item('Monitor LG 19inch', 1500, 2)
        # Assert
        assert keranjang_ku.keranjang == [{'produk': 'Laptop Acer', 'harga': 1200, 'jumlah': 2, 'total': 2400}, {'produk': 'Monitor LG 19inch', 'harga': 1500, 'jumlah': 2, 'total': 3000}]

    def test_tambah_item_quantity(self):
        # Arrange
        keranjang_ku = ShoppingCart('Juragan')
        # Act
        keranjang_ku.tambah_item('Laptop Acer', 1200, 3)
        # Assert
        assert keranjang_ku.keranjang == [{'produk': 'Laptop Acer', 'harga': 1200, 'jumlah': 3, 'total': 3600}]

    def test_tambah_item_zero_quantity(self):
        # Arrange
        keranjang_ku = ShoppingCart('Juragan')
        # Act
        keranjang_ku.tambah_item('Laptop Acer', 1200, 0)
        # Assert
        assert keranjang_ku.keranjang == [{'produk': 'Laptop Acer', 'harga': 1200, 'jumlah': 0, 'total': 0}]
