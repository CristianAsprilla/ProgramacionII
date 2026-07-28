def agregar_contacto(agenda, nombre, telefono):
    # INICIO DE LA IMPLEMENTACIÓN
    agenda[nombre] = telefono
    # FIN DE LA IMPLEMENTACIÓN


def buscar_contacto(agenda, nombre):
    # INICIO DE LA IMPLEMENTACIÓN
    # TODO: implementa las funciones de la agenda (agregar, eliminar, listar)
    return agenda.get(nombre)
    # FIN DE LA IMPLEMENTACIÓN


def eliminar_contacto(agenda, nombre):
    # INICIO DE LA IMPLEMENTACIÓN
    if nombre in agenda:
        agenda.pop(nombre)
        return True
    return False
    # FIN DE LA IMPLEMENTACIÓN


def listar_contactos(agenda):
    # INICIO DE LA IMPLEMENTACIÓN
    return sorted(agenda.items())
    # FIN DE LA IMPLEMENTACIÓN


if __name__ == "__main__":
    agenda = {}
    agregar_contacto(agenda, "Ana", "6000-1234")
    agregar_contacto(agenda, "Luis", "6000-5678")
    print(listar_contactos(agenda))
