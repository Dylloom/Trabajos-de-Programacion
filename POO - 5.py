class Circulo:
     def __init__(self, radio):
         self.radio = radio
         self.diametro = radio * 2

     def obtener_radio(self):
         return self.radio
     
     def obtener_diametro(self):
         return self.diametro
     
     def calcular_area(self):
         area = 3.14 * self.radio ** 2
         return area

     def calcular_circunferencia(self):
         circunferencia = self.diametro * 3.14
         return circunferencia
     
if __name__ == "__main__":
    Circulo1 = Circulo(5)
    
    print(f"Radio: {Circulo1.obtener_radio()}")
    print(f"Diametro: {Circulo1.obtener_diametro()}")
    print(f"Area: {Circulo1.calcular_area()}")
    print(f"Circunferencia: {Circulo1.calcular_circunferencia()}")

