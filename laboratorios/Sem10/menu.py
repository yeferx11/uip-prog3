import lector
import Libro
import autor
import copia
import Pedido
class Menu:
    "Este es el Menu"
    op=0
    copi=10
    print("Bienvendido\nEsta es su Biblioteca\nOpciones")
    print("1.\tIngresar Lector\n")
    print("2.\tIngresar Autor\n")
    print("3.\tIngresar Libro\n")
    print("4.\tHacer Peticion\n")
    print("5.\tHaer Devolucion\n")
    ll={} #Almacena los datos del lector
    an={} #Almacena los datos del Autor
    la={} #Almacena los datos de Autor por libro
    lt={} #Almacena los datos de tipo por libro
    le={} #Almacena los datos de editorial por libro
    aut=0 #Almacena por el momento la variable noma para ligarla a un libro
    while op<6:
        op=int(input("Ingrese la Opcion\n"))
        if op==1:
            nom=input("Ingrese Lector:\t")
            idem=input("Ingrese Id:\t")
            lec = lector.Lector(nom,idem)
            ll[nom]=idem
            print(ll)
        elif op==2:
            noma=input("Ingrese nombre del Autor\t")
            naci=input("ingrese la nacionalidad:\t")
            au= autor.Autor(noma,naci)
            an[noma]=naci
            aut=noma
            print(an)
        elif op==3:
            tt=input("Ingrese el nombre del libro:\t")
            tip=input("Ingrese el tipo:\t")
            edito=input("Ingrese la editorial:\t")
            lib= Libro.Libro(tt,tip,edito)
            la[aut]=tt
            lt[tip]=tt
            le[edito]=tt
            print(la,lt,le,aut)
        elif op==4:
            print("Estos son los lobros disponibles:\n")
            print(la)
            ped=input("Que libro desea:\n")
            copi=copi-1
            Pedido.Pedido()
            print()
            print("Esta es la cantidad de libros disponibles",copi)
        elif op==5:
            print(la)
            ent=input("Ingrese el libro a dejar:\t")
            copi=copi+1
            print("Cantidad de los libros actuales:\t",copi)
            break
