############################################################################################################################################
# Alumno(a): Dafne Marivy Hernandez Cetzal
# Fecha: 12/Octubre/2026
# Matricula: E25081275  Correo institucional: LE25081275@merida.tecnm.mx
############################################################################################################################################
import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Funcionamiento de una Pila")
ventana.geometry("400x500")

pila = []

#nuestra la pila en pantalla
def mostrar_pila():
    lista.delete(0, tk.END)

    for elemento in reversed(pila):
        lista.insert(tk.END, elemento)

    if len(pila) == 0:
        etiqueta.config(text="La pila esta vacia")
    else:
        etiqueta.config(text="Elemento en la cima: " + str(pila[-1]))

#agrega un elemento
def insertar():
    elemento = entrada.get()

    if elemento != "":
        pila.append(elemento)
        entrada.delete(0, tk.END)
        mostrar_pila()
    else:
        messagebox.showwarning("Aviso", "Escriba un elemento, de lo contrario no será posible agregarlo")

def eliminar():
    if len(pila) > 0:
        pila.pop()
        mostrar_pila()
    else:
        messagebox.showwarning("Aviso", "La pila esta vacia")

def limpiar():
    pila.clear()
    mostrar_pila()

titulo = tk.Label(
    ventana,
    text="SIMULADOR DE PILA",
    font=("Arial", 16, "bold")
)
titulo.pack(pady=10)

entrada = tk.Entry(ventana, font=("Arial", 12))
entrada.pack(pady=5)

boton_insertar = tk.Button(
    ventana,
    text="Apilar (Insertar)",
    command=insertar,
    width=20,
    bg="lightgreen"
)
boton_insertar.pack(pady=5)

boton_eliminar = tk.Button(
    ventana,
    text="Desapilar (Eliminar)",
    command=eliminar,
    width=20,
    bg="lightcoral"
)
boton_eliminar.pack(pady=5)

boton_limpiar = tk.Button(
    ventana,
    text="Limpiar pila",
    command=limpiar,
    width=20
)
boton_limpiar.pack(pady=5)

etiqueta = tk.Label(
    ventana,
    text="La pila esta vacia",
    font=("Arial", 11)
)
etiqueta.pack(pady=10)

# Lista donde se muestran los elementos
lista = tk.Listbox(
    ventana,
    font=("Arial", 14),
    width=20,
    height=10,
    justify="center"
)
lista.pack(pady=10)
 
ventana.mainloop()