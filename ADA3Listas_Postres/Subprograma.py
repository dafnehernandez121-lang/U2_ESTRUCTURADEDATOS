from ArregloPostres import menu


def eliminar_postres_repetidos(arreglo_postres):
    if len(arreglo_postres) <= 1:
        print("\n[INFO] El arreglo tiene 0 o 1 elemento; no hay repetidos para eliminar.")
        return

    i = 0
    eliminados = 0

    while i < len(arreglo_postres) - 1:
        if arreglo_postres[i].nombre.lower() == arreglo_postres[i + 1].nombre.lower():
            duplicado = arreglo_postres[i + 1]
            actual = duplicado.lista_ingredientes
            while actual is not None:
                sig = actual.siguiente
                actual.siguiente = None
                actual = sig
            duplicado.lista_ingredientes = None

            del arreglo_postres[i + 1]
            eliminados += 1
        else:
            i += 1

    print(f"\n[DEPURACIÓN AUTOMÁTICA] Se eliminaron {eliminados} postre(s) repetido(s) de la estructura POSTRES.")


if __name__ == "__main__":
    sistema = menu()

    print("\n--- ESTADO DE LA ESTRUCTURA ANTES DEL SUBPROGRAMA ---")
    sistema.mostrar_estructura_completa()

    eliminar_postres_repetidos(sistema.postres)

    print("--- ESTADO DE LA ESTRUCTURA DESPUÉS DEL SUBPROGRAMA ---")
    sistema.mostrar_estructura_completa()