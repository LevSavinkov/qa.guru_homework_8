import pytest

from src.enums.errors_enums import NEGATIVE_NUMBER_ERROR, NOT_ENOUGH_ERROR


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """
    
    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        with pytest.raises(ValueError) as err:
            product.check_quantity(-1)
        assert str(err.value) == NEGATIVE_NUMBER_ERROR
        assert product.check_quantity(0) is True
        assert product.check_quantity(999) is True
        assert product.check_quantity(1000) is True
        assert product.check_quantity(1001) is False
    
    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        with pytest.raises(ValueError) as err:
            product.buy(-1)
        assert str(err.value) == NEGATIVE_NUMBER_ERROR
        assert product.buy(0) == 1000
        assert product.buy(500) == 500
        assert product.buy(1000) == 0
    
    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError) as err:
            product.buy(1500)
        print(err)
        assert str(err.value) == NOT_ENOUGH_ERROR
