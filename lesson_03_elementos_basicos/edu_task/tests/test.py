import unittest
from main import contar_palabras_reservadas


class TestCase(unittest.TestCase):

    def test_sin_palabras_reservadas(self):
        # Ninguna de estas lineas contiene una keyword de Python
        lineas = ["Hola mundo", "Esto es solo texto", "123 456"]
        self.assertEqual(
            0,
            contar_palabras_reservadas(lineas),
            msg="Sin keywords, deberia devolver 0",
        )

    def test_palabras_reservadas_simples(self):
        # 'for' aparece en la primera linea, 'in' tambien
        lineas = ["for i in range(10):"]
        self.assertEqual(
            2,
            contar_palabras_reservadas(lineas),
            msg="'for' e 'in' deberian contarse como 2 keywords",
        )

    def test_multiples_lineas(self):
        lineas = [
            "if x > 0 and y < 10:",
            "return resultado",
            "print('no hay keywords aca')",
            "while contador < 100:",
        ]
        # 'if', 'and', 'return', 'while' = 4
        self.assertEqual(
            4,
            contar_palabras_reservadas(lineas),
            msg="Deberia contar if, and, return y while",
        )

    def test_repeated_keyword_se_cuenta_varias_veces(self):
        # 'for' aparece 2 veces en total
        lineas = [
            "for i in range(3):",
            "for j in range(3):",
        ]
        self.assertEqual(
            4,
            contar_palabras_reservadas(lineas),
            msg="'for' aparece 2 veces, 'in' aparece 2 veces = 4",
        )

    def test_identificadores_con_keywords_adentro_no_cuentan(self):
        # 'for' dentro de 'formato' NO debe contar como keyword
        # 'in' dentro de 'informacion' NO debe contar como keyword
        # 'if' dentro de 'calificacion_final' NO debe contar como keyword
        # 'or' dentro de 'reporte' NO debe contar como keyword
        lineas = ["El formato es importante para la revision",
                 "calificacion_final = 95",
                 "reporte_notas = [80, 90, 75]"]
        self.assertEqual(
            0,
            contar_palabras_reservadas(lineas),
            msg="Substrings dentro de otras palabras no cuentan",
        )

    def test_lista_vacia(self):
        self.assertEqual(
            0,
            contar_palabras_reservadas([]),
            msg="Una lista vacia debe devolver 0",
        )
