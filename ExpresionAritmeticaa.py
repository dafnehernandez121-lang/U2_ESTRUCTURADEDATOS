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

def evaluador_expresiones():
    while True:
        print("\n" + "="*30)
        print("EVALUADOR DE EXPRESIONES")
        print("="*30)
        print("1. Evaluar expresión Posfija")
        print("2. Evaluar expresión Prefija")
        print("3. Salir del programa")
        
        opcion = input("Elige una opción: ")
        
        if opcion == '1':
            print("\n Nota: Separa los números y operadores con un espacio.")
            print(" Los signos que puedes usar son:(+) suma, (-) resta, (*) multiplicación Y (/) división")
            exp = input("Ingresa la expresión posfija (ej. 5 3 + 2 *): ")
            print("Calculando...")
            print(f"Resultado: {evaluar_posfija(exp)}")
            
        elif opcion == '2':
            print("\n Nota: Separa los números y operadores con un espacio.")
            print(" Los signos que puedes usar son:(+) suma, (-) resta, (*) multiplicación Y (/) división")
            exp = input("Ingresa la expresión prefija (ej. * + 5 3 2): ")
            print("Calculando...")
            print(f"Resultado: {evaluar_prefija(exp)}")
            
        elif opcion == '3':
            print("Cerrando programa...")
            break
            
        else:
            print("Opción inválida, por favor intenta de nuevo.")

def evaluar_posfija(expresion):
    pila = Pila()
    tokens = expresion.split()
    
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            numero2 = pila.desapilar() 
            numero1 = pila.desapilar()
            
            if numero1 is None or numero2 is None:
                return "Error: Expresión mal formada"
                
            if token == '+':
                resultado = numero1 + numero2
            elif token == '-':
                resultado = numero1 - numero2
            elif token == '*':
                resultado = numero1 * numero2
            elif token == '/':
                resultado = numero1 / numero2
                
            pila.apilar(resultado)
        else:
            pila.apilar(float(token))
            
    return pila.desapilar()

def evaluar_prefija(expresion):
    pila = Pila()
    tokens = expresion.split()[::-1] 
    
    for token in tokens:
        if token in ['+', '-', '*', '/']:
            numero1 = pila.desapilar() 
            numero2 = pila.desapilar()
            
            if numero1 is None or numero2 is None:
                return "Error: Expresión mal formada"
                
            if token == '+':
                resultado = numero1 + numero2
            elif token == '-':
                resultado = numero1 - numero2
            elif token == '*':
                resultado = numero1 * numero2
            elif token == '/':
                resultado = numero1 / numero2
                
            pila.apilar(resultado)
        else:
            pila.apilar(float(token))
            
    return pila.desapilar()

if __name__ == "__main__":
    evaluador_expresiones()