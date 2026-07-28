# Quiz de escritorio: recursion (factorial)

## Pregunta

¿Que imprime este codigo?

```python
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))
```

## Pista

`factorial(n) = n * factorial(n-1)`, hasta llegar a `factorial(0) = 1`. `5! = 5 * 4 * 3 * 2 * 1` = ?