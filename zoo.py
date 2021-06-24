from animal import Ardilla, Loro, Orangutan

def menu2():
	zoologico = Zoo(input("Ingrese el nombre del zoologico: "))
	print(f"Bienvenido al zoologico {zoologico.zoo_name}")
	while True:
		print("\n1 : Muestra la informacion del Zoologico.")
		print("2 : Agregar animales.")
		print("3 : Alimentar animales.")
		print("4 : Salir.")
		respuesta = input("Seleccione una opcion: ")
		try:
			int(respuesta)
		except ValueError:
			print("Debe ingresar un numero")
			continue
		if respuesta == "1":
			zoologico.print_all_info()
		elif respuesta == "2":
			lista_animales = ["Loro","Ardilla","Orangutan"]
			n = 1
			print("")
			for i in lista_animales:
				print(f"{n} : {i}")
				n += 1

			respuesta_2 = input("Seleccione el animal a crear en el zoologico:")
			try:
				int(respuesta)
			except ValueError:
				print("Debe ingresar un numero")
				continue
			nombre = input(f"Ingrese el nombre del/a {lista_animales[int(respuesta_2)-1]}: ")
			if respuesta_2 == "1":
				zoologico.add_loro(nombre)
			elif respuesta_2 == "2":
				zoologico.add_ardilla(nombre)
			elif respuesta_2 == "3":
				zoologico.add_orangutan(nombre)
		elif respuesta == "3":
			if len(zoologico.animals) == 0:
				print("Primero debe ingresar un animal.")
				continue
			zoologico.print_all_info()
			alimentar = input("Seleccione un animal para alimentar: ")
			zoologico.animals[int(alimentar)-1].alimentar()
		elif respuesta == "4":
			print("Salio del programa.")
			exit()

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
		print(f"\n*** {self.zoo_name} ***")
		if len(self.animals)==0:
			print("Sin animales.")
			return self
		for i in range(len(self.animals)):
			print(f"{i+1} : ",end = '')
			self.animals[i].display_info()
		return self

#zoo1 = Zoo("Maravillozoo").add_ardilla("Chip").add_loro("Pirata").add_orangutan("Mauricio").print_all_info()

if __name__ == '__main__':
	#Zoo(input("Ingrese el nombre del zoologico: ")).menu()
	menu2()