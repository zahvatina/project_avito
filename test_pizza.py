from pizza import Margherita, Pepperoni


def test_dict():
    """Тестируем функцию dict()"""
    expected = {
        'size': 'M',
        'ingredients': {
            'cheese': 'mozzarella',
            'filling': 'tomatoes',
            'sauce': 'tomato sauce'
        }
    }
    actual = dict(Margherita(size='M'))
    assert actual == expected


def test_eq_true():
    """Тестируем функцию __eq__ в случае одинаковых пицц"""
    assert Margherita(size='L') == Margherita(size='L')


def test_eq_false():
    """Тестируем функцию __eq__ в случае разных пицц"""
    assert Margherita(size='L') != Pepperoni(size='L')
