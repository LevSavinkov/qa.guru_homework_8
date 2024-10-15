import pytest

from src.enums.errors_enums import NEGATIVE_NUMBER_ERROR, NOT_ENOUGH_ERROR
from tests.helpers.products import Products

book = Products().book


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """
    
    def test_book_check_quantity(self):
        # TODO напишите проверки на метод check_quantity
        assert book.check_quantity(0) is True
        assert book.check_quantity(999) is True
        assert book.check_quantity(1000) is True
        assert book.check_quantity(1001) is False
    
    def test_book_check_quantity_negative(self):
        with pytest.raises(ValueError) as err:
            book.check_quantity(-1)
        assert str(err.value) == NEGATIVE_NUMBER_ERROR
    
    def test_book_buy(self):
        # TODO напишите проверки на метод buy
        assert book.buy(0) == 1000
        assert book.buy(500) == 500
        assert book.buy(1000) == 0
    
    def test_book_buy_negative(self):
        with pytest.raises(ValueError) as err:
            book.buy(-1)
        assert str(err.value) == NEGATIVE_NUMBER_ERROR
    
    def test_book_buy_more_than_available(self):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError) as err:
            book.buy(1500)
        print(err)
        assert str(err.value) == NOT_ENOUGH_ERROR
