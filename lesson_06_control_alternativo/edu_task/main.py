def clasificar_nota_colegio(nota: float) -> str:
    """Devuelve el descriptor de una nota del Bachillerato Tecnico de Panama.

    Escala oficial del colegio: 1.0 a 5.0, con 3.0 como minimo aprobatorio.

    Reglas de clasificación:
    - 4.5 <= nota <= 5.0: "Excelente"
    - 4.0 <= nota <  4.5: "Muy bueno"
    - 3.5 <= nota <  4.0: "Bueno"
    - 3.0 <= nota <  3.5: "Mínimo aprobatorio"
    - nota <  3.0       : "Reprobado"

    Si la nota no está en el rango 1.0-5.0, lanzar ValueError con el mensaje
    "La nota debe estar entre 1.0 y 5.0".
    """
    # TODO: implementa la clasificación según la escala del colegio (1.0–5.0)
    pass
