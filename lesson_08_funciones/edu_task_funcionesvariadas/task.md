# Funciones variadas: círculo y conversión de temperatura

En esta práctica vas a implementar dos funciones independientes, cada una con su propia responsabilidad:

1. **`area_circulo(radio)`** — devuelve el área de un círculo usando la fórmula `π × radio²`. Importá `pi` desde `math` para usar un valor preciso. Un radio negativo debe lanzar `ValueError("El radio no puede ser negativo")`.

2. **`fahrenheit_a_celsius(f)`** — convierte grados Fahrenheit a Celsius con la fórmula `(f - 32) × 5 / 9`. Por ejemplo, `32 °F` equivalen a `0 °C` y `212 °F` a `100 °C`.

Ambas funciones deben estar listas al mismo tiempo: la primera la usan los reportes de geometría y la segunda los paneles climáticos del laboratorio de cómputo de Panamá. Mantén cada `# TODO` en su función y no devuelvas valores fijos: ¡las pruebas usan varios radios y temperaturas!