def main():
 # Ejemplo de variables y constantes
 PI = 3.14159 # constante (convención UPPER_SNAKE_CASE)
 nombre = "Ana" # variable de tipo str
 edad = 17 # variable de tipo int
 promedio = 88.5 # variable de tipo float
 aprobado = promedio >= 71 # variable de tipo bool

 print(f"{nombre} tiene {edad} años.")
 print(f"Su promedio es {promedio} y aprobo: {aprobado}")
 print(f"Valor de PI: {PI}")


if __name__ == '__main__':
 main()