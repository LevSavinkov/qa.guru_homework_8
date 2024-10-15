from models.product import Product


class Products:
    
    def __init__(self):
        self.book = Product("book", 100, "This is a book", 1000)
        self.ball = Product("ball", 50.21, "This is a ball", 300)
