#chamba de Erick Ethel Cordova Gonzalez
#funciooooon de el rombo
#osea checar que es rombo ps

import math
def es_rombo(a,b,c,d):
    lados=False
    Rombo=False
    #Un rombo es:
    #un cuadrilatero paralelogramo con
    #cuatro lados iguales
    #angulos opuestos iguales #osea laterales iguales y arriba abajo tmbn
    #cada punto tiene X y Y, OBVIAMENTE
    #ABCD son listas, obvio
    #calcular distancia para saber los lados, supongo
    #formula distancia:
    #mats.sqrt(x2-x1^2 + y2-y1^2)
    d1=math.sqrt(((b[0]-a[0])**2)+((b[1]-a[1])**2))
    d2=math.sqrt(((c[0]-b[0])**2)+((c[1]-b[1])**2))
    d3=math.sqrt(((d[0]-c[0])**2)+((d[1]-c[1])**2))
    d4=math.sqrt(((a[0]-d[0])**2)+((a[1]-d[1])**2))
    if d1==d2 and d2==d3 and d3==d4 and d4==d1:
        lados=True#que los lados sean iguales pue
    if lados==True:
        #como los lados son iguales, ahora checar que los angulos opuestos sean iguales
        #formula m (pendiente)=y2-y1/x2-x1
        #con formula= grados=tan((m2-m1)/(1+m2*m1))
        #pendientes
        m1=(b[1]-a[1])/(b[0]-a[0])        
        m2=(c[1]-b[1])/(c[0]-b[0])        
        m3=(d[1]-c[1])/(d[0]-c[0])        
        m4=(a[1]-d[1])/(a[0]-d[0])
        #grados
        g1=math.atan(abs((m2-m1)/(1+m2*m1)))
        g2=math.atan(abs((m3-m2)/(1+m3*m2)))
        g3=math.atan(abs((m4-m3)/(1+m4*m3)))
        g4=math.atan(abs((m1-m4)/(1+m1*m4)))
        g1 = round(g1, 10)
        g2 = round(g2, 10)
        g3 = round(g3, 10)
        g4 = round(g4, 10)
        
        if g1==g3 and g2==g4:
            rombo=True
    else:
        rombo=False
    return rombo
"""
#ejemplo de puntos para un rombo
a = [0, 0]
b = [3, 1]
c = [4, 4]
d = [1, 3] 

var=es_rombo(a,b,c,d)

if var==True:
    print("Tu figura es un rombo")
else:
    print("La grafica no es un rombo")
"""