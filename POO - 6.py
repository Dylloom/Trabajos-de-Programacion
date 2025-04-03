class Estudiante:
    def __init__(self, nombre, edad, carrera):
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre
        
    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_carrera(self):
        return self.carrera

    def establecer_carrera(self, carrera):
        self.carrera = carrera

    def nota_media(self, examenes):
        total = sum(examenes)
        return total / len(examenes)

if __name__ == "__main__":
    sujeto1 = Estudiante("Marcos", 19, "Ingeniería informática")
    
    print(f"Nombre: {sujeto1.obtener_nombre()}")
    print(f"Edad: {sujeto1.obtener_edad()}")
    print(f"Carrera: {sujeto1.obtener_carrera()}")
    
    aux = int(input("Cuántos exámenes: "))
    exam = []
    
    for i in range(aux):
        nota = int(input(f"Nota del examen {i + 1}: "))
        exam.append(nota)
    
    print(f"Nota media: {sujeto1.nota_media(exam)}")

    sujeto1.establecer_nombre("Ayelen")
    sujeto1.establecer_edad(25)
    sujeto1.establecer_carrera("Filosofía")

    print("\nDespués de actualizar:")
    print(f"Nombre: {sujeto1.obtener_nombre()}")
    print(f"Edad: {sujeto1.obtener_edad()}")
    print(f"Carrera: {sujeto1.obtener_carrera()}")
    
    aux = int(input("Cuántos exámenes: "))
    exam = []
    
    for i in range(aux):
        nota = int(input(f"Nota del examen {i + 1}: "))
        exam.append(nota)
    
    print(f"Nota media: {sujeto1.nota_media(exam)}")
