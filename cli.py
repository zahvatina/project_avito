import sys
import click
from random import randint

from pizza import Margherita, Pepperoni, Hawaiian, Pizza


@click.group()
def cli():
    pass


@cli.command()
@click.option('--delivery', default=False, is_flag=True)
@click.argument('pizza', nargs=1)
def order(pizza: str, delivery: bool) -> None:
    """
    Готовит и доставляет пиццу
    :param pizza: название пиццы
    :param delivery: нужна ли доставка
    :return:
    """
    # Находим пиццу на складе
    try:
        pizza = getattr(sys.modules[__name__], pizza.capitalize())()
    except AttributeError:
        print('Такой пицци на складе нет!')
        return
    print('Вы выбрали пиццу: {}'.format(str(pizza)))
    bake_func(pizza)
    if delivery:
        delivery_func(pizza)
    else:
        pickup_func(pizza)


@cli.command()
def menu() -> None:
    """Выводит меню"""
    pizzas = [Margherita(), Pepperoni(), Hawaiian()]
    for pizza in pizzas:
        print('- {}: {}'.format(
            str(pizza), ', '.join(pizza.ingredients.values()))
        )


def log(fn_or_output):
    """Декаратор"""

    def decorator(fn):
        def wrapper(*args, **kwargs):
            if callable(fn_or_output):
                print('{} - {}c!'.format(fn_or_output.__name__, randint(1, 3)))
            else:
                print(fn_or_output.format(randint(1, 3)))
            return fn(*args, **kwargs)

        return wrapper

    if callable(fn_or_output):
        return decorator(fn_or_output)
    else:
        return decorator


@log
def bake_func(pizza: Pizza):
    """Готовит пиццу"""


@log('🛵 Доставили за {}с!')
def delivery_func(pizza: Pizza):
    """Доставляет пиццу"""


@log('🏠 Забрали за {}с!')
def pickup_func(pizza: Pizza):
    """Самовывоз"""


if __name__ == '__main__':
    cli()
