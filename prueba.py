# print("Hola Azeroth")

# # Crendo Variables

# titulo="Clima de hoy" #String
# diaDelMes=13          #Int
# mes=4                 #Int

# temperatura=22.3      #Float
# llueve=False          #boolean

# print(titulo)
# print("Temperatura Actual:", temperatura, "grados")
# print(diaDelMes, "-",mes)

# if llueve:
#     print("Tiene que llevar paraguas")
# else:
#     print("puede llevar polera sin mangas")

#Pedir Password y pin
#Pida al Usuario Password en palabra que debe ser "TEMU"
#ademas pida el pin que debe ser 3435
#los dos deben estar correctos para acceder al sistema

# passw="temu"
# pin=3435
# print("Ingrese su clave")
# input()
# if passw == "temu":
#     print("Clave Correcta")
#     print("Ingrese su Pin")
#     input(int)
#     if pin==3435:
#         print("Pin Correcto")
#     else:
#         print("Pin incorrecto")
# else:
#     print("Clave Incorrecta")

# passw="temu"
# pin=3435

# palabra=input("Ingrese su clave: ")
# code=int(input("Ingrese su Pin: "))

# if code==pin and passw==palabra:
#     print("Datos Correctos ")
# else:
#     print("Datos Incorrecos")

ingreso=int(input("Ingrese su sueldo "))
print("1.- Basico")
print("2.- Medio")
print("3.- Superior")
edu=int(input("Ingrese su nivel educacional: "))
nacionalidad=input("Ingrese nacionalidad (chilena / Otra) ")
credito=0
if ingreso>=500000 and ingreso<=1000000:
    credito=credito+300000
elif ingreso>1000000 and ingreso<=1500000:
    credito=credito+650000
elif ingreso>1500001:
    credito=credito+1000000
else:
    print("")

if edu==1:
    print("")
elif edu==2:
    credito=credito*1.3
elif edu==3:
    credito=credito*1.5

if nacionalidad=="chilena":
    credito=credito+300000
else:
    print("")

print("Su puntaje de credito es: ", credito)

    


