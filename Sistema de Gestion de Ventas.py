class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad

    def __str__(self):
        return f"Producto: {self.nombre}, Precio: ${self.precio}, Cantidad: {self.cantidad}"

class Venta:
    def __init__(self):
        self.productos = []
        self.total = 0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto.precio * producto.cantidad

    def mostrar_productos(self):
        for producto in self.productos:
            print(producto)

    def mostrar_total(self):
        print(f"Total: ${self.total}")

def menu():
    print("Bienvenido al sistema de venta")
    print("1. Agregar producto")
    print("2. Mostrar productos")
    print("3. Mostrar total de venta")
    print("4. Salir")
    opcion = int(input("Ingrese una opción: "))
    return opcion

venta = Venta()

while True:
    opcion = menu()
    if opcion == 1:
        nombre = input("Ingrese el nombre del producto: ")
        precio = float(input("Ingrese el precio del producto: "))
        cantidad = int(input("Ingrese la cantidad de productos: "))
        producto = Producto(nombre, precio, cantidad)
        venta.agregar_producto(producto)
    elif opcion == 2:
        venta.mostrar_productos()
    elif opcion == 3:
        venta.mostrar_total()
    elif opcion == 4:
        print("Gracias por usar el sistema de venta")
        break
    else:
        print("Opción inválida. Intente de nuevo.")
