from dataclasses import dataclass
from src.utils.errors_util import ErrorUtil


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
        if quantity < 0:
            ErrorUtil.negative_number_error()
        else:
            return self.quantity >= quantity
    
    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if quantity < 0:
            ErrorUtil.negative_number_error()
        else:
            if self.check_quantity(quantity):
                return self.quantity - quantity
            else:
                ErrorUtil.not_enough_error()
    
    def __hash__(self):
        return hash(self.name + self.description)
