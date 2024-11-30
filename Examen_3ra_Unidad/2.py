print(" ")
print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")
print(" ")
#Funcion inicial
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    def mostrar_datos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
    def es_mayor_de_edad(self):
        return self.edad >= 18
def main():
    #Solicitar datos al usuario
    nombre = input("Ingrese el nombre de la persona: ")
    edad = int(input("Ingrese la edad de la persona: "))
    #Crear una instancia de Persona
    persona = Persona(nombre, edad)
    #Mostrar los datos de la persona
    persona.mostrar_datos()
    #Indicar si es mayor de edad o no
    if persona.es_mayor_de_edad():
        print(f"{persona.nombre} es mayor de edad.")
    else:
        print(f"{persona.nombre} no es mayor de edad.")
if __name__ == "__main__":
    main()