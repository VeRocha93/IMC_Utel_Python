#02 Nov- Inedice de masa corporal
print("******************************************")
print("   Buen día \n Vamos a conocer tu IMC   ")
print("******************************************")

print("\n Favor de anotar los siguientes datos")
Apellido_paterno =input("\n Ingresa Apellido paterno: ")
Apellido_materno =input("Ingresa Apellidod materno: ")
Nombre =input("Ingresa Nombre(s): ")

print("\n ************************************************************************")
print(f"          Bienvenido {Nombre } {Apellido_paterno } {Apellido_materno }    ")
print(" ************************************************************************")


Edad = int(input("\n Ingresa tu edad: "))
Peso = float(input("Ingresa tu peso en Kg: "))
Estatura = float(input("Ingresa tu estatura: "))
Indice_masa_corporal = round(Peso / Estatura**2,2)


print("\n ***********************************************************************")
print(f"      Tu IMC es : {Indice_masa_corporal} a la edad de {Edad} años       ")


# Menor a 18.9   = peso bajo
# 18.50 a 24.99   = peso normal
# 25.00 a 29.99   = sobrepeso
# 30.00 a 34.99   = obesidad leve
# 35.00 a 39.99   = obesidad media
# Mayor a 40.0   = obesidad mórbida

if Indice_masa_corporal >= 1 and Indice_masa_corporal <= 18.9:
    print("     Tienes un peso bajo :( )")

elif Indice_masa_corporal >= 18.50 and Indice_masa_corporal <=24.99:
    print("     Tienes un peso normal :) ")

elif Indice_masa_corporal >= 25.00 and Indice_masa_corporal <=29.99:
    print("     Tienes sobrepeso :/")

elif Indice_masa_corporal >= 30.00 and Indice_masa_corporal <=34.99:
    print("     Tienes obesidad leve :|")

elif Indice_masa_corporal >= 35.00 and Indice_masa_corporal <=39.99:
    print("     Tienes obesidad media :/")

elif Indice_masa_corporal >= 40.00:
    print("     Tienes obesidad mórbida :o)")

else:
    Indice_masa_corporal <=0
    print("ERROR: Ingresaste un dato incorrecto")

with open("registroIMC.txt", "a") as archivo:
    archivo.write('Nombre;')
    archivo.write('Apellido Paterno;')
    archivo.write('Apellido Materno;')
    archivo.write('Edad;')
    archivo.write('Peso;')
    archivo.write('Estatura;')
    archivo.write('IMC; \n')


   
    archivo.write('{};'.format(Nombre))
    archivo.write('{};'.format(Apellido_paterno))
    archivo.write('{};'.format(Apellido_materno))
    archivo.write('{};'.format(Edad))
    archivo.write('{};'.format(Peso))
    archivo.write('{};'.format(Estatura))
    archivo.write('{};'.format(Indice_masa_corporal))
print(" ************************************************************************")

print (f"   \n {Nombre } {Apellido_paterno } {Apellido_materno }Tú registro se gaurdo de forma exitosa")



