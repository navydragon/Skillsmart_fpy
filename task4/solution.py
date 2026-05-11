"""
Задание 4

На основе каррированной add() функция add10 принимает один функторный
аргумент (Just или ListMonad) и прибавляет 10 к каждому «внутреннему»
значению через map, не меняя структуру контейнера.
"""

from pymonad.list import ListMonad
from pymonad.maybe import Just, Nothing
from pymonad.tools import curry


@curry(2)
def add(x, y):
    return x + y


def add10(functor):
    return functor.map(add(10))


if __name__ == "__main__":
    print(add10(Just(5)))
    print(add10(Nothing))
    print(add10(ListMonad(1, 2, 3, 4)))
