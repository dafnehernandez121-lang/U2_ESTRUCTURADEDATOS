class Cola:
    def __init__(self):
        self.elementos = []

    def esta_vacia(self):
        return len(self.elementos) == 0

    def encolar(self, dato):
        self.elementos.append(dato)

    def desencolar(self):
        return self.elementos.pop(0) if not self.esta_vacia() else None

    def tamano(self):
        return len(self.elementos)


class SistemaSeguros:
    def __init__(self):
        self.servicios = {1: "Polizas", 2: "Siniestros", 3: "Pagos"}
        self.colas = {s: Cola() for s in self.servicios}
        self.turnos = {s: 0 for s in self.servicios}

    def estado(self):
        resumen = " | ".join(f"[{k}] {v}: {self.colas[k].tamano()} en espera" for k, v in self.servicios.items())
        print(f"\nESTADO ACTUAL -> {resumen}")

    def llegada(self, s):
        if s not in self.colas:
            print("[!] Servicio no valido (1, 2 o 3).")
            return
        self.turnos[s] += 1
        ticket = f"{self.servicios[s][:3].upper()}-{self.turnos[s]:03d}"
        self.colas[s].encolar(ticket)
        print(f">> Turno entregado: [{ticket}] para {self.servicios[s]} (En espera: {self.colas[s].tamano()})")

    def atender(self, s):
        if s not in self.colas:
            print("[!] Servicio no valido (1, 2 o 3).")
            return
        ticket = self.colas[s].desencolar()
        if ticket:
            print(f">> LLAMANDO AL TURNO: *** {ticket} *** a Ventanilla {s} ({self.servicios[s]})")
        else:
            print(f">> No hay clientes en espera para el servicio {s}.")


def main():
    sistema = SistemaSeguros()
    print("=" * 50)
    print("SISTEMA DE TURNOS - SEGUROS")
    print("Servicios: 1: Polizas | 2: Siniestros | 3: Pagos")
    print("Comandos: C <num> (Llegada) | A <num> (Atender) | SALIR")
    print("=" * 50)

    while True:
        sistema.estado()
        entrada = input("\nComando (ej. C 1 o A 2): ").strip().upper()

        if entrada == "SALIR":
            print("Cerrando sistema...")
            break

        partes = entrada.split()
        if len(partes) != 2 or not partes[1].isdigit():
            print("[Error] Ingrese accion y numero de servicio (ej: C 1 o A 2).")
            continue

        accion, servicio = partes[0], int(partes[1])

        if accion == "C":
            sistema.llegada(servicio)
        elif accion == "A":
            sistema.atender(servicio)
        else:
            print("[Error] Use 'C' para llegada o 'A' para atender.")


if __name__ == "__main__":
    main()