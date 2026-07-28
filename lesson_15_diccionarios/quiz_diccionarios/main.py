datos = {
    "curso": "Programación II",
    "grado": 11,
    "activo": True,
}

print(datos["curso"])
print(datos.get("docente", "Pendiente"))
print(list(datos.keys()))
