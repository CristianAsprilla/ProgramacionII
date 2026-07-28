# Proyecto Guiado III: Sistema de inventario de la tiendita escolar

¡Último proyecto guiado del curso! En este vas a construir un
**sistema de inventario** para la tiendita de la escuela.

Con este proyecto vas a integrar todo lo aprendido en el tercer trimestre:

- **Arreglos unidimensionales** (listas) para guardar el catálogo.
- **Arreglos bidimensionales** (matrices) para el reporte de ventas por mes.
- **Listas dinámicas** para gestionar el historial de movimientos.
- **Pilas** para el sistema de "deshacer" (undo).
- **Diccionarios** para representar cada producto con sus datos.

## ¿Cómo se verá el programa?

```
========================================
   INVENTARIO - TIENDITA LA SALLE
========================================
1. Agregar producto
2. Buscar producto
3. Actualizar stock
4. Deshacer última operación
5. Ver reporte de ventas
6. Salir
========================================
Elige una opción: 1
Nombre del producto: Cuaderno
Precio: 2.50
Stock inicial: 20
Producto 'Cuaderno' agregado con éxito.
```

## Estructura del proyecto

El proyecto se divide en **cuatro pasos**:

1. **Paso 1**: gestionar el catálogo de productos con un **diccionario** (cada
   producto tiene `nombre`, `precio` y `stock`).
2. **Paso 2**: implementar el **historial de operaciones** con una lista
   dinámica.
3. **Paso 3**: implementar la **función de deshacer (undo)** con una **pila**.
4. **Paso 4**: armar el **reporte de ventas** con una **matriz** y conectar
   todo en el menú principal.

¡Vamos!
