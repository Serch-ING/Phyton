print("Binevenido")
x= str(input("Ingrese su contraseña: "))
y= str(input("Ingrese de nuevo su contraseña: "))

if x == y:
    print("\nLas contraseñas coinciden\n")
else:
    print("\nLas contraseñas no coinciden\n")


print("Bienvenido")
x = str(input("Ingresa tu nombre: "))
y = str(input("Sexo H o M:")) 
if y == "M" or y == "m":
        if x.lower() < "m":
            print("\nUsted se encuentra en el grupo A")
        else:
            print("\nUsted se encuentra en el grupo B")
else:
    if y == "H" or y == "h":
        if x.lower() >"n":
            print("\nUsted se encuentra en el grupo A")
        else:
            print("\nUsted se encuentra en el grupo B")