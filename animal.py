class Animal:
    def __init__(self, nombre, edad, salud,felicidad) -> None:
        self.nombre = nombre
        self.edad = edad
        self.salud = salud
        self.felicidad = felicidad
    
    def display_info(self):
        print(f"Nombre:{self.nombre} Salud:{self.salud} Felicidad:{self.felicidad}")
        return self
    
    def alimentar(self):
        self.salud += 10
        self.felicidad += 10
        return self
    
class Loro(Animal):
    def __init__(self, nombre,edad=5,salud=60,felicidad=60) -> None:
        super().__init__(nombre,edad,salud,felicidad)
        self.frases_conocidas = []
    
    def alimentar(self):
        self.salud += 5
        self.felicidad += 5
        return self
    
    def agregar_frase(self,frase):
        self.frases_conocidas.append(frase)
        return self

class Ardilla(Animal):
    def __init__(self, nombre,edad=2,salud=80,felicidad=80) -> None:
        super().__init__(nombre,edad,salud,felicidad)
        self.nueces_escondidas = 0
    
    def guardar_nueces(self,num):
        self.nueces_escondidas += num
        return self
    
    def alimentar(self):
        self.salud += 3
        self.felicidad += 3
        return self

class Orangutan(Animal):
    def __init__(self, nombre,edad=5,salud=70,felicidad=70) -> None:
        super().__init__(nombre,edad,salud,felicidad)
        self.simbolo_senas = False
    
    def alimentar(self):
        self.salud += 3
        self.felicidad += 3
        return self
    
    def ensenar_senas(self):
        self.simbolo_senas=True
        return self