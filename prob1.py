"""
Dado un arreglo de números donde cada elemento se repite exactamente dos veces, 
excepto  uno  que  aparece  solo  una  vez,  implemente  una  función  que  encuentre  y 
retorne ese número único. 
• Ejemplo: Entrada: [4, 1, 2, 1, 2] -> Salida: 4. """

lista=[4, 1, 2, 1, 2]
for numero in lista:
    if lista.count(numero)>1:
        continue
    else:
        break
print(numero)


