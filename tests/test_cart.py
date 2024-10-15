"""
Протестируйте классы из модуля tests/models.py
"""
import pytest

from src.enums.errors_enums import NOT_ENOUGH_ERROR
from tests.conftest import cart


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    
    def test_cart_add_products(self, book, cart):
        cart.add_product(book, 2)
        assert cart.products[book] == 2
        
        cart.add_product(book, 2)
        assert cart.products[book] == 4
    
    def test_cart_remove_product(self, book, cart):
        cart.add_product(book, 5)
        cart.remove_product(book, 10)
        assert cart.products == {}
        
        cart.add_product(book, 5)
        cart.remove_product(book, 5)
        assert cart.products == {}
        
        cart.add_product(book, 5)
        cart.remove_product(book, 1)
        assert cart.products[book] == 4
        
        cart.remove_product(book)
        assert cart.products == {}
    
    def test_cart_clear_cart(self, book, ball, cart):
        cart.add_product(book, 5)
        cart.add_product(ball, 10)
        cart.clear()
        assert cart.products == {}
    
    def test_cart_get_total_price(self, book, ball, cart):
        cart.add_product(book, 5)
        cart.add_product(ball, 10)
        assert cart.get_total_price() == 1002.1
    
    def test_cart_success_buy(self, book, ball, cart):
        cart.add_product(book, 500)
        cart.add_product(ball, 100)
        assert cart.buy() == "Success!"
        assert book.quantity == 500
        assert ball.quantity == 200
    
    def test_cart_buy_more_products(self, book, ball, cart):
        cart.add_product(book, 50)
        cart.add_product(ball, 310)
        print(cart.products)
        with pytest.raises(ValueError) as err:
            cart.buy()
        assert str(err.value) == NOT_ENOUGH_ERROR
