class Pila:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return len(self.items) == 0

    def apilar(self, dato):
        self.items.append(dato)

    def desapilar(self):
        if not self.esta_vacia():
            return self.items.pop()
        return None
        
    def limpiar(self):
        self.items = []
        
    def mostrar_historial(self):
        return self.items

def simulador_navegador():
    historial = Pila()
    pagina_actual = "Inicio"
    
    while True:
        print("\n" + "="*30)
        print(f"ESTÁS EN: {pagina_actual}")
        print("="*30)
        print("1. Visitar nueva página")
        print("2. Ir atrás (Regresar)")
        print("3. Ver historial")
        print("4. Limpiar historial")
        print("5. Salir del navegador")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            nueva_pagina = input("Ingresa la URL (ej. youtube.com): ")
            historial.apilar(pagina_actual)
            pagina_actual = nueva_pagina
            print(f"Cargando {pagina_actual}...")
            
        elif opcion == '2':
            if not historial.esta_vacia():
                pagina_actual = historial.desapilar()
                print("Regresando...")
            else:
                print("No hay más páginas en el historial para regresar.")
                
        elif opcion == '3':
            print("\n--- Historial de navegación ---")
            if historial.esta_vacia():
                print("El historial está vacío.")
            else:

                paginas = historial.mostrar_historial()
                for i, pagina in enumerate(reversed(paginas), 1):
                    print(f"{i}. {pagina}")
                    
        elif opcion == '4':
            historial.limpiar()
            print("El historial ha sido borrado exitosamente.")
            
        elif opcion == '5':
            print("Cerrando navegador...")
            break
            
        else:
            print("Opción inválida, por favor intenta de nuevo.")

if __name__ == "__main__":
    simulador_navegador()