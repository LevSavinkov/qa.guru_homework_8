class ErrorUtil:
    
    @staticmethod
    def negative_number_error():
        raise ValueError("The value must be more than or equal to 0")
    
    @staticmethod
    def not_enough_error():
        raise ValueError("Not enough products in the shop to buy")
