def saludar(nombre):
    """Devuelve un saludo personalizado para la persona indicada."""
    return f"Hola, {nombre}!"

# Ejemplo de uso de la funcion
if __name__ == '__main__':
    mensaje = saludar("estudiante")
    print(mensaje)