from pizza_funciones import *

while True:
    limpiar()
    mostrar_menu()
    try:
        op = int(input("Ingrese opción: "))
    except ValueError:
        print("\nERROR: debe ingresar un número válido.\n")
        time.sleep(2)
        continue
    limpiar()
    if op == 1:
        registrar_pizza()
    elif op == 2:
        ver_catalogo()
    elif op == 3:
        realizar_pedido()
    elif op == 4:
        ver_pedidos()
    elif op == 5:
        salir()
        break
    else:
        print("\nERROR: opción fuera de rango (1-5).\n")
        time.sleep(2)
