from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente
from servicios.restaurante import Restaurante


def mostrar_menu() -> None:
    """Muestra el menú principal del sistema."""
    print("\n" + "=" * 40)
    print("        SISTEMA DE RESTAURANTE")
    print("=" * 40)
    print("1. Registrar producto")
    print("2. Registrar bebida")
    print("3. Registrar cliente")
    print("-" * 40)
    print("4. Listar productos")
    print("5. Listar clientes")
    print("-" * 40)
    print("6. Salir")


def registrar_producto(restaurante: Restaurante) -> None:
    """Solicita datos y crea un objeto Producto para registrarlo."""
    print("\n--- REGISTRAR NUEVO PRODUCTO ---")
    codigo = input("Código único: ").strip()
    nombre = input("Nombre del producto: ").strip()
    categoria = input("Categoría (ej: Entrada, Plato fuerte, Postre): ").strip()

    try:
        precio = float(input("Precio unitario: $").strip())
        if precio <= 0:
            print("Error: El precio debe ser mayor a cero.")
            return
    except ValueError:
        print("Error: Ingrese un valor numérico válido para el precio.")
        return

    nuevo_producto = Producto(codigo, nombre, categoria, precio)
    print(restaurante.registrar_producto(nuevo_producto))


def registrar_bebida(restaurante: Restaurante) -> None:
    """Solicita datos y crea un objeto Bebida para registrarlo."""
    print("\n--- REGISTRAR NUEVA BEBIDA ---")
    codigo = input("Código único: ").strip()
    nombre = input("Nombre de la bebida: ").strip()
    categoria = input("Categoría (ej: Caliente, Fría, Sin alcohol): ").strip()

    try:
        precio = float(input("Precio unitario: $").strip())
        if precio <= 0:
            print("Error: El precio debe ser mayor a cero.")
            return
    except ValueError:
        print("Error: Ingrese un valor numérico válido para el precio.")
        return

    tamaño = input("Tamaño/porción (ej: 300ml, 500ml): ").strip()
    tipo_envase = input("Tipo de envase (ej: Botella, Vaso, Lata): ").strip()

    nueva_bebida = Bebida(codigo, nombre, categoria, precio, tamaño, tipo_envase)
    print(restaurante.registrar_producto(nueva_bebida))


def registrar_cliente(restaurante: Restaurante) -> None:
    """Solicita datos y crea un objeto Cliente para registrarlo."""
    print("\n--- REGISTRAR NUEVO CLIENTE ---")
    identificacion = input("Número de identificación: ").strip()
    nombre = input("Nombre completo: ").strip()
    correo = input("Correo electrónico: ").strip()

    nuevo_cliente = Cliente(identificacion, nombre, correo)
    print(restaurante.registrar_cliente(nuevo_cliente))


def listar_productos(restaurante: Restaurante) -> None:
    """Muestra todos los productos y bebidas registrados."""
    print("\n=== LISTA DE PRODUCTOS REGISTRADOS ===")
    lista = restaurante.listar_productos()
    if not lista:
        print("No hay productos registrados en el sistema.")
        return
    for producto in lista:
        print(producto)


def listar_clientes(restaurante: Restaurante) -> None:
    """Muestra todos los clientes registrados."""
    print("\n=== LISTA DE CLIENTES REGISTRADOS ===")
    lista = restaurante.listar_clientes()
    if not lista:
        print("No hay clientes registrados en el sistema.")
        return
    for cliente in lista:
        print(cliente)


def main() -> None:
    """Punto de entrada del programa."""
    sistema = Restaurante()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            registrar_producto(sistema)
        elif opcion == "2":
            registrar_bebida(sistema)
        elif opcion == "3":
            registrar_cliente(sistema)
        elif opcion == "4":
            listar_productos(sistema)
        elif opcion == "5":
            listar_clientes(sistema)
        elif opcion == "6":
            print("\nGracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("\nOpción no válida. Intente nuevamente.")


if __name__ == "__main__":
    main()