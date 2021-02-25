from tools.parser import Simulation, Street
from typing import List


class Solver:
    def __init__(self, s: Simulation):
        self.s = s

    def run(self):
        print(self.s.inters_nb)
        for inter, streets_indexes in self.s.map.items():
            print(inter)
            streets: List[Street] = []
            for street_index in streets_indexes:
                street: Street = self.s.streets[street_index]
                if street.end == inter:
                    streets.append(street)

            print(len(streets))
            for street in streets:
                print(street.name, 1)
            #     print(street.name)
            # print(self.s.map[inter])