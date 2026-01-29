"""
Dada una lista de números, mueva todos los ceros al final de la misma sin cambiar el 
orden relativo de los demás elementos. 
• Ejemplo: Entrada: [0, 1, 0, 3, 12] -> Salida: [1, 3, 12, 0, 0].  """

# aqui se hace mas que nada un algoritmo a fuerza bruta
lista=[0, 1, 0, 3, 12]
for numero in lista:
    if numero==0:
        if lista.count(0)>1:
            lista.remove(0)
            lista.append(0)
        else:
            lista.remove(0)
            lista.append(0)
print(lista)