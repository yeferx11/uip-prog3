op=0
cont=0
print("Bienvendido\nEsta es su lista de supermercado\nOpciones")
print("1.\tAgregar elementos a su lista de supermercado")
print("2.\tEliminar elementos de su lista de supermercado")
print("3.\tVer elementos de su lista de supermercado")
print("4.\tVer menu de nuevo")
print("5.\tSallir")
lista=[]
while op<5:
    op=int(input("Ingrese la Opcion\n"))
    if op==1:
        cont+=1
        arg=input("Ingrese elemento\n")
        lista.append(str(cont)+".   "+arg)
    elif op==2:
        print(lista)
        dlt=int(input("Ingrese el elemento a eliminar\n"))
        del lista[dlt-1]
    elif op==3:
        print(lista)
    elif op==4:
        print("1.\tAgregar elementos a su lista de supermercado")
        print("2.\tEliminar elementos de su lista de supermercado")
        print("3.\tVer elementos de su lista de supermercado")
