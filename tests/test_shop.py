"""
Протестируйте классы из модуля tests/models.py
"""
import pytest

from tests.conftest import cart


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """
    
    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(-1) == "The value must be more than or equal to 0"
        assert product.check_quantity(0) is True
        assert product.check_quantity(999) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False
    
    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        with pytest.raises(ValueError) as err:
            product.buy(-1)
        assert str(err.value) == "The value must be more than or equal to 0"
        assert product.buy(0) is True
        assert product.buy(500) is True
        assert product.buy(1000) is True
    
    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError) as err:
            product.buy(1500)
        print(err)
        assert str(err.value) == "Not enough products in the shop to buy"


class TestCart:
    """
    TODO Напишите тесты на методы класса Cart
        На каждый метод у вас должен получиться отдельный тест
        На некоторые методы у вас может быть несколько тестов.
        Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
    """
    
    def test_add_products(self, product, new_cart):
        cart.add_product(product, 2)
        assert cart.products[product] == 2
        
        cart.add_product(product, 2)
        assert cart.products[product] == 4
    
    def test_remove_product(self, product, new_cart):
        new_cart(product, 5)
        cart.remove_product(product, 10)
        assert cart.products == {}
        
        new_cart(product, 5)
        cart.remove_product(product, 1)
        assert cart.products[product] == 4
        
        cart.remove_product(product)
        assert cart.products == {}
    
    def test_clear_cart(self, product, new_cart):
        new_cart(product, 5)
        cart.clear()
        assert cart.products == {}
    
    def test_get_total_price(self, product, new_cart):
        new_cart(product, 5)
        assert cart.get_total_price(product) == 500.0
    
    def test_success_buy(self, product, new_cart):
        new_cart(product, 800)
        assert cart.buy(product) == "Success!"
        assert product.quantity == 200
    
    def test_buy_more_products(self, product, new_cart):
        new_cart(product, 1800)
        with pytest.raises(ValueError) as err:
            cart.buy(product)
        assert str(err.value) == "Not enough the products in the shop"
