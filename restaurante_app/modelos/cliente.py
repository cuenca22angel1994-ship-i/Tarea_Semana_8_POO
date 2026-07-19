class Cliente:
    """
    Representa un cliente registrado del restaurante.
    Principio SRP: Únicamente gestiona los datos de un cliente.
    """

    def __init__(self, identificacion: str, nombre: str, correo: str) -> None:
        self._identificacion = identificacion
        self._nombre = nombre
        self._correo = correo

    @property
    def identificacion(self) -> str:
        return self._identificacion

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def correo(self) -> str:
        return self._correo

    def mostrar_informacion(self) -> str:
        """Devuelve los datos completos del cliente."""
        return (
            f"Identificación: {self.identificacion} | "
            f"Nombre: {self.nombre} | "
            f"Correo: {self.correo}"
        )