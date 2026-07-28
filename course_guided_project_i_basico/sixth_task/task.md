# Paso 6: integrar todo

En este paso final vas a **integrar todos los pasos anteriores** en una sola aplicacion.

## Objetivo

Implementa `main()` que:

1. Pide el nombre (con validacion del paso 5)
2. Pide la edad (con validacion del paso 5)
3. Pide el peso (en kg)
4. Pide la altura (en metros)
5. Calcula el IMC (paso 4)
6. Determina la categoria del IMC (paso 4)
7. Muestra una tarjeta completa con todos los datos

## Formato esperado de salida

```
========================================
   TARJETA DE PRESENTACION DEL ESTUDIANTE
========================================
Nombre:           Maria
Edad:             17 anos
Peso:             70.0 kg
Altura:           1.75 m
IMC:              22.86 (normal)
========================================
```

## Pistas

- Importa las funciones de los pasos anteriores: `from third_task.main import leer_nombre, leer_edad` (o reorganiza el codigo como prefieras).
- Usa un bucle principal o llamadas directas segun lo que te resulte mas limpio.
- El test solo verifica que `main()` exista como callable, no valida el output (eso lo probas manualmente corriendo el programa).

## ¿Como probar?

Hace clic en **Check** para verificar que la funcion existe. Luego corre el programa desde la terminal para probar interactivamente.
