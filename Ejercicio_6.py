# Definimos la clase Estudiante
class Estudiante:
    """Clase que representa a un estudiante con nombre, edad y notas."""

    def __init__(self, nombre, edad):
        """Constructor que inicializa el nombre, la edad y una lista vacía de notas."""
        self.nombre = nombre
        self.edad = edad
        self.notas = []

    def agregar_nota(self, nota):
        """Método para agregar una nota a la lista de notas del estudiante."""
        self.notas.append(nota)

    def promedio(self):
        """Método que calcula y devuelve el promedio de las notas."""
        if self.notas:
            return sum(self.notas) / len(self.notas)
        return 0  # Retorna 0 si no hay notas

    def detalle(self):
        """Método que muestra el nombre, edad y promedio del estudiante."""
        print(f"Estudiante: {self.nombre}, Edad: {self.edad}, Promedio: {self.promedio():.2f}")

# Lista para almacenar los estudiantes
estudiantes = []

# Pedir al usuario el número de estudiantes
num_estudiantes = int(input("Ingrese la cantidad de estudiantes: "))

# Bucle para registrar los datos de cada estudiante
for i in range(num_estudiantes):
    print(f"\nIngresando datos del estudiante {i + 1}:")
    
    nombre = input("Nombre del estudiante: ")
    edad = int(input("Edad del estudiante: "))
    
    estudiante = Estudiante(nombre, edad)
    
    # Pedir 4 notas al usuario
    for j in range(4):
        nota = float(input(f"Ingrese la nota {j + 1}: "))
        estudiante.agregar_nota(nota)

    # Agregar el estudiante a la lista
    estudiantes.append(estudiante)

# Mostrar los detalles de cada estudiante
print("\nDetalles de los estudiantes registrados:")
for est in estudiantes:
    est.detalle()
