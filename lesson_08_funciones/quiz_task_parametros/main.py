def clasificar(edad, es_estudiante=True):
    if edad < 0:
        return "Edad inválida"
    if edad < 12:
        return "Menor" if es_estudiante else "Menor (general)"
    if edad < 18:
        return "Adolescente" if es_estudiante else "Adolescente (general)"
    return "Adulto"


print(clasificar(20))
print(clasificar(16))