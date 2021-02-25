from tools.parser import Simulation, Street
from typing import List


class Solver:
    def __init__(self, s: Simulation):
        self.s = s
        self.output = ""

    def push(self, data):
        self.output += str(data) + '\n'

    def run(self):
        self.push(self.s.inters_nb)
        for inter, streets_indexes in self.s.map.items():
            self.push(inter)
            streets: List[Street] = []
            for street_index in streets_indexes:
                street: Street = self.s.streets[street_index]
                if street.end == inter:
                    streets.append(street)

            self.push(len(streets))
            m = sum(map(lambda x: x.trafic, streets))
            for street in streets:
                time = street.trafic * 30 / m
                self.push(f'{street.name} {int(time)}')
            #     print(street.name)
            # print(self.s.map[inter])
        print(self.output)
