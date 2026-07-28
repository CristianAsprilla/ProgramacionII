def saludar(nombre: str, saludo: str = "Hola") -> str:
    """Construye un saludo personalizado."""
    return f"{saludo}, {nombre}"

print(saludar("Ana"))
