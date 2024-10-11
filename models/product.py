from dataclasses import dataclass


@dataclass
class Product:
    """
    Класс продукта
    """
    name: str
    price: float
    description: str
    quantity: int
    
    def check_quantity(self, quantity) -> bool:
        """
        TODO Верните True если количество продукта больше или равно запрашиваемому
            и False в обратном случае
        """
        if quantity >= 0:
            return self.quantity >= quantity
    
    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if quantity < 0:
            raise ValueError("The value must be more than or equal to 0")
        else:
            if self.check_quantity(quantity):
                return self.check_quantity(quantity)
            else:
                raise ValueError("Not enough products in the shop to buy")
    
    def __hash__(self):
        return hash(self.name + self.description)
