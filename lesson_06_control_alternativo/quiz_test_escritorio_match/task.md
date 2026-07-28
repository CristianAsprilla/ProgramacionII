# Quiz de escritorio: match/case

## Pregunta

¿Que imprime este codigo (Python 3.10+)?

```python
comando = 1
match comando:
    case 1:
        print("Uno")
    case 2:
        print("Dos")
    case _:
        print("Otro")
```

## Pista

`match/case` funciona como un switch de otros lenguajes. La variable `comando` vale `1`, asi que entra en `case 1:`.