# U2_ESTRUCTURADEDATOS
Repositorio de la unidad 2

#Torre Hanoi
El programa tiene dos métodos torre_hanoi(n, origen, auxiliar, destino). Es recursivo y se encarga de simular los movimientos en los discos, también está el main() que define la lista de pruebas que en este caso son (5, 10, 30 y 64 discos), hace los cálculos matemáticos de los movimientos esperados, reinicia el contador y calcula el tiempo.
Respecto a los tiempos de ejecución, esto fue lo que tenía en l terminal:
Discos: 5
Movimientos necesarios: 31
Movimientos realizados: 31
Tiempo de ejecución: 0.000005 segundos

Discos: 10
Movimientos necesarios: 1,023
Movimientos realizados: 1,023
Tiempo de ejecución: 0.000114 segundos

Discos: 30
Movimientos necesarios: 1,073,741,823
Movimientos realizados: 1,073,741,823
Tiempo de ejecución: 80.177215 segundos

Discos: 64
Movimientos necesarios: 18,446,744,073,709,551,615

EN ESTE ÚLTIMO TIENE MUCHOS MOVIMIENTOS POR LO QUE EL PROGRAMA TARDA EN MOSTRAR EL RESULTADO, ESPERÉ COMO UNA HORA Y SEGUÍA SIN MOSTRAR EL TIEMPO, es imposible saber cuánto tiempo se tardaría, aunque lo busqué en Google y me dijo: Tiempo de ejecución: Cientos de miles de millones de años. El programa jamás terminará de ejecutarse; tendrías que detenerlo a la fuerza cerrando la terminal.
En la torre de Hanói cada disco extra multiplica el tiempo y la cantidad de movimientos por dos, también me dí cuenta que es muy complicado para la máquina ejecutar este programa cuando son cantidades grandes de discos.
