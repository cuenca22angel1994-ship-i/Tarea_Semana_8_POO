from modelos.producto import Producto
from modelos.bebida import Bebida
from modelos.cliente import Cliente

class Restaurante:
    """
    Servicio encargado de administrar productos y clientes.
    Principio SRP: Solo gestiona las colecciones y reglas de negocio del sistema.
    """

    def __init__(self) -> None:
        self._productos: list[Producto] = []
        self._clientes: list[Cliente] = []

    def registrar_producto(self, producto: Producto) -> str:
        """Registra un producto o bebida si su código no existe."""
        if self._buscar_producto_por_codigo(producto.codigo):
            return f"Error: Ya existe un producto con el código {producto.codigo}"
        
        self._productos.append(producto)
        return f"Éxito: Producto '{producto.nombre}' registrado correctamente"

    def registrar_cliente(self, cliente: Cliente) -> str:
        """Registra un cliente si su identificación no existe."""
        if self._buscar_cliente_por_identificacion(cliente.identificacion):
            return f"Error: Ya existe un cliente con la identificación {cliente.identificacion}"
        
        self._clientes.append(cliente)
        return f"Éxito: Cliente '{cliente.nombre}' registrado correctamente"

    def listar_productos(self) -> list[str]:
        """
        Devuelve la información de todos los productos.
        Aplica polimorfismo: Funciona igual para Producto y Bebida.
        """
        return [producto.mostrar_informacion() for producto in self._productos]

    def listar_clientes(self) -> list[str]:
        """Devuelve la información de todos los clientes registrados."""
        return [cliente.mostrar_informacion() for cliente in self._clientes]

    def _buscar_producto_por_codigo(self, codigo: str) -> Producto | None:
        """Método interno para buscar productos por código único."""
        for producto in self._productos:
            if producto.codigo == codigo:
                return producto
        return None

    def _buscar_cliente_por_identificacion(self, identificacion: str) -> Cliente | None:
        """Método interno para buscar clientes por identificación única."""
        for cliente in self._clientes:
            if cliente.identificacion == identificacion:
                return None
        return None