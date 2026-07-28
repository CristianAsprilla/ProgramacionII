# Ejercicio: prueba de escritorio de paradigmas

En esta actividad vas a "leer" codigo como si fueras el computador, identificar el paradigma y predecir su comportamiento. Esto se llama **prueba de escritorio** y es una habilidad fundamental para programar.

## Objetivo

Implementa `predecir_output(codigo, lenguaje)` que reciba un fragmento de codigo y un lenguaje, y retorne una descripcion de su comportamiento segun el paradigma detectado.

## Como funciona

| Si el codigo contiene... | El paradigma es... |
|--------------------------|--------------------|
| `class`, `self` | POO (orientado a objetos) |
| `lambda`, `map`, `filter` | Funcional |
| `for`, `while`, asignaciones | Imperativo |

## Pistas

- Converti el codigo a minusculas antes de buscar.
- Devuelve strings como "poo", "funcional" o "imperativo".
- Si hay varios paradigmas, prioriza POO > funcional > imperativo.

## ¿Como probar?

Hace clic en **Check** y verifica que los 4 tests pasen.