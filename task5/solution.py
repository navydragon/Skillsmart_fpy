"""
Задание 5: канатоходец
"""

from pymonad.maybe import Just, Nothing

# смещение числа птиц на левом краю
raw_add_left = lambda n: lambda pole: Just([pole[0] + n, pole[1]])

# смещение на правом краю
raw_add_right = lambda n: lambda pole: Just([pole[0], pole[1] + n])

# баланс по правилу : abs(лево − право) не больше 4
if_balanced = (
    lambda pole: Just(pole)
    if abs(pole[0] - pole[1]) <= 4
    else Nothing
)

to_left = lambda num: (
    lambda pole: Just(pole).bind(raw_add_left(num)).bind(if_balanced)
)

to_right = lambda num: (
    lambda pole: Just(pole).bind(raw_add_right(num)).bind(if_balanced)
)

banana = lambda pole: Nothing

begin = lambda: Just([0, 0])


def show(maybe):
    if maybe == Nothing:
        print(False)
    else:
        print(True)
        print(maybe.value)


if __name__ == "__main__":
    show(
        begin()
        .bind(to_left(2))
        .bind(to_right(5))
        .bind(to_left(-2))
    )
    show(
        begin()
        .bind(to_left(2))
        .bind(to_right(4))
        .bind(to_left(-1))
    )
    show(
        begin()
        .bind(to_left(2))
        .bind(banana)
        .bind(to_right(5))
        .bind(to_left(-1))
    )
