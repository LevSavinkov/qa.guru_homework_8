import pytest

from models.cart import Cart
from models.product import Product


@pytest.fixture()
def cart():
    yield Cart()
    
    Cart().clear()

@pytest.fixture()
def product():
    book = Product("book", 100, "This is a book", 1000)
    ball = Product("ball", 50.21, "This is a ball", 300)
    
    yield book, ball
    