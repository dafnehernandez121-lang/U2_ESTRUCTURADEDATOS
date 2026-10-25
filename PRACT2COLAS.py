class Order:
    def __init__(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty

    def print_order(self):
        print(f"     Customer: {self.get_customer()}")
        print(f"     Quantity: {self.get_qtty()}")
        print("     ------------")

    def get_qtty(self):
        return self.qtty

    def get_customer(self):
        return self.customer


class Node:
    def __init__(self, info):
        self.info = info  
        self.next = None  


class Queue:
    def __init__(self):
        self.top = None   
        self.tail = None  
        self._size = 0    

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def front(self):
        if self.is_empty():
            return None
        return self.top.info

    def enqueue(self, info):
        new_node = Node(info)
        if self.is_empty():
            self.top = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    def dequeue(self):
        if self.is_empty():
            return None
        
        info_to_return = self.top.info
        self.top = self.top.next
        self._size -= 1
        
        if self.is_empty():
            self.tail = None
            
        return info_to_return

    def print_info(self):
        print("********************************* QUEUE DUMP **********************************")
        print(f"   Size: {self.size()}")
        node = self.top
        count = 1
        while node is not None:
            print(f"   ** Element {count}")
            node.info.print_order()
            node = node.next
            count += 1
        print("*******************************************************************************")

    def get_nth(self, pos):
        if pos < 1 or pos > self.size():
            return None
        
        node = self.top
        for _ in range(1, pos):
            node = node.next
            
        return node.info


if __name__ == "__main__":
    cola = Queue()

    cola.enqueue(Order(20, "cust1"))
    cola.enqueue(Order(30, "cust2"))
    cola.enqueue(Order(40, "cust3"))

    print("\n--------------- Estado de la cola tras insertar 3 pedidos ---------------------")
    cola.print_info()

    print("\n--- Probando método front() ---")
    primer_elemento = cola.front()
    if primer_elemento:
        primer_elemento.print_order()

    print("\n----- Probando método dequeue() (Se prueba extrayendo el primer elemento) -----")
    cola.dequeue()
    cola.print_info()

    print("\n---------------- Añadiendo más elementos para tener 4 en total ---------------- ")
    cola.enqueue(Order(50, "cust4"))
    cola.enqueue(Order(60, "cust5"))
    cola.print_info()

    print("\n-------------------------- Probando método getNth(3) --------------------------")
    tercer_elemento = cola.get_nth(3)
    if tercer_elemento:
        print("El tercer elemento en la cola es:")
        tercer_elemento.print_order()
    else:
        print("Posición no válida.")