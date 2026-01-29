"""
Se le entrega una lista que contiene $n-1$ números en el rango de $1$ a $n$. No hay 
duplicados. Encuentre el número que falta en la secuencia. 
• Ejemplo: Rango de 1 a 5, lista [1, 2, 4, 5] -> Salida: 3 """


lista=[1,2,4,5]
n=5
for i in range(1,n+1):
    if i not in lista:
        print(i)