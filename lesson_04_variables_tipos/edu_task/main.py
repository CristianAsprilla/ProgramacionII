def datos_rectangulo(base, altura):
 """
 Recibe la base y la altura de un rectangulo y devuelve un diccionario
 con su area y su perimetro.

 Parametros:
 base (float): la base del rectangulo (en metros).
 altura (float): la altura del rectangulo (en metros).

 Retorna:
 dict: diccionario con claves 'area' y 'perimetro'.
 """
 # calcula el área y el perímetro
 # TODO: calcula el area (base * altura) y perimetro (2 * (base + altura))
 return {"area": 0, "perimetro": 0}


if __name__ == '__main__':
 info = datos_rectangulo(8.5, 4.2)
 print(f"Area: {info['area']} m^2")
 print(f"Perimetro: {info['perimetro']} m")