from modelos.producto import Producto

class Bebida(Producto):
    """
    Clase que representa una bebida, especialización de Producto.
    Principio OCP: Amplía el sistema sin modificar la clase base Producto.
    Principio LSP: Se puede usar en cualquier lugar donde se espere un Producto.
    """

    def __init__(
        self,
        codigo: str,
        nombre: str,
        categoria: str,
        precio: float,
        tamaño: str,
        tipo_envase: str
    ) -> None:
        super().__init__(codigo, nombre, categoria, precio)
        self._tamaño = tamaño
        self._tipo_envase = tipo_envase

    @property
    def tamaño(self) -> str:
        return self._tamaño

    @property
    def tipo_envase(self) -> str:
        return self._tipo_envase

    def mostrar_informacion(self) -> str:
        """Devuelve información específica de la bebida (polimorfismo)."""
        return (
            f"[Bebida] Código: {self.codigo} | "
            f"Nombre: {self.nombre} | "
            f"Categoría: {self.categoria} | "
            f"Precio: ${self.precio:.2f} | "
            f"Tamaño: {self.tamaño} | "
            f"Envase: {self.tipo_envase}"
        )