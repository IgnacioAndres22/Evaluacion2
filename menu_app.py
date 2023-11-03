# Función para agregar una compra a la lista agregue un try en caso de que se ingrese erronamiente
def agregar_compra(compras):
    while True:
        try:
            monto_compra = float(input("Ingrese el monto de la compra: "))
            if monto_compra >= 0:
                compras.append(monto_compra)
                print("Compra agregada correctamente.")
                break
            else:
                print("Por favor, ingrese un número positivo.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
# Función para mostrar las compras registradas
def mostrar_compras(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        for i in compras:
            print(i)

# Función para mostrar el total gastado
def mostrar_total(compras):
    if not compras:
        print("No hay compras registradas.")
    else:
        total_gastado = sum(compras)
        print(total_gastado)

# Función main
def main():
    compras = []

    while True:
        print("\nMenu:")
        print("1. Agregar compra")
        print("2. Mostrar compras")
        print("3. Mostrar total gastado")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            agregar_compra(compras)
        elif opcion == "2":
            mostrar_compras(compras)
        elif opcion == "3":
            mostrar_total(compras)
        elif opcion == "4":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida")
#llama la funcino main como principal
if __name__ == "__main__":
    main()
