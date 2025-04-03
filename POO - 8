class Tienda:
    def __init__(self, nombre, producto):
        self.nombre = nombre
        lista = [producto]
        self.lista = lista

    def obtener_nombre(self):
        return self.nombre

    def obtener_lista(self):
        return self.lista

    def añadir(self, nuevo):
        listaaux = self.lista
        aux = True
        for a in listaaux:
            if (nuevo == listaaux):
                aux = False
        if (aux == True):
            listaaux.append(nuevo)
        self.lista = listaaux
    
    def eliminar(self, elim):
        listaaux = self.lista
        for a in listaaux:
            if (a == elim):
                listaaux.remove(elim)
        self.lista = listaaux
    
        
        
if __name__ == "__main__":
    sujeto1 = Tienda("Coto", "Oreo")
    
    print(f"Nombre: {sujeto1.obtener_nombre()}")
    print(f"Lista de productos: {sujeto1.obtener_lista()}")
    print("1: Sumar producto")
    print("2: Eliminar producto")
    resp = 0
    while (resp != 2):
        print("1: Sumar producto")
        print("2: Eliminar producto")
        nel = int(input("Añadir/Eliminar producto: "))
        if nel == 1:
            suma = str(input("Nombre del producto a agregar: "))
            sujeto1.añadir(suma)
            print(f"Lista de productos: {sujeto1.obtener_lista()}")
        else:
            resta = str(input("Nombre del producto a eliminar: "))
            sujeto1.eliminar(resta)
            print(f"Lista de productos: {sujeto1.obtener_lista()}")
        print("1: Si")
        print("2: No")
        resp = int(input("Repetir?: "))
