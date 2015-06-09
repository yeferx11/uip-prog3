name=input("Ingrese el Nombre:")
venta1=input("Ingrese las ventas del mes 1:")
venta2=input("Ingrese las ventas del mes 2:")
venta3=input("Ingrese las ventas del mes 3:")
ventast=float(venta1)+float(venta2)+float(venta3)
comis=ventast*0.125
print("Vendedor\tVentas\tComision\t\n--------\t-------\t------\t\n"+name+"\t"+str(ventast)+"\t"+str(comis))
