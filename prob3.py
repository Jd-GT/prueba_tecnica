"""
Implemente un método para realizar una compresión básica de cadenas utilizando el 
recuento de caracteres repetidos. Si la cadena "comprimida" no es más pequeña que 
la original, debe devolver la original. 
• Ejemplo: Entrada: aabcccccaaa -> Salida: a2b1c5a3.  """


print("Digita tu cadena a evaluar")
entrada=input()

salida=''
count=0
while count<len(entrada):
    contador=1
    letra=entrada[count]
    j=count+1
    while j<len(entrada) and entrada[j]==letra:
        contador+=1
        j+=1
    salida+=letra+str(contador)
    count=j
if len(salida)>=len(entrada):
    print(entrada)
else:
    print(salida)
