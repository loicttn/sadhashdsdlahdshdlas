from typing import *

class Street:
    def __init__(self, name: str, l: int, start: int, end: int):
        self.name = name
        self.start = start
        self.end = end
        self.l = l
        self.trafic = 0

    def __str__(self):
        return f"name:{self.name}\tstarts:{str(self.start)}\tends:{self.end}\tlength:{self.l}"

class Simulation:
    def __init__(self, duration: int, inters_nb: int, street_nb: int, cars_nb: int, points: int):
        self.duration = duration
        self.inters_nb = inters_nb
        self.cars_nb = cars_nb
        self.street_nb = street_nb
        self.points = points
        self.streets = []
        self.cars = []
        self.map = {}

class Car:
    def __init__(self, l: int):
        self.l = l
        self.streets = []

    def __str__(self):
        return f"l:{self.l}\tstreets:{self.streets}"

class Parser:
    def __init__(self):
        pass

    def run(self, c: List[str]) -> Simulation:
        s = Simulation(*map(int,c[0].split()))
        # dict key: intersection index, values: [street index in s.streets]
        for i in range(s.street_nb):
            street = c[i+1].split()
            s.streets.append(Street(street[2], int(street[-1]), int(street[0]), int(street[1])))
            if s.map.get(int(street[0])) is None:
                s.map[int(street[0])] = []
            if s.map.get(int(street[1])) is None:
                s.map[int(street[1])] = []
            s.map[int(street[0])].append(i)
            s.map[int(street[1])].append(i)
        # ttl = 0
        print("HERE")
        car = []
        for i in range(s.cars_nb):
            car += c[i+1+s.street_nb].split()
        for s in s.streets:
            s.trafic = car.count(s.name)
        print("THERE")
        # print(ttl / s.cars_nb)
        return s
