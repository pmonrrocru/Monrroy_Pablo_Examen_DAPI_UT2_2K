def price(Mes1, Mes2, Mes3):
    """Funcion que calcula el precio mediante una fórmula

    Parámetros:
        - Mes1: El consumo del cliente el primer mes.
        - Mes2: El consumo del cliente el segundo mes.
        - Mes3: El consumo del cliente el tercer mes.
    Salida:
        Una variable con el precio.
    """
    Mes1 = input(float("Introduce el consumo del mes 1: "))
    Mes2 = input(float("Introduce el consumo del mes 2: "))
    Mes3 = input(float("Introduce el consumo del mes 3: "))
    precio = ((Mes1 + Mes2 + Mes3) * 0,0615)
    return precio



def gas2price(lista):
    """Función que convierte una lista de consumos en una lista de precios

    Parámetros:
        - lista: Es una lista con tuplas de 3 elementos dentro.
    Salida:
        Lista de precios a pagar por cada cliente
    """
    lista = [(Mes1:c1, Mes2:c1, Mes3:c1)]
    for i in range(len(lista), 0, -1):
        return(lista[i] * price())
