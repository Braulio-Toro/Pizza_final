import os, time

lista_pizzas = []
lista_pedidos = []
tipo_masa = ("Delgada", "Tradicional", "Gruesa")

def limpiar():
    os.system("cls" if os.name == "nt" else "clear")

def mostrar_menu():
    print("""--- MENU DE PIZZAS ---
1) Registrar pizzas
2) Ver catalogo de pizzas
3) Realizar pedido
4) Ver pedidos realizados
5) Salir
""")

def registrar_pizza():
    while True:
        try:
            codigo = int(input("Ingrese el código de la pizza: "))
            if codigo > 0:
                if any(x["codigo"] == codigo for x in lista_pizzas):
                    print("El código ya existe. Ingrese un código diferente.")
                    time.sleep(2)
                else:
                    break
            else:
                print("El código debe ser superior a 0")
                time.sleep(2)
        except ValueError:
            print("ERROR! Ingrese un código válido\n")
            time.sleep(2)

    while True:
        nombre = input("Ingrese el nombre de la pizza: ").strip().title()
        if len(nombre) > 3:
            if any(x["nombre"].lower() == nombre.lower() for x in lista_pizzas):
                print("El nombre ya existe. Ingrese un nombre diferente.")
                time.sleep(2)
            else:
                break
        else:
            print("El nombre debe tener como mínimo tres letras\n")
            time.sleep(2)

    while True:
        print("\nTipos de masa disponibles:")
        for i, masa in enumerate(tipo_masa, start=1):
            print(f"{i}) {masa}")
        try:
            masa = int(input("\nSeleccione el tipo de masa (1-2-3): "))
            if 0 < masa < 4:
                break
            else:
                print("ERROR! El número no es válido")
                time.sleep(2)
        except ValueError:
            print("ERROR! El número no es válido\n")
            time.sleep(2)
    masa_pizza = tipo_masa[masa - 1]

    while True:
        try:
            precio = int(input("Ingrese el precio de la pizza: "))
            if precio > 5000:
                break
            else:
                print("El precio debe ser superior a $5.000")
                time.sleep(2)
        except ValueError:
            print("Error! Debe ingresar un valor válido\n")
            time.sleep(2)

    while True:
        try:
            stock = int(input("Ingrese el stock de la pizza: "))
            if stock > 0:
                break
            else:
                print("ERROR! Debes ingresar un valor válido")
        except ValueError:
            print("ERROR! Debes ingresar un valor válido\n")
            time.sleep(2)

    pizza = {
        "codigo": codigo,
        "nombre": nombre,
        "masa": masa_pizza,
        "precio": precio,
        "stock": stock
    }
    lista_pizzas.append(pizza)
    print("Pizza ingresada exitosamente")
    time.sleep(2)

def ver_catalogo():
    if not lista_pizzas:
        print("No hay pizzas registradas.")
        time.sleep(2)
    else:
        print("--- LISTA DE PIZZAS ---\n")
        for x in lista_pizzas:
            for llave in x:
                print(llave, "=>", x[llave])
            print("-" * 30)
        input("\nPresione ENTER para continuar...")

def realizar_pedido():
    if not lista_pizzas:
        print("No hay pizzas registradas.")
        time.sleep(2)
    else:
        while True:
            cliente = input("Ingrese el nombre del cliente: ").strip().title()
            if len(cliente) >= 3:
                break
            else:
                print("El nombre es muy corto.")
                time.sleep(2)

        while True:
            try:
                codigo_pedido = int(input("Ingrese el código de la pizza que desea pedir: "))
                if codigo_pedido > 0:
                    break
                else:
                    print("El código debe ser un número positivo.")
                    time.sleep(2)
            except ValueError:
                print("Error! Ingrese un valor válido.\n")
                time.sleep(2)

        while True:
            try:
                cantidad = int(input("Ingrese la cantidad de pizzas a pedir: "))
                if cantidad > 0:
                    break
                else:
                    print("La cantidad debe ser un número positivo.")
                    time.sleep(2)
            except ValueError:
                print("Error! Ingrese un número válido.\n")
                time.sleep(2)

        found = False
        for x in lista_pizzas:
            if x["codigo"] == codigo_pedido:
                if x["stock"] >= cantidad:
                    x["stock"] -= cantidad
                    print(f"\nPedido realizado exitosamente para {cliente}.")
                    print(f"Cantidad de pizzas: {cantidad}, Total a pagar: {x['precio'] * cantidad}")
                    input("\nPresione ENTER para continuar...")
                    found = True
                    pizzas = {
                        "cliente": cliente,
                        "codigo_pizza": x["codigo"],
                        "nombre_pizza": x["nombre"],
                        "cantidad": cantidad,
                        "total": x["precio"] * cantidad
                    }
                    lista_pedidos.append(pizzas)
                    break
                else:
                    print(f"No hay suficiente stock de la pizza {x['nombre']}. Stock disponible: {x['stock']}")
                    time.sleep(2)
                    found = True
                    break
        if not found:
            print("Pizza no encontrada.")
            time.sleep(2)

def ver_pedidos():
    if not lista_pedidos:
        print("No hay pedidos realizados.")
        time.sleep(2)
    else:
        print("--- PEDIDOS REALIZADOS ---\n")
        for x in lista_pedidos:
            for llave in x:
                print(llave, "=>", x[llave])
            print("-" * 30)
        input("\nPresione ENTER para continuar...")

def salir():
    print("Saliendo del sistema, hasta luego.")
    time.sleep(2)