import time

movimientos = 0

def torre_hanoi(n, origen, auxiliar, destino):
    global movimientos

    if n == 1:
        movimientos += 1
    else:
        torre_hanoi(n - 1, origen, destino, auxiliar)
        movimientos += 1
        torre_hanoi(n - 1, auxiliar, origen, destino)


def main():
    discos = [5, 10, 30, 64]

    for n in discos:
        cantidad = 2 ** n - 1

        print(f"\nDiscos: {n}")
        print(f"Movimientos necesarios: {cantidad:,}")

        #Aquí se calcula el tiempo
        global movimientos
        movimientos = 0

        inicio = time.perf_counter()

        torre_hanoi(n, "A", "B", "C")

        fin = time.perf_counter()

        print(f"Movimientos realizados: {movimientos:,}")
        print(f"Tiempo de ejecución: {fin - inicio:.6f} segundos")


if __name__ == "__main__":
    main()