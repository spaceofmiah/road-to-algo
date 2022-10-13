
class Flower:

    def __init__(self, name:str, petals_num:int, price:float) -> None:
        self._name = name
        self._price = price
        self._petal_num = petals_num
    
    def set_name(self, new_name:str):
        """Sets a new name for the flower"""
        self._name = new_name
    
    def set_price(self, new_price:float):
        """Sets a new price for flower"""
        self._price = new_price
    
    def set_petal(self, petal_num:int):
        """Set number of petal flower holds"""
        self._petal_num = petal_num
    
    def get_name(self) -> str:
        """Returns flower's name"""
        return self._name
    
    def get_price(self) -> float:
        """Returns flower's price"""
        return self._price
    
    def get_petal(self) -> int:
        """Returns flower's petal count"""
        return self._petal_num
