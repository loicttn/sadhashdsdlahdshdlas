from tools.parser import Simulation, Street

class Solver:
    def __init__(self, s: Simulation):
        self.s = s

    def run(self):
        print(self.s.inters_nb)
        for inter, streets_indexes in self.s.map.items():
            print(inter)
            print(len(streets_indexes))
            for street_index in streets_indexes:
                street: Street = self.s.streets[street_index]
                print(street.name, 1)
            #     print(street.name)
            # print(self.s.map[inter])