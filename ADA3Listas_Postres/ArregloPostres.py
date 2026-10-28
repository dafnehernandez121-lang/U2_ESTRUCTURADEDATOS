class NodoIngrediente:
    def __init__(self, ingrediente):
        self.ingrediente = ingrediente.strip()
        self.siguiente = None


class ElementoPostre:
    def __init__(self, nombre):
        self.nombre = nombre.strip().capitalize()
        self.lista_ingredientes = None


class SistemaPostres:
    def __init__(self):
        self.postres = []

    def _obtener_indices_postre(self, nombre):
        nombre_normalizado = nombre.strip().capitalize()
        indices = []
        for i, postre in enumerate(self.postres):
            if postre.nombre == nombre_normalizado:
                indices.append(i)
        return indices

    def _obtener_cadena_ingredientes(self, postre):
        actual = postre.lista_ingredientes
        if actual is None:
            return "NIL (Sin ingredientes)"
        ingredientes = []
        while actual is not None:
            ingredientes.append(actual.ingrediente)
            actual = actual.siguiente
        return " -> ".join(ingredientes) + " -> NIL"

    def imprimir_ingredientes(self, nombre_postre):
        indices = self._obtener_indices_postre(nombre_postre)
        if not indices:
            print(f"\n[ERROR] El postre '{nombre_postre}' no se encuentra en el arreglo.")
            return

        if len(indices) > 1:
            print(f"\n[ADVERTENCIA] Se encontraron {len(indices)} postres duplicados con el nombre '{nombre_postre}'.")
            print("Mostrando la lista de ingredientes de cada uno de ellos:")
            for idx in indices:
                postre = self.postres[idx]
                print(f"  - Registro #{idx + 1} (Índice [{idx}]): {self._obtener_cadena_ingredientes(postre)}")
        else:
            postre = self.postres[indices[0]]
            print(f"\nIngredientes de '{postre.nombre}': {self._obtener_cadena_ingredientes(postre)}")

    def insertar_ingrediente(self, nombre_postre, nuevo_ingrediente):
        indices = self._obtener_indices_postre(nombre_postre)
        if not indices:
            print(f"\n[ERROR] No se puede insertar: el postre '{nombre_postre}' no existe.")
            return False

        if len(indices) > 1:
            print(f"\n[ADVERTENCIA] Se encontraron {len(indices)} postres duplicados con el nombre '{nombre_postre}'.")
            print(f"El ingrediente '{nuevo_ingrediente}' se agregará a todos los postres con ese nombre.")
            print("Estado previo:")
            for idx in indices:
                print(f"  - Registro #{idx + 1} (Índice [{idx}]): {self._obtener_cadena_ingredientes(self.postres[idx])}")

        ingrediente_limpio = nuevo_ingrediente.strip().lower()

        for idx in indices:
            postre = self.postres[idx]
            actual = postre.lista_ingredientes
            ya_existe = False
            while actual is not None:
                if actual.ingrediente.lower() == ingrediente_limpio:
                    ya_existe = True
                    break
                actual = actual.siguiente

            if ya_existe:
                print(f"\n[AVISO] En el registro #{idx + 1} (Índice [{idx}]), el ingrediente '{nuevo_ingrediente}' ya existía.")
            else:
                nuevo_nodo = NodoIngrediente(nuevo_ingrediente)
                if postre.lista_ingredientes is None:
                    postre.lista_ingredientes = nuevo_nodo
                else:
                    actual = postre.lista_ingredientes
                    while actual.siguiente is not None:
                        actual = actual.siguiente
                    actual.siguiente = nuevo_nodo
                print(f"[ÉXITO] Ingrediente '{nuevo_ingrediente}' agregado al registro #{idx + 1} (Índice [{idx}]).")
                print(f"  -> Nueva lista: {self._obtener_cadena_ingredientes(postre)}")

        return True

    def eliminar_ingrediente(self, nombre_postre, ingrediente_a_eliminar):
        indices = self._obtener_indices_postre(nombre_postre)
        if not indices:
            print(f"\n[ERROR] Postre '{nombre_postre}' no encontrado.")
            return False

        if len(indices) > 1:
            print(f"\n[ADVERTENCIA] Se encontraron {len(indices)} postres duplicados con el nombre '{nombre_postre}'.")
            print(f"Se buscará y eliminará '{ingrediente_a_eliminar}' en cada una de sus listas.")
            print("Estado previo:")
            for idx in indices:
                print(f"  - Registro #{idx + 1} (Índice [{idx}]): {self._obtener_cadena_ingredientes(self.postres[idx])}")

        ingrediente_limpio = ingrediente_a_eliminar.strip().lower()

        for idx in indices:
            postre = self.postres[idx]
            actual = postre.lista_ingredientes
            previo = None

            if actual is None:
                print(f"\n[ERROR] El registro #{idx + 1} (Índice [{idx}]) no tiene ingredientes registrados.")
                continue

            while actual is not None and actual.ingrediente.lower() != ingrediente_limpio:
                previo = actual
                actual = actual.siguiente

            if actual is None:
                print(f"\n[ERROR] El ingrediente '{ingrediente_a_eliminar}' no se encontró en el registro #{idx + 1} (Índice [{idx}]).")
            else:
                if previo is None:
                    postre.lista_ingredientes = actual.siguiente
                else:
                    previo.siguiente = actual.siguiente
                print(f"\n[ÉXITO] Ingrediente '{ingrediente_a_eliminar}' eliminado del registro #{idx + 1} (Índice [{idx}]).")
                print(f"  -> Lista restante: {self._obtener_cadena_ingredientes(postre)}")

        return True

    def dar_de_alta_postre(self, nombre_postre, lista_ingredientes):
        indices = self._obtener_indices_postre(nombre_postre)
        if indices:
            print(f"\n[ADVERTENCIA] El postre '{nombre_postre}' ya existe previamente en la(s) posición(es) {indices}.")
            print("Se procederá a dar de alta de todas formas como registro duplicado.")

        nuevo_postre = ElementoPostre(nombre_postre)
        
        cabeza = None
        ultimo = None
        for ing in lista_ingredientes:
            texto = ing.strip()
            if texto:
                nuevo_nodo = NodoIngrediente(texto)
                if cabeza is None:
                    cabeza = nuevo_nodo
                    ultimo = nuevo_nodo
                else:
                    ultimo.siguiente = nuevo_nodo
                    ultimo = nuevo_nodo

        nuevo_postre.lista_ingredientes = cabeza

        pos = 0
        while pos < len(self.postres) and self.postres[pos].nombre <= nuevo_postre.nombre:
            pos += 1
        
        self.postres.insert(pos, nuevo_postre)
        print(f"[ÉXITO] Postre '{nuevo_postre.nombre}' agregado en la posición {pos}.")
        return True

    def dar_de_baja_postre(self, nombre_postre):
        indices = self._obtener_indices_postre(nombre_postre)
        if not indices:
            print(f"\n[ERROR] No se puede dar de baja: el postre '{nombre_postre}' no existe.")
            return False

        if len(indices) > 1:
            print(f"\n[ADVERTENCIA] Se encontraron {len(indices)} postres duplicados con el nombre '{nombre_postre}'.")
            print("Listas de ingredientes que se darán de baja junto con cada postre:")
            for idx in indices:
                print(f"  - Registro #{idx + 1} (Índice [{idx}]): {self._obtener_cadena_ingredientes(self.postres[idx])}")
            print(f"Dando de baja todos los {len(indices)} registros duplicados...")

        for idx in reversed(indices):
            postre_a_eliminar = self.postres[idx]
            actual = postre_a_eliminar.lista_ingredientes
            while actual is not None:
                siguiente = actual.siguiente
                actual.siguiente = None
                actual = siguiente
            postre_a_eliminar.lista_ingredientes = None
            del self.postres[idx]
            print(f"  [ÉXITO] Postre '{nombre_postre}' en la posición {idx} y su lista fueron eliminados.")

        return True

    def mostrar_estructura_completa(self):
        print("\n================== ESTRUCTURA POSTRES ==================")
        if not self.postres:
            print("  (El arreglo está vacío)")
        else:
            for i, p in enumerate(self.postres):
                cadena = self._obtener_cadena_ingredientes(p)
                print(f"  [{i}] {p.nombre.ljust(15)} | Head -> {cadena}")
        print("========================================================\n")


