# ********RoostGPT********
"""
Test generated by RoostGPT for test python-oop-test using AI Type Open AI and AI Model gpt-4

Test generated by RoostGPT for test python-oop-test using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=hapus_item_ba34e340e6
ROOST_METHOD_SIG_HASH=hapus_item_3704d929a1


Scenario 1: Delete an Existing Product from the Shopping Cart
Details:
  TestName: test_delete_existing_product
  Description: This test is intended to verify that the function hapus_item can successfully delete a product that exists in the shopping cart.
Execution:
  Arrange: Initialize a ShoppingCart object with some products in the keranjang attribute.
  Act: Call the hapus_item function on the ShoppingCart object, passing the name of an existing product as a parameter.
  Assert: Check that the product is no longer in the keranjang attribute of the ShoppingCart object.
Validation:
  This test is important to ensure the function correctly implements the business requirement of being able to remove items from the shopping cart.

Scenario 2: Attempt to Delete a Non-Existing Product from the Shopping Cart
Details:
  TestName: test_delete_non_existing_product
  Description: This test is intended to verify the behavior of the function hapus_item when asked to delete a product that does not exist in the shopping cart.
Execution:
  Arrange: Initialize a ShoppingCart object with some products in the keranjang attribute.
  Act: Call the hapus_item function on the ShoppingCart object, passing the name of a product that does not exist in the keranjang as a parameter.
  Assert: Check that the keranjang attribute of the ShoppingCart object remains unchanged.
Validation:
  This test is important to ensure the function correctly handles the scenario where a non-existent item is attempted to be removed, without affecting other items in the shopping cart.

Scenario 3: Delete a Product from an Empty Shopping Cart
Details:
  TestName: test_delete_product_from_empty_cart
  Description: This test is intended to verify the behavior of the function hapus_item when the shopping cart is empty.
Execution:
  Arrange: Initialize a ShoppingCart object with an empty keranjang attribute.
  Act: Call the hapus_item function on the ShoppingCart object, passing any product name as a parameter.
  Assert: Check that the keranjang attribute of the ShoppingCart object remains empty.
Validation:
  This test is important to ensure the function correctly handles the scenario where it is asked to remove an item from an empty shopping cart, without causing any errors.
"""

# ********RoostGPT********
import pytest
from Contoh import ShoppingCart

class Test_ShoppingCartHapusItem:
    @pytest.mark.regression
    def test_delete_existing_product(self):
        # Arrange
        shopping_cart = ShoppingCart('Juragan')
        shopping_cart.tambah_item('Laptop Acer', 1200, 2)
        shopping_cart.tambah_item('Monitor LG 19inch', 1500, 2)

        # Act
        shopping_cart.hapus_item('Laptop Acer')

        # Assert
        assert 'Laptop Acer' not in [item['produk'] for item in shopping_cart.keranjang]

    @pytest.mark.regression
    def test_delete_non_existing_product(self):
        # Arrange
        shopping_cart = ShoppingCart('Juragan')
        shopping_cart.tambah_item('Laptop Acer', 1200, 2)
        shopping_cart.tambah_item('Monitor LG 19inch', 1500, 2)

        # Act
        shopping_cart.hapus_item('Smartphone Samsung')

        # Assert
        assert len(shopping_cart.keranjang) == 2

    @pytest.mark.regression
    def test_delete_product_from_empty_cart(self):
        # Arrange
        shopping_cart = ShoppingCart('Juragan')

        # Act
        shopping_cart.hapus_item('Laptop Acer')

        # Assert
        assert len(shopping_cart.keranjang) == 0
