def precio_final(precio, descuento=10):
    return precio * (1 - descuento / 100)

print(precio_final(50))
print(precio_final(50, descuento=20))
