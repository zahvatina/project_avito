"""Классы пицц"""


class Pizza:
    """Базовый класс пиццы"""
    def __init__(self, size: str) -> None:
        self.size = size
        self.ingredients = {}

    def __eq__(self, other) -> bool:
        return self.size == other.size and \
               self.ingredients == other.ingridients

    def __iter__(self):
        yield 'size', self.size
        yield 'ingridients', self.ingredients


class Margherita(Pizza):
    """Пицца - маргарита"""
    def __init__(self, size='L') -> None:
        super().__init__(size)
        self.ingredients = {
            'sauce': 'tomato sauce',
            'cheese': 'mozzarella',
            'filling': 'tomatoes'
        }

    def __str__(self) -> str:
        return 'Margherita 🧀'


class Pepperoni(Pizza):
    """Пицца - пипперони"""
    def __init__(self, size='L') -> None:
        super().__init__(size)
        self.ingredients = {
            'sauce': 'tomato sauce',
            'cheese': 'mozzarella',
            'filling': 'pepperoni'
        }

    def __str__(self) -> str:
        return 'Pepperoni 🍕'


class Hawaiian(Pizza):
    """Пицца - гавайская"""
    def __init__(self, size='L') -> None:
        super().__init__(size)
        self.ingredients = {
            'sauce': 'tomato sauce',
            'cheese': 'mozzarella',
            'filling': 'chicken',
            'extra filling': 'pineapples'
        }

    def __str__(self) -> str:
        return 'Hawaiian'
