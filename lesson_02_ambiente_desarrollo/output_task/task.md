¡Excelente! Ya tienes Python instalado y un IDE funcionando. Ahora vamos a
comprobarlo con un pequeño programa.

### Ejercicio

El módulo estándar `sys` de Python trae información útil sobre el intérprete
que está ejecutando tu código. En particular, `sys.version_info` es una
**tupla** con los componentes de la versión (mayor, menor, micro, etc.).

Escribí un programa en `main.py` que:

1. **Importe** el módulo `sys`.
2. **Imprima** la información de versión usando `print(sys.version_info)`.

El programa **no lee ninguna entrada del usuario** (`stdin` queda vacío).

### Ejemplo de ejecución

Si tu versión de Python es 3.12.4, el programa debería imprimir algo como:

```
sys.version_info(major=3, minor=12, micro=4, releaselevel='final', serial=0)
```

> 💡 **Tip**: si ya hiciste `python --version` en la terminal y te mostró
> `Python 3.12.4`, ¡eso coincide con lo que vas a ver aquí! La diferencia es
> que la terminal usa el comando externo, mientras que tu programa accede a la
> misma información desde adentro del propio intérprete.