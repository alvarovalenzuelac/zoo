from animal import Ardilla, Loro, Orangutan

class Zoo:
    def __init__(self,zoo_name) -> None:
        self.animals = []
        self.zoo_name = zoo_name
    def add_loro(self,name):
        self.animals.append(Loro(name))
        return self
    def add_ardilla(self,name):
        self.animals.append(Ardilla(name))
        return self
    def add_orangutan(self,name):
        self.animals.append(Orangutan(name))
        return self
    def print_all_info(self):
        print(f"*** {self.zoo_name} ***")
        for a in self.animals:
            a.display_info()
        return self

zoo1 = Zoo("Maravillozoo").add_ardilla("Chip").add_loro("Pirata").add_orangutan("Mauricio").print_all_info()