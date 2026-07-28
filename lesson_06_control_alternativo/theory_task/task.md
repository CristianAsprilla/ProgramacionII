# Estructuras de control alternativas

Los programas toman decisiones. En Python, `if` ejecuta un bloque cuando una condición es verdadera; `elif` permite probar alternativas y `else` cubre el resto.

```python
temperatura = 31
if temperatura >= 35:
    print("Alerta de calor")
elif temperatura >= 25:
    print("Día cálido")
else:
    print("Día fresco")
```

## Comparar valores

Usamos `==` (igual), `!=` (distinto), `<`, `>`, `<=` y `>=`. No confundas `==` con `=`, que asigna un valor. Las condiciones se combinan con `and`, `or` y `not`.

## Anidación

Un `if` puede estar dentro de otro. La sangría indica qué instrucciones pertenecen a cada bloque. Evita demasiados niveles: suelen volver difícil la lectura.

```python
tiene_pasaje = True
edad = 16
if tiene_pasaje:
    if edad < 18:
        print("Entrada de estudiante")
```

## Selección con match/case

Desde Python 3.10, `match` compara un valor con varios casos, parecido al *switch* de otros lenguajes. El caso `_` funciona como opción predeterminada.

```python
dia = 1
match dia:
    case 1:
        print("Lunes")
    case 2:
        print("Martes")
    case _:
        print("Otro día")
```

Al terminar podrás elegir la estructura adecuada y construir decisiones claras para situaciones como clasificar notas.
