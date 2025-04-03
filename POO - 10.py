class Libro:
    def __init__(self, titulo, autor, genero, pagina):
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.pagina = pagina

    def obtener_titulo(self):
        return self.titulo

    def establecer_titulo(self, titulo):
        self.nombre = titulo

    def obtener_autor(self):
        return self.autor

    def establecer_autor(self, autor):
        self.autor = autor

    def obtener_genero(self):
        return self.genero

    def establecer_genero(self, genero):
        self.genero = genero

    def obtener_pagina(self):
        return self.pagina

    def establecer_pagina(self, pagina):
        self.pagina = pagina

    def ficcion(self):
        a = "No"
        if (self.genero == "Ficcion"):
            a = "Si"
        return a
        
if __name__ == "__main__":
    sujeto1 = Libro("Mi lucha", "Hitler", "Ficcion", 100)
    
    print(f"titulo: {sujeto1.obtener_titulo()}")
    print(f"autor: {sujeto1.obtener_autor()}")
    print(f"genero: {sujeto1.obtener_genero()}")
    print(f"paginas: {sujeto1.obtener_pagina()}")
    print(f"Es ficcion?: {sujeto1.ficcion()}")
    print("")

    sujeto1.establecer_titulo("Cronica de un goleador")
    sujeto1.establecer_autor("Messi")
    sujeto1.establecer_genero("Realista")
    sujeto1.establecer_pagina(999)

    print(f"titulo: {sujeto1.obtener_titulo()}")
    print(f"autor: {sujeto1.obtener_autor()}")
    print(f"genero: {sujeto1.obtener_genero()}")
    print(f"paginas: {sujeto1.obtener_pagina()}")
    print(f"Es ficcion?: {sujeto1.ficcion()}")
