op=0
tex=[]
tx=0
cont=0
print("Bienvenido a Cipher\n")
print("Para introcucir un texto precione    \"1\"")
print("Para cifrar un texto precione    \"2\"")
print("Para decifrar y mostrar en pantalla precione    \"3\"")
print("\"4\"    Para salir")
op=int(input("Introsuca la opcion\n"))
while op<4:
    if op==1:
        tx=input("Introsuca el texto\n")
        print(tx)
        op=int(input("Introsuca la opcion\n"))
    elif op==2:
        print("intodusca un texto cada ves que precione enter y si quiere finalizar precione 11\n")
        while tx!="11":
            tx=input()
            cont=cont+1
            tex.append(tx)
            print(tex)
        break
        while cont
        print(tex)
        del tex[cont]
        op=int(input("Introsuca la opcion\n"))
    elif op==3:
        pint(tex)
