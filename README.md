# Examen_3_Parcial
Examen de la tercera unidad 
#Dylan Aaron Elicserio Martínez 3°W #Control:1179

#Codigo 1

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

class Alumno:

    def __init__(self, nombre, nota):
    
        self.nombre = nombre
        
        self.nota = nota

    def imprimir_info(self):
    
        print(f"Nombre del alumno: {self.nombre}")
        
        print(f"Nota del alumno: {self.nota}")

def resultado(self):

    if self.nota >= 6:
    
        return f"{self.nombre} ha aprobado."
        
    else:
    
        return f"{self.nombre} no ha aprobado."

def main():

    # Crear un objeto Alumno
    
    nombre = input("Ingrese el nombre del alumno: ")
    
    nota = float(input("Ingrese la nota del alumno: "))
    
    alumno = Alumno(nombre, nota)
    
    # Imprimir la información del alumno
    
    alumno.imprimir_info()
    
    # Mostrar el resultado
    
    print(alumno.resultado())

if __name__ == "__main__":

    main()

![image](https://github.com/user-attachments/assets/72740756-ff40-4a1a-b109-49014f3607b3)

![image](https://github.com/user-attachments/assets/7ac3ada9-7b8f-4879-9397-5915444a8689)

#Codigo 2

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

![image](https://github.com/user-attachments/assets/bc853a51-ac5f-47c3-a649-8e567793c784)

![image](https://github.com/user-attachments/assets/0411a579-fa8e-4910-98ce-35ad1bfb2a95)

#Codigo 3

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

#Función inicial

class Metodos:

    def __init__(self, lado1, lado2, lado3):
    
        self.lado1 = lado1
        
        self.lado2 = lado2
        
        self.lado3 = lado3
        
    def mostrar_datos(self):
    
        print(f"Primer lado: {self.lado1}")
        
        print(f"Segundo lado: {self.lado2}")
        
        print(f"Tercer lado: {self.lado3}")
        
    def triangulo_equilatero(self):
    
        if self.lado1 == self.lado2 == self.lado3:
        
            return "El triángulo es Equilátero"
            
        return None
        
    def triangulo_isosceles(self):
    
        if (self.lado1 == self.lado2 and self.lado1 != self.lado3) or \
        
        (self.lado1 == self.lado3 and self.lado2 != self.lado3) or \
        
        (self.lado2 == self.lado3 and self.lado1 != self.lado2):
        
            return "El triángulo es Isósceles"
            
        return None
        
    def triangulo_escaleno(self):
    
        if self.lado1 != self.lado2 and self.lado1 != self.lado3 and self.lado2 != self.lado3:
        
            return "El triángulo es Escaleno"
            
        return None
        
#Solicitar datos

def main():

    lado1 = float(input("Ingrese cuánto mide el primer lado del triángulo: "))
    
    lado2 = float(input("Ingrese cuánto mide el segundo lado del triángulo: "))
    
    lado3 = float(input("Ingrese cuánto mide el tercer lado del triángulo: "))
    
    #Crear una instancia de la clase Metodos
    
    triangulo = Metodos(lado1, lado2, lado3)
    
    #Mostrar los datos del triángulo
    
    triangulo.mostrar_datos()
    
    #Determinar el tipo de triángulo
    
    tipo_equilatero = triangulo.triangulo_equilatero()
    
    tipo_isosceles = triangulo.triangulo_isosceles()
    
    tipo_escaleno = triangulo.triangulo_escaleno()
    
    #Imprimir el tipo de triángulo
    
    if tipo_equilatero:
    
        print(tipo_equilatero)
        
    elif tipo_isosceles:
    
        print(tipo_isosceles)
        
    elif tipo_escaleno:
    
        print(tipo_escaleno)
        
    else:
    
        print("Los lados no forman un triángulo válido.")
        
if __name__ == "__main__":

    main()

![image](https://github.com/user-attachments/assets/5a103be6-2f50-40d4-9e84-30a8786bb46a)

![image](https://github.com/user-attachments/assets/01ce5c75-3ba2-4371-9174-a30b0439e3b8)

#Codigo 4

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

#Declarando las funciones principales

class Calculadora:

    def __init__(self, num1, num2):
    
        self.num1 = num1
        
        self.num2 = num2
        
    def suma(self):
    
        return self.num1 + self.num2
        
    def resta(self):
    
        return self.num1 - self.num2
        
    def multiplicacion(self):
    
        return self.num1 * self.num2
        
    def division(self):
    
        if self.num2 != 0:
        
            return self.num1 / self.num2
            
        else:
        
            return "Error: División por cero"
            
#Solicitar los valores al usuario

try:

    valor1 = int(input("Ingrese el primer número entero: "))
    
    valor2 = int(input("Ingrese el segundo número entero: "))
    
    #Crear una instancia de la clase Calculadora
    
    calculadora = Calculadora(valor1, valor2)
    
    #Realizar las operaciones y mostrar los resultados
    
    print(f"Suma: {calculadora.suma()}")
    
    print(f"Resta: {calculadora.resta()}")
    
    print(f"Multiplicación: {calculadora.multiplicacion()}")
    
    print(f"División: {calculadora.division()}")
    
except ValueError:

    print("Por favor, ingrese valores enteros válidos.")

![image](https://github.com/user-attachments/assets/8029f2a0-a747-4a80-ab5b-b5c39686a02a)

![image](https://github.com/user-attachments/assets/34909e8d-3a87-40ae-8396-15f0670d2aab)

#Codigo 5

print(" ")

print("Dylan Aaron Elicserio Martínez 3°W #Control:1179")

print(" ")

#Clase de contacto

class Contacto:

    def __init__(self, nombre, telefono, email):
    
        self.nombre = nombre
        
        self.telefono = telefono
        
        self.email = email

    def __str__(self):
    
        return f"Nombre: {self.nombre}, Teléfono: {self.telefono}, Email: {self.email}"
        
#Funcion principal

class Agenda:

    def __init__(self):
    
        self.contactos = []
        
    def añadir_contacto(self):
    
        nombre = input("Ingrese el nombre del contacto: ")
        
        telefono = input("Ingrese el teléfono del contacto: ")
        
        email = input("Ingrese el email del contacto: ")
        
        nuevo_contacto = Contacto(nombre, telefono, email)
        
        self.contactos.append(nuevo_contacto)
        
        print("Contacto añadido exitosamente.")
        
    def listar_contactos(self):
    
        if not self.contactos:
        
            print("La agenda está vacía.")
            
        else:
        
            print("Lista de contactos:")
            
            for contacto in self.contactos:
            
                print(contacto)
                
    def buscar_contacto(self):
    
        nombre = input("Ingrese el nombre del contacto a buscar: ")
        
        for contacto in self.contactos:
        
            if contacto.nombre.lower() == nombre.lower():
            
                print("Contacto encontrado:")
                
                print(contacto)
                
                return
                
        print("Contacto no encontrado.")
        
#Funcion para editar el contacto

    def editar_contacto(self):
    
        nombre = input("Ingrese el nombre del contacto a editar: ")
        
        for contacto in self.contactos:
        
            if contacto.nombre.lower() == nombre.lower():
            
                nuevo_nombre = input("Ingrese el nuevo nombre (deje en blanco para no cambiar): ")
                
                nuevo_telefono = input("Ingrese el nuevo teléfono (deje en blanco para no cambiar): ")
                
                nuevo_email = input("Ingrese el nuevo email (deje en blanco para no cambiar): ")
                
                if nuevo_nombre:
                
                    contacto.nombre = nuevo_nombre
                    
                if nuevo_telefono:
                
                    contacto.telefono = nuevo_telefono
                    
                if nuevo_email:
                
                    contacto.email = nuevo_email
                
                print("Contacto editado exitosamente.")
                
                return
                
        print("Contacto no encontrado.")
        
    #Menu para escoger
    
    def menu(self):
    
        while True:
        
            print("\n--- Menú de la Agenda ---")
            
            print("1. Añadir contacto")
            
            print("2. Lista de contactos")
            
            print("3. Buscar contacto")
            
            print("4. Editar contacto")
            
            print("5. Cerrar agenda")
            
            opcion = input("Seleccione una opción: ")
            
            if opcion == "1":
            
                self.añadir_contacto()
                
            elif opcion == "2":
            
                self.listar_contactos()
                
            elif opcion == "3":
            
                self.buscar_contacto()
                
            elif opcion == "4":
            
                self.editar_contacto()
                
            elif opcion == "5":
            
                print("Cerrando agenda...")
                
                break
                
            else:
            
                print("Opción no válida. Por favor, intente de nuevo.")
                
#Código para ejecutar la agenda

if __name__ == "__main__":

    agenda = Agenda()
    
    agenda.menu()

![image](https://github.com/user-attachments/assets/7adc7434-89de-4bbe-b07a-88541532ccad)

![image](https://github.com/user-attachments/assets/1171bd06-0e8a-4b7d-80fd-fbf6ecf4e22f)

