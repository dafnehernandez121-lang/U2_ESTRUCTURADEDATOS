class Cola:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def encolar(self, dato):
        self.elementos.append(dato)

    def desencolar(self):
        if not self.esta_vacia():
            return self.elementos.pop(0)
        return None

    def tamano(self):
        return len(self.elementos)


def sumar_colas(cola_a, cola_b):
    cola_resultado = Cola()

    while not cola_a.esta_vacia() and not cola_b.esta_vacia():
        dato_a = cola_a.desencolar()
        dato_b = cola_b.desencolar()
        suma = dato_a + dato_b
        cola_resultado.encolar(suma)

    return cola_resultado


if __name__ == "__main__":
    cola_a = Cola()
    cola_b = Cola()

    elementos_a = []
    elementos_b = []

    cantidad = int(input("¿Cuántos números tendrá cada cola?: "))

    print("\n--- Ingresa los números de la Cola A ---")
    for i in range(cantidad):
        num = int(input(f"Elemento {i + 1} de Cola A: "))
        elementos_a.append(num)
        cola_a.encolar(num)

    print("\n--- Ingresa los números de la Cola B ---")
    for i in range(cantidad):
        num = int(input(f"Elemento {i + 1} de Cola B: "))
        elementos_b.append(num)
        cola_b.encolar(num)

    print("\n*****************************************")
    print("      SUMA DE COLAS ELEMENTO A ELEMENTO  ")
    print("-----------------------------------------")
    print(f"Cola A inicial: {elementos_a}")
    print(f"Cola B inicial: {elementos_b}")
    print("-----------------------------------------")

    cola_res = sumar_colas(cola_a, cola_b)

    print("Resultado de la suma:")
    while not cola_res.esta_vacia():
        print(f"° {cola_res.desencolar()}")
    print("_________________________________________")