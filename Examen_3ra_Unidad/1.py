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