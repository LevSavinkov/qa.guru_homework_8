from dataclasses import dataclass

from src.enums.errors_enums import NEGATIVE_NUMBER_ERROR, NOT_ENOUGH_ERROR


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
            raise ValueError(NEGATIVE_NUMBER_ERROR)
        else:
            return self.quantity >= quantity
    
    def buy(self, quantity):
        """
        TODO реализуйте метод покупки
            Проверьте количество продукта используя метод check_quantity
            Если продуктов не хватает, то выбросите исключение ValueError
        """
        if quantity < 0:
            raise ValueError(NEGATIVE_NUMBER_ERROR)
        else:
            if self.check_quantity(quantity):
                self.quantity -= quantity
                return self.quantity
            else:
                raise ValueError(NOT_ENOUGH_ERROR)
    
    def __hash__(self):
        return hash(self.name + self.description)
