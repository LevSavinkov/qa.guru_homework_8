"""
Протестируйте классы из модуля tests/models.py
"""
import pytest

from models.product import Product
from src.enums.errors_enums import NOT_ENOUGH_ERROR
from tests.conftest import cart

boll = Product("boll", 50.21, "This is a boll", 300)


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    
    def test_cart_add_products(self, product, cart):
        cart.add_product(product, 2)
        assert cart.products[product] == 2
        
        cart.add_product(product, 2)
        assert cart.products[product] == 4
    
    def test_cart_remove_product(self, product, cart):
        cart.add_product(product, 5)
        cart.remove_product(product, 10)
        assert cart.products == {}
        
        cart.add_product(product, 5)
        cart.remove_product(product, 1)
        assert cart.products[product] == 4
        
        cart.remove_product(product)
        assert cart.products == {}
    
    def test_cart_clear_cart(self, product, cart):
        cart.add_product(product, 5)
        cart.add_product(boll, 10)
        cart.clear()
        assert cart.products == {}
    
    def test_cart_get_total_price(self, product, cart):
        cart.add_product(product, 5)
        cart.add_product(boll, 10)
        assert cart.get_total_price() == 1002.1
    
    def test_cart_success_buy(self, product, cart):
        cart.add_product(product, 500)
        cart.add_product(boll, 100)
        assert cart.buy() == "Success!"
        assert product.quantity == 500
        assert boll.quantity == 200
    
    def test_cart_buy_more_products(self, product, cart):
        cart.add_product(product, 50)
        cart.add_product(boll, 310)
        with pytest.raises(ValueError) as err:
            cart.buy()
        assert str(err.value) == NOT_ENOUGH_ERROR
