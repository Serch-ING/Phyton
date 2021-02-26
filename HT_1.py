puntos = float(input("\nIngrese el número de niveles para la piramide de * (Asteriscos) \n"))
cadena="*"
print("\n")

i=0

while i < puntos:
    print(cadena)
    cadena+="*"
    i+=1


puntos=int(input("\nIngrese un numero entero positivo: "))
contador=0
if puntos > 1:
    for i in range(2, puntos):
        n=puntos%i
        if n==0:
            contador+=1
    if contador== 0:
        print("El numero ", puntos ," es primo")
    else:
        print("El numero " , puntos ,  " no es primo")
else:
    print("No es un numero primo")

