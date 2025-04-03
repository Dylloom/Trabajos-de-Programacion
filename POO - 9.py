class Empleado:
    def __init__(self, nombre, edad, salario, cargo):
        self.nombre = nombre
        self.edad = edad
        self.salario = salario
        self.cargo = cargo

    def obtener_nombre(self):
        return self.nombre

    def establecer_nombre(self, nombre):
        self.nombre = nombre

    def obtener_edad(self):
        return self.edad

    def establecer_edad(self, edad):
        self.edad = edad

    def obtener_salario(self):
        return self.salario

    def establecer_salario(self, salario):
        self.salario = salario

    def obtener_cargo(self):
        return self.cargo

    def establecer_cargo(self, cargo):
        self.cargo = cargo

    def salario_anual(self):
        sal_anual = self.salario*12
        return sal_anual
    
        
        
if __name__ == "__main__":
    sujeto1 = Empleado("Wos", 27, 100000, "Cantante")
    
    print(f"Nombre: {sujeto1.obtener_nombre()}")
    print(f"Edad: {sujeto1.obtener_edad()}")
    print(f"Salario: {sujeto1.obtener_salario()}$")
    print(f"Cargo: {sujeto1.obtener_cargo()}")
    print(f"Salario anual: {sujeto1.salario_anual()}$")
    print("")

    sujeto1.establecer_nombre("Jose")
    sujeto1.establecer_edad(42)
    sujeto1.establecer_salario(10000)
    sujeto1.establecer_cargo("Operario")

    print(f"Nombre: {sujeto1.obtener_nombre()}")
    print(f"Edad: {sujeto1.obtener_edad()}")
    print(f"Salario: {sujeto1.obtener_salario()}$")
    print(f"Cargo: {sujeto1.obtener_cargo()}")
    print(f"Salario anual: {sujeto1.salario_anual()}$")

