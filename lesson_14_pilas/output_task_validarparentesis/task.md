# Reto: validar paréntesis balanceados

En programación es muy común encontrar expresiones que mezclan paréntesis `()`, corchetes `[]`
y llaves `{}`. Para que una expresión sea **válida**, cada símbolo de apertura debe tener su
correspondiente símbolo de cierre en el orden correcto.

En este reto vas a leer una expresión desde la entrada estándar y debes imprimir
**`Balanceado`** si todos los símbolos están correctamente emparejados, o
**`No balanceado`** en caso contrario. Ignora cualquier otro carácter que no sea un paréntesis,
corchete o llave.

## Entrada

Una sola línea con una expresión (por ejemplo `([{}])`).

## Salida

Imprime **`Balanceado`** o **`No balanceado`** según corresponda, sin comillas.

## Ejemplos

| Entrada   | Salida           |
|-----------|------------------|
| `([{}])`  | `Balanceado`     |
| `([)]`    | `No balanceado`  |
| `{[()]}`  | `Balanceado`     |
| `(a+b`    | `No balanceado`  |

## Pista

Usa una **pila**: apila los símbolos de apertura y, cuando encuentres un cierre, compara con
el último símbolo apilado. Si coincide, lo desapilas; si no coincide (o la pila está vacía),
la expresión no está balanceada. Al final, la pila debe quedar vacía.