def menu():
    sistema = SistemaPostres()

    while True:
        print("""
------------------ MENÚ DE OPCIONES (EJERCICIO 1) ------------------
1. Mostrar toda la estructura
2. Dar de alta un postre con sus ingredientes
3. Imprimir ingredientes de un postre
4. Insertar un ingrediente a un postre existente
5. Eliminar un ingrediente de un postre
6. Dar de baja un postre con todos sus ingredientes
7. Salir
--------------------------------------------------------------------""")
        opcion = input("Seleccione una opción (1-7): ").strip()

        if opcion == "1":
            sistema.mostrar_estructura_completa()

        elif opcion == "2":
            nombre = input("Ingrese el nombre del postre: ").strip()
            if not nombre:
                print("[ERROR] El nombre no puede estar vacío.")
                continue
            cadena_ingredientes = input("Ingrese los ingredientes separados por coma (ej. Leche, Azúcar, Huevo): ")
            ingredientes = [item.strip() for item in cadena_ingredientes.split(",") if item.strip()]
            sistema.dar_de_alta_postre(nombre, ingredientes)

        elif opcion == "3":
            nombre = input("Nombre del postre a consultar: ").strip()
            sistema.imprimir_ingredientes(nombre)

        elif opcion == "4":
            nombre = input("Nombre del postre: ").strip()
            ingrediente = input("Nuevo ingrediente a agregar: ").strip()
            if ingrediente:
                sistema.insertar_ingrediente(nombre, ingrediente)
            else:
                print("[ERROR] El ingrediente no puede estar vacío.")

        elif opcion == "5":
            nombre = input("Nombre del postre: ").strip()
            ingrediente = input("Ingrediente que desea eliminar: ").strip()
            if ingrediente:
                sistema.eliminar_ingrediente(nombre, ingrediente)
            else:
                print("[ERROR] Debe indicar el ingrediente.")

        elif opcion == "6":
            nombre = input("Nombre del postre que desea dar de baja: ").strip()
            sistema.dar_de_baja_postre(nombre)

        elif opcion == "7":
            print("\nSaliendo del menú...")
            return sistema

        else:
            print("\n[ERROR] Opción no válida. Ingrese un número del 1 al 7.")


if __name__ == "__main__":
    menu()