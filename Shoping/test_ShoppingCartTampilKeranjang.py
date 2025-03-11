# ********RoostGPT********
"""
Test generated by RoostGPT for test python-oop-test using AI Type Open AI and AI Model gpt-4

ROOST_METHOD_HASH=tampil_keranjang_9a9ae624df
ROOST_METHOD_SIG_HASH=tampil_keranjang_91dda67794


```
Scenario 1: Testing the function with an empty cart
Details:
  TestName: test_empty_cart
  Description: This test is intended to verify that the function correctly handles the situation when the cart is empty.
Execution:
  Arrange: Initialize an instance of ShoppingCart class with any name and an empty cart.
  Act: Invoke the function tampil_keranjang with no parameters.
  Assert: The expected outcome is that the function should display the name of the buyer and total bill as 0.
Validation:
  This test is important to ensure that the function can handle edge cases and does not throw an error when the cart is empty.

Scenario 2: Testing the function with multiple items in the cart
Details:
  TestName: test_multiple_items
  Description: This test is intended to verify that the function correctly calculates the total bill for multiple items in the cart.
Execution:
  Arrange: Initialize an instance of ShoppingCart class with any name and add multiple items to the cart.
  Act: Invoke the function tampil_keranjang with no parameters.
  Assert: The expected outcome is that the function should display the name of the buyer, details of the items in the cart, and the correct total bill.
Validation:
  This test is important to ensure that the function correctly implements the business logic and can handle typical scenarios.

Scenario 3: Testing the function with different types of products
Details:
  TestName: test_different_product_types
  Description: This test is intended to verify that the function correctly handles different types of products.
Execution:
  Arrange: Initialize an instance of ShoppingCart class with any name and add different types of products to the cart.
  Act: Invoke the function tampil_keranjang with no parameters.
  Assert: The expected outcome is that the function should display the name of the buyer, details of the different types of products in the cart, and the correct total bill.
Validation:
  This test is important to ensure that the function is flexible and supports different types of products.
```

"""

# ********RoostGPT********
import pytest
from Contoh import ShoppingCart

class Test_ShoppingCartTampilKeranjang:
    
    @pytest.mark.regression
    def test_empty_cart(self):
        # Arrange
        cart = ShoppingCart('John Doe')
        # Act
        result = cart.tampil_keranjang()
        # Assert
        assert result == ('John Doe', 0)

    @pytest.mark.regression
    @pytest.mark.performance
    def test_multiple_items(self):
        # Arrange
        cart = ShoppingCart('Jane Doe')
        cart.tambah_item('item1', 100, 2)
        cart.tambah_item('item2', 200, 3)
        # Act
        result = cart.tampil_keranjang()
        # Assert
        assert result == ('Jane Doe', [('item1', 100, 2, 200), ('item2', 200, 3, 600)], 800)

    @pytest.mark.regression
    @pytest.mark.performance
    def test_different_product_types(self):
        # Arrange
        cart = ShoppingCart('Doe Junior')
        cart.tambah_item('book', 50, 1)
        cart.tambah_item('laptop', 1000, 1)
        # Act
        result = cart.tampil_keranjang()
        # Assert
        assert result == ('Doe Junior', [('book', 50, 1, 50), ('laptop', 1000, 1, 1000)], 1050)
