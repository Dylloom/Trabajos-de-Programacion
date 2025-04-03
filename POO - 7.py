class Banco:
    def __init__(self, banco, tna):
        self.banco = banco
        self.tna = tna

    def obtener_banco(self):
        return self.banco
        
    def obtener_tna(self):
        return self.tna

    def interes(self, canti):
        interes = canti * (self.tna/100)
        return interes

    def tiempo_dup(self, canti):
        interes = (self.tna/100) * canti
        suma = 0
        meses = 0
        while (suma < canti*2):
            suma += interes
            meses += 1
        return meses
            

if __name__ == "__main__":
    sujeto1 = Banco("BBVA", 2.4)
    
    print(f"Banco: {sujeto1.obtener_banco()}")
    print(f"Tasa de interes: {sujeto1.obtener_tna()}%")
    aux = float(input("Cantidad a ingresar: "))
    print(f"Interes un mes: {sujeto1.interes(aux)}")
    print(f"Hasta duplicar: {sujeto1.tiempo_dup(aux)}")
