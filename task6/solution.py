"""
Задание 6: монада состояний

Железнодорожный рейс: журнал событий накапливается в цепочке,
состояние поезда (топливо, экипаж, деньги, груз) передаётся только в run()

результат цепочки - log (журнал)
скрытое состояние - train (словарь с топливом, деньгами и т.д.)
"""

from pymonad.state import State
from pymonad.tools import curry

# перегоны: расстояние (км) и плата за путь (руб.)
legs = {
    ("Москва", "Тверь"): {"km": 167, "fee": 1200},
    ("Тверь", "СПб"): {"km": 485, "fee": 3500},
    ("Тверь", "Ржев"): {"km": 90, "fee": 600},
}

FUEL_PER_KM = 2.5
LOAD_MAX_T = 2000
AVG_SPEED_KMH = 80
LOADING_HOURS = 1.0

DEFAULT_FUEL_PRICE = 58

trip_init = {
    "log": [],
    "train": {
        "fuel_l": 12000,
        "crew_h": 0.0,
        "cash": 100000,
        "load_t": 0,
    },
}

trip_state = State.insert(trip_init["log"])


def _fuel_for_leg(km, load_t):
    return km * FUEL_PER_KM * (1 + load_t / LOAD_MAX_T)


@curry(3)
def run_leg(station_from, station_to, log):
    """Перегон: расход топлива, время экипажа, плата за путь."""

    def step(train):
        leg = legs[(station_from, station_to)]
        fuel = _fuel_for_leg(leg["km"], train["load_t"])
        hours = leg["km"] / AVG_SPEED_KMH
        new_train = {
            "fuel_l": train["fuel_l"] - fuel,
            "crew_h": train["crew_h"] + hours,
            "cash": train["cash"] - leg["fee"],
            "load_t": train["load_t"],
        }
        new_log = log + [("run", station_from, station_to)]
        return new_log, new_train

    return State(step)


@curry(3)
def load_cargo(cargo_name, tons, log):
    """Погрузка: увеличение массы и стоянка на путях."""

    def step(train):
        new_train = {
            "fuel_l": train["fuel_l"],
            "crew_h": train["crew_h"] + LOADING_HOURS,
            "cash": train["cash"],
            "load_t": train["load_t"] + tons,
        }
        new_log = log + [("load", cargo_name, tons)]
        return new_log, new_train

    return State(step)


@curry(2)
def crew_rest(hours, log):
    """Отдых экипажа: сброс накопленных часов в пути."""

    def step(train):
        new_train = {
            **train,
            "crew_h": max(0.0, train["crew_h"] - hours),
        }
        new_log = log + [("rest", hours)]
        return new_log, new_train

    return State(step)


@curry(3)
def refuel_at_station(station, liters, log):
    """Заправка на любой станции по единой цене DEFAULT_FUEL_PRICE."""

    def step(train):
        cost = liters * DEFAULT_FUEL_PRICE
        new_train = {
            "fuel_l": train["fuel_l"] + liters,
            "crew_h": train["crew_h"],
            "cash": train["cash"] - cost,
            "load_t": train["load_t"],
        }
        new_log = log + [("refuel", station, liters)]
        return new_log, new_train

    return State(step)




if __name__ == "__main__":
    trip_plan = (
        trip_state.then(run_leg("Москва", "Тверь"))
        .then(load_cargo("уголь", 40))
        .then(crew_rest(8))
        .then(run_leg("Тверь", "СПб"))
        .then(refuel_at_station("СПб", 800))
    )

    log, train = trip_plan.run(trip_init["train"])
    print("Журнал:", log)
    print("Поезд:", train)
