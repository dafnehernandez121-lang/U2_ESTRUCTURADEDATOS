class Nodo:
    def __init__(self, dato):
        self.info = dato
        self.liga = None


class ListaSimplementeLigada:
    def __init__(self):
        self.p = None


    def insertar_al_inicio(self, dato):
        q = Nodo(dato)
        q.liga = self.p
        self.p = q


    def insertar_al_final(self, dato):
        q = Nodo(dato)
        if self.p is None:
            self.p = q
        else:
            actual = self.p
            visitados = set()
            while actual.liga is not None and actual.liga not in visitados:
                visitados.add(actual)
                actual = actual.liga
            actual.liga = q


    def insertar_antes_de(self, x, dato):
        if self.p is None:
            print("La lista está vacía.")
            return

        if self.p.info == x:
            self.insertar_al_inicio(dato)
            return

        anterior = self.p
        actual = self.p.liga
        visitados = {anterior}
        while actual is not None and actual.info != x and actual not in visitados:
            visitados.add(actual)
            anterior = actual
            actual = actual.liga

        if actual is None or actual.info != x:
            print(f"No se encontró el nodo con la información '{x}'.")
        else:
            q = Nodo(dato)
            q.liga = actual
            anterior.liga = q


    def insertar_despues_de(self, x, dato):
        actual = self.p
        visitados = set()
        while actual is not None and actual.info != x and actual not in visitados:
            visitados.add(actual)
            actual = actual.liga

        if actual is None or actual.info != x:
            print(f"No se encontró el nodo con la información '{x}'.")
        else:
            q = Nodo(dato)
            q.liga = actual.liga
            actual.liga = q


    def apuntar_a_mismo_nodo(self, dato_origen, dato_destino):
        nodo_origen = None
        nodo_destino = None
        
        actual = self.p
        visitados = set()
        
        while actual is not None and actual not in visitados:
            visitados.add(actual)
            if actual.info == dato_origen:
                nodo_origen = actual
            if actual.info == dato_destino:
                nodo_destino = actual
            actual = actual.liga

        if nodo_origen is None:
            print(f"Error: No se encontró el nodo origen '{dato_origen}'.")
            return
        if nodo_destino is None:
            print(f"Error: No se encontró el nodo destino '{dato_destino}'.")
            return

        nodo_origen.liga = nodo_destino
        print(f"\n¡Enlace exitoso! Ahora '{dato_origen}' apunta directamente a '{dato_destino}'.")
        print(f"(Cualquier otro nodo que antes apuntara a '{dato_destino}' lo sigue haciendo).")


    def todos_apuntan_a_uno(self, dato_destino):
        if self.p is None:
            print("La lista está vacía.")
            return

        nodos = []
        actual = self.p
        visitados = set()
        nodo_destino = None

        while actual is not None and actual not in visitados:
            visitados.add(actual)
            nodos.append(actual)
            if actual.info == dato_destino:
                nodo_destino = actual
            actual = actual.liga

        if nodo_destino is None:
            print(f"Error: No se encontró el nodo destino '{dato_destino}'.")
            return


        for nodo in nodos:
            if nodo != nodo_destino:
                nodo.liga = nodo_destino
            else:
                nodo.liga = None

        print(f"\n¡Éxito! Todos los nodos ahora apuntan directamente a '{dato_destino}'.")
        print("Estado individual de cada nodo en memoria:")
        for nodo in nodos:
            destino_str = nodo.liga.info if nodo.liga is not None else "NIL"
            print(f"  Nodo [{nodo.info}] ---> {destino_str}")

    def mostrar(self):
        actual = self.p
        elementos = []
        visitados = set()

        while actual is not None:
            if actual in visitados:
                elementos.append(f"[CICLO -> vuelve a '{actual.info}']")
                break
            visitados.add(actual)
            elementos.append(str(actual.info))
            actual = actual.liga
        else:
            elementos.append("NIL")
            
        print(" -> ".join(elementos))



if __name__ == "__main__":

    datos = []
    cantidad = int(input("¿Cuántos datos iniciales deseas ingresar a la lista?: "))
    
    for i in range(cantidad):
        dato = input(f"Ingresa el dato #{i + 1}: ").strip()
        datos.append(dato)


    print("\n--- Creación de lista insertando al inicio (Figura 5.3) ---")
    lista_inversa = ListaSimplementeLigada()
    for nombre in datos:
        lista_inversa.insertar_al_inicio(nombre)
        print(f"Luego de insertar a '{nombre}':")
        lista_inversa.mostrar()


    print("\n--- Creación de lista insertando al final (orden original) ---")
    lista = ListaSimplementeLigada()
    for nombre in datos:
        lista.insertar_al_final(nombre)
    lista.mostrar()

    while True:
        print("\n--- Opciones para manipular la lista ordenada ---")
        print("1. Insertar un nodo al inicio")
        print("2. Insertar un nodo al final")
        print("3. Insertar un nodo antes de X")
        print("4. Insertar un nodo después de X")
        print("5. Hacer que un nodo apunte a otro (2 nodos apuntando al mismo)")
        print("6. Hacer que TODOS los nodos apunten a uno solo")
        print("7. Salir")
        
        opcion = input("Selecciona una opción (1-7): ").strip()
        
        if opcion == "1":
            nuevo = input("Ingresa el nuevo dato a insertar al inicio: ").strip()
            lista.insertar_al_inicio(nuevo)
            lista.mostrar()
            
        elif opcion == "2":
            nuevo = input("Ingresa el nuevo dato a insertar al final: ").strip()
            lista.insertar_al_final(nuevo)
            lista.mostrar()
            
        elif opcion == "3":
            x = input("Ingresa el dato de referencia (X): ").strip()
            nuevo = input(f"Ingresa el nuevo dato a insertar ANTES de '{x}': ").strip()
            lista.insertar_antes_de(x, nuevo)
            lista.mostrar()
            
        elif opcion == "4":
            x = input("Ingresa el dato de referencia (X): ").strip()
            nuevo = input(f"Ingresa el nuevo dato a insertar DESPUÉS de '{x}': ").strip()
            lista.insertar_despues_de(x, nuevo)
            lista.mostrar()

        elif opcion == "5":
            print("\nNota: Si haces que el último nodo apunte a uno intermedio, ambos apuntarán al mismo nodo.")
            origen = input("Ingresa el dato del nodo que cambiará su flecha (origen): ").strip()
            destino = input("Ingresa el dato del nodo al que quieres que apunte (destino): ").strip()
            lista.apuntar_a_mismo_nodo(origen, destino)
            lista.mostrar()

        elif opcion == "6":
            destino = input("Ingresa el dato del nodo al que TODOS van a apuntar: ").strip()
            lista.todos_apuntan_a_uno(destino)
            print("\nRecorrido iniciando desde P (cabeza de la lista):")
            lista.mostrar()
            
        elif opcion == "7":
            print("Programa finalizado.")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")
