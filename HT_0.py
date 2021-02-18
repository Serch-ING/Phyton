# Python 3: 
# Author: Sergie Arizandieta 
# Calculo de IMC

# Pedir los valores -> IMC
altura = input ("\nIngrese su altura en metros(m): ")
peso = input ("\nIngrese su peso en kilogramos(kg): ")

# Mostrar Datos
print("\nDatos ingresados: \nAltura: ", altura, " m \nPeso: ", peso," kg ")

# Cal. IMC
imc = round (float(peso) / float(altura)**2,2)

# Mostrar IMC
print("\nSu indice de masa corporal: ",imc)