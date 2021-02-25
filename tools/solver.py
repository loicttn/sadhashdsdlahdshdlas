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
            streets: List[Street] = []
            for street_index in streets_indexes:
                street: Street = self.s.streets[street_index]
                if street.end == inter:
                    streets.append(street)

            schedule = []
            m = sum(map(lambda x: x.trafic, streets))
            m = 1 if m == 0 else m
            for street in streets:
                q = 400 if self.s.duration > 400 else self.s.duration
                time = (street.trafic * q / m )
                if int(time) == 0:
                    time += 1
                schedule.append(f'{street.name} {int(time)}')
            if len(schedule) != 0:
                self.push(inter)
                self.push(len(schedule))
                self.push('\n'.join(schedule))
            #     print(street.name)
            # print(self.s.map[inter])
        print(self.output[:-1])
