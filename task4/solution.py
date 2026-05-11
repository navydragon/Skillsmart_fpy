"""
Задание 4

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
