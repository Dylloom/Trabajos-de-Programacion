class Producto:
     def __init__(self, nombre, precio, stock):
         self.nombre = nombre
         self.precio = precio 
         self.stock = stock 
         
     def obtener_nombre(self):
         return self.nombre
     
     def obtener_precio(self):
         return self.precio
     
     def obtener_stock(self):
         return self.stock
     
     def stock_aumentar(self, aumen_dismi):
         self.stock = self.stock + aumen_dismi
         return self.stock
     
if __name__ == "__main__":
    Producto1 = Producto("Leche", 12, 100)
    
    print(f"Nombre: {Producto1.obtener_nombre()}")
    print(f"Precio: {Producto1.obtener_precio()}")
    print(f"Stock: {Producto1.obtener_stock()} unidades")
    print("Para aumentar solo ponga el numero, para disminuir escriba en negativo")
    aux = int(input("Suma/Resta stock: "))
    print(f"Stock: {Producto1.stock_aumentar(aux)} unidades")
