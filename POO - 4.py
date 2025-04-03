class Rectangulo:
     def __init__(self, longitud, anchura):
         self.longitud = longitud
         self.anchura = anchura
         
     def obtener_longitud(self):
         return self.longitud
     
     def obtener_anchura(self):
         return self.anchura
     
     def calcular_area(self):
         area = self.longitud * self.anchura
         return area
     def calcular_perimetro(self):
         perimetro = (self.longitud + self.anchura) * 2
         return perimetro
     
if __name__ == "__main__":
    Rectangulo1 = Rectangulo(5, 3)
    
    print(f"Longitud: {Rectangulo1.obtener_longitud()}")
    print(f"Precio: {Rectangulo1.obtener_anchura()}")
    print(f"Area: {Rectangulo1.calcular_area()}")
    print(f"Perimetro: {Rectangulo1.calcular_perimetro()}")
