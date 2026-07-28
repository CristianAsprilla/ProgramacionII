# Detectar números primos

Un **número primo** es un entero mayor que 1 que solo es divisible por 1 y por sí mismo. Por ejemplo, `2`, `3`, `5` y `7` son primos; `1`, `4` y `6` no lo son.

Implementa dos funciones que se apoyan entre sí:

1. **`es_primo(n)`** — devuelve `True` si `n` es primo y `False` en caso contrario. Una forma eficiente es probar divisores solo hasta la raíz cuadrada de `n`: si encontramos uno, ya no es primo.

2. **`lista_primos(n)`** — devuelve una lista con todos los primos desde `2` hasta `n` (incluido), usando `es_primo` como filtro. Si `n < 2`, devuelve una lista vacía.

La idea es practicar **subrutinas que se llaman entre sí** y se importan desde otros archivos si fuera necesario. Mantén ambas funciones en este mismo módulo por ahora.