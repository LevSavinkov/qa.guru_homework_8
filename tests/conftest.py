import pytest

from models.cart import Cart
from models.product import Product

cart = Cart()


@pytest.fixture(scope="session", autouse=True)
def product():
    return Product("book", 100, "This is a book", 1000)


def create_cart(product, count):
    return cart.add_product(product, count)


@pytest.fixture(scope="function", autouse=False)
def new_cart(product):
    cart.clear()
    
    yield create_cart
    
    cart.remove_product(product)
