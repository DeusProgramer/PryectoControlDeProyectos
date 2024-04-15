"""
Empresa: XYZ Solutions

Descripción de la empresa:
XYZ Solutions es una empresa de desarrollo de software que se especializa en soluciones empresariales personalizadas.
Nuestro enfoque principal es brindar herramientas eficientes y fáciles de usar para optimizar los procesos internos de
las empresas.

Proyecto: Sistema de gestión de proyectos

Descripción del proyecto:
Nuestra empresa XYZ Solutions está buscando desarrollar un sistema de gestión de proyectos interno para mejorar
la eficiencia y organización en la ejecución de nuestros proyectos. El objetivo principal del programa es
proporcionar una plataforma centralizada para el seguimiento y control de proyectos.

Requisitos del programa:

1. Interfaz de usuario:
   - El programa debe tener una interfaz de usuario intuitiva y atractiva, desarrollada utilizando Dear PyGUI.
   - Debe haber una pantalla de inicio de sesión para acceder al sistema, con autenticación de usuarios.

2. Gestión de proyectos:
   - El programa debe permitir crear nuevos proyectos y asignarles un nombre, una descripción y una fecha de inicio y
    finalización estimada.
   - Debe haber una vista general de todos los proyectos en curso, con la capacidad de ordenarlos y filtrarlos
   según diferentes criterios (por ejemplo, estado, fecha, prioridad).
   - Cada proyecto debe tener una página de detalles donde se pueda agregar información adicional, como tareas
   asociadas, archivos adjuntos y comentarios.

3. Gestión de tareas:
   - Dentro de cada proyecto, debe ser posible crear y administrar tareas.
   - Cada tarea debe tener un nombre, una descripción, una fecha de vencimiento y un estado (pendiente,
    en progreso, completada).
   - Debe haber una vista de lista de tareas que muestre todas las tareas pendientes y las asignadas a un usuario
   en particular.

4. Colaboración y comunicación:
   - Los usuarios deben poder comentar en cada proyecto y tarea, lo que facilitará la colaboración entre
    los miembros del equipo.
   - El programa puede incluir notificaciones o alertas para informar sobre actualizaciones o
   cambios en los proyectos y tareas.

5. Seguridad:
   - El acceso al programa debe estar restringido a usuarios autorizados a través de un sistema de autenticación
    y autorización seguro.

Expectativas y consideraciones adicionales:
- El programa debe ser estable, seguro y capaz de manejar una cantidad considerable de proyectos y tareas.
- Es preferible que el código esté bien estructurado, documentado y siga buenas prácticas de programación.
- Si es posible, considera implementar una base de datos para almacenar la información de los proyectos y tareas.
- Si tienes alguna idea adicional o mejora para el sistema de gestión de proyectos, ¡siéntete libre de agregarla!"""
import asyncio
from UsersLogin import LoginSystem


if __name__ == '__main__':
    iniT = LoginSystem()
    asyncio.run(iniT.accionAsyncrona())
