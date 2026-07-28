edad = 15
tiene_permiso = True

if edad >= 18 and tiene_permiso:
    print("Acceso completo")
elif edad >= 16 and tiene_permiso:
    print("Acceso con acompañante")
elif tiene_permiso:
    print("Acceso solo en horario diurno")
else:
    print("Acceso denegado")