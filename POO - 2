Hoy = 2025
class Coche:
     def __init__(self, marca, modelo, anio_fab):
         self.marca = marca
         self.modelo = modelo
         self.anio_fab = anio_fab
         
     def obtener_marca(self):
         return self.marca
     
     def obtener_modelo(self):
         return self.modelo
     
     def obtener_anio_fab(self):
         return self.anio_fab
     
     def anios_desde_fab(self, anio_hoy):
         anios_de_fab = anio_hoy - self.anio_fab
         return anios_de_fab
     
if __name__ == "__main__":
    Coche1 = Coche("Ferrari", "Roma", 2019)
    
    print(f"Marca: {Coche1.obtener_marca()}")
    print(f"Modelo: {Coche1.obtener_modelo()}")
    print(f"Año de fabricacion: {Coche1.obtener_anio_fab()}")
    print(f"Años desde fabricacion: {Coche1.anios_desde_fab(Hoy)}")
