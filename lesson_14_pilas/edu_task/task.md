# Práctica: clase `Pila` y paréntesis balanceados

Crea una clase `Pila` que use una lista interna llamada `elementos`. Debe ofrecer estos
métodos:

- `apilar(elemento)`: agrega un elemento en la cima.
- `desapilar()`: devuelve y elimina el elemento de la cima. Si está vacía, devuelve `None`.
- `cima()`: devuelve el elemento de la cima sin eliminarlo. Si está vacía, devuelve `None`.
- `esta_vacia()`: devuelve `True` cuando no hay elementos y `False` en caso contrario.

También completa `parentesis_balanceados(expresion)`. La función debe usar una pila para
verificar los símbolos `()`, `[]` y `{}`. Ignora los demás caracteres de la expresión. Devuelve
`True` si cada apertura tiene el cierre correcto y no sobran símbolos; de lo contrario, devuelve
`False`.

Ejemplos:

```python
parentesis_balanceados("(a + [b])")  # True
parentesis_balanceados("([)]")        # False
parentesis_balanceados("(")           # False
```

Practica primero las operaciones de la pila y después aplica LIFO al recorrido de la expresión.
