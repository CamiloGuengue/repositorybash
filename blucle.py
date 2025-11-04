n = int(input("INGRESE LA CANTIDAD DE NUMEROS A DESCUBRIR :  "))
#for i in range (n+1):
#    if(i == 0):
#        print(i," ", "este numero es cero")
#    elif(i%2>0):
#        print(i," ","este numero es impar")
#    else:
#        print(i," ","este numero es par")

i=0
while (i<n+1):
    if(i == 0):
        print(i," ", "este numero es cero")
    elif(i%2>0):
        print(i," ","este numero es impar")
    else:
        print(i," ","este numero es par")
        
    i = i +1