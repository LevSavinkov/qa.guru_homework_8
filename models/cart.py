from models.product import Product
from src.enums.errors_enums import NOT_ENOUGH_ERROR


class Cart:
    """
    Класс корзины. В нем хранятся продукты, которые пользователь хочет купить.
    TODO реализуйте все методы класса
    """
    
    # Словарь продуктов и их количество в корзине
    products: dict[Product, int]
    
    def __init__(self):
        # По-умолчанию корзина пустая
        self.products = {}
    
    def add_product(self, product: Product, buy_count=1):
        """
        Метод добавления продукта в корзину.
        Если продукт уже есть в корзине, то увеличиваем количество
        """
        if product in self.products:
            self.products[product] += buy_count
        else:
            self.products[product] = buy_count
    
    def remove_product(self, product: Product, remove_count=None):
        """
        Метод удаления продукта из корзины.
        Если remove_count не передан, то удаляется вся позиция
        Если remove_count больше, чем количество продуктов в позиции, то удаляется вся позиция
        """
        if product not in self.products:
            return "No such product in the cart"
        else:
            if remove_count is None or remove_count >= self.products[product]:
                self.products.pop(product)
            elif remove_count < self.products[product]:
                self.products[product] -= remove_count
    
    def clear(self):
        self.products.clear()
    
    def get_total_price(self) -> float:
        total_price: float = 0
        for product in self.products:
            total_price += product.price * self.products[product]
        return round(total_price, 2)
    
    def buy(self):
        """
        Метод покупки.
        Учтите, что товаров может не хватать на складе.
        В этом случае нужно выбросить исключение ValueError
        """
        for product in self.products:
            if not product.check_quantity(self.products[product]):
                raise ValueError(NOT_ENOUGH_ERROR)
            else:
                product.buy(self.products[product])
        self.clear()
        return "Success!"
