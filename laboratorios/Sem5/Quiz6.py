op=0
print("Bienvendido\nEsta es su directorio de telefonos\nOpciones")
print("1.\tImprimir numeros de telefono")
print("2.\tAgregar numeros de telefono")
print("3.\tEliminar numeros de telefono")
print("4.\tBuscar numeros de telefono")
print("5.\tSallir")
directorio={}
while op<5:
    op=int(input("Ingrese la Opcion\n"))
    if op==1:
        print(directorio)
    elif op==2:
        nom=input("Ingrese el nombre\n")
        num=input("Ingrese el numero\n")
        directorio[nom]=num
    elif op==3:
        dnom=input("Ingrese el nombre\n")
        del directorio[dnom]
    elif op==4:
        denom=input("Ingrese el nombre\n")
        print(directorio[denom])
