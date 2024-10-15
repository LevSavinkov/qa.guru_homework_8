import pytest

from models.cart import Cart
from models.product import Product


@pytest.fixture()
def cart():
    yield Cart()
    
    Cart().clear()
