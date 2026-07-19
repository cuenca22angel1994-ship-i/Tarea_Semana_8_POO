# Sistema de Gestión de Restaurante
**Estudiante:** Angel Rafael Cuenca Tamayo
**Asignatura:** Programación Orientada a Objetos - Semana 8

---

##  Descripción
Aplicación modular en Python para administrar productos, bebidas y clientes de un restaurante, desarrollada aplicando los principios SOLID de diseño orientado a objetos.

---

##  Estructura del proyecto
 
 
restaurante_app/
├── modelos/          # Clases que representan las entidades del sistema
│   ├── producto.py   # Clase base para todos los productos
│   ├── bebida.py     # Clase hija especializada en bebidas
│   └── cliente.py    # Clase para clientes registrados
├── servicios/        # Lógica de negocio y administración
│   └── restaurante.py # Servicio principal del sistema
└── main.py           # Interacción con el usuario y menú
  
---

##  Relaciones entre clases
- **Producto ↔ Bebida**: Relación de herencia válida: *"Una bebida ES UN tipo de producto"*. La clase Bebida hereda todos los atributos y métodos de Producto, y agrega características propias.
- **Producto ↔ Cliente**: No existe relación de herencia, ya que representan conceptos totalmente diferentes.

---

##  Principios SOLID aplicados
### 1. Principio de Responsabilidad Única (SRP)
- Cada clase tiene una única función:
  - `Producto` y `Bebida`: Gestionan solo sus propios datos.
  - `Cliente`: Representa únicamente la información de un usuario.
  - `Restaurante`: Administra las colecciones y reglas de registro.
  - `main.py`: Solo se encarga de la interacción por consola.

### 2. Principio Abierto/Cerrado (OCP)
- El sistema está **abierto para ampliarse**: Se agregó la clase `Bebida` sin modificar el código existente de `Producto` ni de `Restaurante`.
- Está **cerrado para modificaciones**: No es necesario reescribir lógica general para agregar nuevos tipos de productos.

### 3. Principio de Sustitución de Liskov (LSP)
- Un objeto `Bebida` se puede usar en cualquier lugar donde se espere un `Producto`:
  - Ambos se almacenan en la misma lista de productos.
  - El método `mostrar_informacion()` funciona igual para ambos sin errores.
  - No se altera el comportamiento esperado al sustituir la clase base por la derivada.

---
 
 **Reflexión**
 
Diseñar proyectos con responsabilidades claras y principios SOLID hace que el código sea más fácil de entender, modificar y corregir. Si en el futuro necesitamos agregar nuevos tipos de productos (por ejemplo,  Postre  o  PlatoEspecial ), solo debemos crear una nueva clase hija sin alterar el funcionamiento del sistema completo, reduciendo errores y tiempo de desarrollo.
 
