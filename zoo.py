class Animal:
    def __init__(self, nombre) -> None:
        self.nombre = nombre
        self.edad = 1
        self.salud = 80
        self.felicidad = 80
    
class Loro(Animal):
    def __init__(self, nombre) -> None:
        super().__init__(nombre)
        self.frases_conocidas = []