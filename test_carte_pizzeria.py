import pytest
from unittest.mock import Mock

from carte_pizzeria import CartePizzeria
from exceptions import CartePizzeriaException


def make_pizza_mock(name: str):
    p = Mock()
    p.name = name
    return p


def test_is_empty_when_created():
    carte = CartePizzeria()

    assert carte.is_empty() is True
    assert carte.nb_pizzas() == 0


def test_add_pizza_makes_menu_not_empty():
    carte = CartePizzeria()
    pizza = make_pizza_mock("Margherita")

    carte.add_pizza(pizza)

    assert carte.is_empty() is False
    assert carte.nb_pizzas() == 1


def test_nb_pizzas_counts_correctly_with_multiple_adds():
    carte = CartePizzeria()

    carte.add_pizza(make_pizza_mock("Margherita"))
    carte.add_pizza(make_pizza_mock("Pepperoni"))
    carte.add_pizza(make_pizza_mock("4 Fromages"))

    assert carte.nb_pizzas() == 3


def test_remove_pizza_removes_existing_pizza_by_name():
    carte = CartePizzeria()
    carte.__pizzas = [make_pizza_mock("Margherita"), make_pizza_mock("Pepperoni")]

    carte.remove_pizza("Margherita")

    assert len(carte._pizzas) == 1


def test_remove_pizza_raises_exception_if_not_found():
    carte = CartePizzeria()
    carte.add_pizza(make_pizza_mock("Margherita"))

    with pytest.raises(CartePizzeriaException):
        carte.remove_pizza("Hawaiian")
