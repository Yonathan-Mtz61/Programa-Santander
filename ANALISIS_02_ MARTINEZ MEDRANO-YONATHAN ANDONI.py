import csv
datos=[]
encabezado=[]
with open("synergy_logistics_database.csv", "r")as archivo:
    lector = csv.reader(archivo, delimiter =",")    
    for i in lector:
        encabezado.append(i)
        break
    for i in lector:
        datos.append(i)

"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------"""

""" 
Opción 1) Rutas de importación y exportación. Synergy logistics está considerando la posibilidad de enfocar sus esfuerzos en las 10 rutas más demandadas.
Acorde a los flujos de importación y exportación, ¿cuáles son esas 10 rutas? ¿le conviene implementar esa estrategia? ¿porqué?"""

Rutas_de_importación_y_exportación_0=[]
Rutas_de_importación_y_exportación_1=[]
for i in range(0,len(datos),1):
    Rutas_de_importación_y_exportación_0.append(datos[i][2]+"-"+datos[i][3])
    Rutas_de_importación_y_exportación_1.append([datos[i][2]+"-"+datos[i][3],datos[i][9]])

Rutas_de_importación_y_exportación_1.sort(key=lambda x:x[0],reverse=False)

Rutas_de_importación_y_exportación_2=[]
for i in range(0,len(Rutas_de_importación_y_exportación_1),1):
    if Rutas_de_importación_y_exportación_1[i][0] != Rutas_de_importación_y_exportación_1[i-1][0]:
        Rutas_de_importación_y_exportación_2.append(Rutas_de_importación_y_exportación_1[i][0])

Rutas_de_importación_y_exportación_3=[]
for i in range(0,len(Rutas_de_importación_y_exportación_2),1):
    Rutas_de_importación_y_exportación_3.append(Rutas_de_importación_y_exportación_0.count(Rutas_de_importación_y_exportación_2[i]))

Rutas_de_importación_y_exportación_4=[]
conteo=0
for i in range(0,len(Rutas_de_importación_y_exportación_2),1):
    contador=0
    for j in range(0,len(Rutas_de_importación_y_exportación_1),1):
        if Rutas_de_importación_y_exportación_2[i] == Rutas_de_importación_y_exportación_1[j][0]:
            contador += int(Rutas_de_importación_y_exportación_1[j][1])
    Rutas_de_importación_y_exportación_4.append([Rutas_de_importación_y_exportación_3[i],Rutas_de_importación_y_exportación_2[i],contador])
    conteo += contador

Rutas_de_importación_y_exportación_4.sort(key=lambda x:x[2],reverse=True)

Rutas_de_importación_y_exportación_5=[]
contador=0
for i in range(0,10):
    Rutas_de_importación_y_exportación_5.append(["La ruta: "+str(Rutas_de_importación_y_exportación_4[i][1])+" tuvo un registro de: "+str(Rutas_de_importación_y_exportación_4[i][0])+" salidas con un valor de ex/importacion de: "+str(Rutas_de_importación_y_exportación_4[i][2])+"$"])
    contador+= int(Rutas_de_importación_y_exportación_4[i][2])

"""==========>"""
print("\n"*2,"\t"*4,"Las 10 Rutas de importación y exportación más demandadas por importación y exportación","\n")
print(Rutas_de_importación_y_exportación_5,"\n")
"""==========>"""

con=0
for i in range(0,len(Rutas_de_importación_y_exportación_1),1):
    con += int(Rutas_de_importación_y_exportación_1[i][1])


"""El primer print muestra el valor total de las 10 rutas, el segundo hace una verificacion de que si la cantidad de valores totales de la base de datos y los valores
que yo programe son iguales, el tercero muestra el valor total de todas las importaciones y exportaciones, el cuarto hago una division para saber que fraccion es el total
de las 10 rutas, el quinto y ultimo muestra la cantidad de rutas totales y menos 10 que son la estrategia

print(contador)
print(conteo == con)
print(con)
print(conteo/contador)
print(len(Rutas_de_importación_y_exportación_2)-10)
"""


"""para centrarse en las 10 rutas con mas exportacion e importacion como estrategia para esta empresa no la veria como una opcion porque en el rango de años (5 años)
que tiene esta empresa con la base de datos que nos dan no lo veria como una opcion ya que al hacer la sumatoria de estas 10 rutas con mas importacion y exportacion
hacen una tercera parte del total de todas las rutas, si tuviera un panorama mas extenso de como esque fue avanzando estas rutas a lo largo de los 5 años pudiera decir
con mas certeza si es una buena estrategia, sin embargo se reducirian mucho los costos en ciertas rutas si se tomaran como prioridad estas 10 rutas como su principal
enfoque, pero si la empresa depende de esas 2 terceras partes que es bastante obvio que si entonces no seria una buena opcion dejar como las 10 principales rutas ya que
el total de rutas son 172 y si lo vieramos en perpectiva de que 10 rutas estan haciendo una tercera parte de lo que las 162 rutas restantes estan haciendo es algo increible
por lo que si seria buena estrategia dejar esas 10 rutas solo si la empresa no necesite esas 2 terceras partes del total y como condicion de ver un histograma de como
fue avanzando a lo largo de los años estas 10 rutas."""



"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------"""





"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""
Opción 2) Medio de transporte utilizado. ¿Cuáles son los 3 medios de transporte más importantes para Synergy logistics considerando el valor de las
importaciones y exportaciones? ¿Cuál es medio de transporte que podrían reducir? 
"""

Medio_transporte_utilizado=[]
Medio_transporte_utilizado_valor=[]

for i in range(0,len(datos),1):
    Medio_transporte_utilizado.append(datos[i][7])
    Medio_transporte_utilizado_valor.append(datos[i][9])
    
Medio_transporte_utilizado_lista=list(set(Medio_transporte_utilizado))

lista_resumen=[]
for i in range(0,len(Medio_transporte_utilizado_valor),1):
    lista_resumen.append([Medio_transporte_utilizado[i],Medio_transporte_utilizado_valor[i]])

lista_todo=[]
for k in range(0,len(Medio_transporte_utilizado_lista),1):
    contador=0
    conteo=0
    for i in range(0,len(lista_resumen),1):
        for j in range(0,len(Medio_transporte_utilizado_lista),1):
            if lista_resumen[i][0] == Medio_transporte_utilizado_lista[k] and lista_resumen[i][0] == Medio_transporte_utilizado_lista[j]:
                contador =contador + int(lista_resumen[i][1])
                conteo += 1
    lista_todo.append([conteo,Medio_transporte_utilizado_lista[k],contador])

lista_todo.sort(key=lambda x:x[2],reverse=True)

lista_Medio_de_transporte_utilizado_1=[]
for i in range(0,len(lista_todo),1):
    lista_Medio_de_transporte_utilizado_1.append(["El medio de transporte: "+"'"+str(lista_todo[i][1])+"'"+" tuvo un registro de: "+str(lista_todo[i][0])+" con un valor total de: "+str(lista_todo[i][2])+" $"])

lista_Medio_de_transporte_utilizado_1_1=[]
for i in range (0,len(lista_todo),1):
    lista_Medio_de_transporte_utilizado_1_1.append([lista_todo[i][1],lista_todo[i][2]/lista_todo[i][0]])

lista_Medio_de_transporte_utilizado_1_1.sort(key=lambda x:x[1],reverse=True)

lista_Medio_de_transporte_utilizado_1_2=[]
for i in range(0,len(lista_Medio_de_transporte_utilizado_1_1),1):
    lista_Medio_de_transporte_utilizado_1_2.append(["En resumen el medio de transporte: "+"'"+str(lista_Medio_de_transporte_utilizado_1_1[i][0])+"'"+" por cada ex/importacion tuvo un valor de: "+str(lista_Medio_de_transporte_utilizado_1_1[i][1])+" $"])

"""==========>"""
print("\n"*2,"\t"*2,"Los 3 medios de transporte más importantes para Synergy logistics considerando el valor de las importaciones y exportaciones","\n")
print(lista_Medio_de_transporte_utilizado_1,"\n")
print(lista_Medio_de_transporte_utilizado_1_2,"\n")
"""==========>"""

"""El medio de transporte mas utilizado va en orden dependiendo de las veces que se utilizo y ademas del valor total de cada ex/importacion, como el valor de esa
ex/importacion se sumaba y se guardaba al igual con el medio de trasporte para los casos similares tambien se contaba y se guardaba en una lista, para hacer como
un resumen de las veces que se uso ese medio y del valor promedio que este medio de trasporte aporto a esta compañia y asi en resumen y no es que se pueda reducir
un medio que otro pero aun asi por los filtros que hice podria decirse que los primeros 3 que se muestran son los mas importantes en base a las condiciones que me
solicitan y el 4 medio de transporte es el que podria decirse que se podria reducir, mas sin embargo debemos de ver si es una alternativa en cuestion de la ruta y
el precio de trasportar esos productos a un futuro."""


"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------"""



"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------"""

"""
Opción 3) Valor total de importaciones y exportaciones. Si Synergy Logistics quisiera enfocarse en los países que le generan el 80% del valor de las exportaciones
e importaciones ¿en qué grupo de países debería enfocar sus esfuerzos?"""

Valor_total_de_importaciones_y_exportaciones_1=[]
for i in range(0,len(datos),1):
    Valor_total_de_importaciones_y_exportaciones_1.append(int(datos[i][9]))

Valor_total_de_importaciones_y_exportaciones_2 = sum(Valor_total_de_importaciones_y_exportaciones_1)

Valor_total_de_importaciones_y_exportaciones_3=[]
for i in range(0,len(Rutas_de_importación_y_exportación_2),1):
    contador=0
    for j in range(0,len(Rutas_de_importación_y_exportación_1),1):
        if Rutas_de_importación_y_exportación_2[i] == Rutas_de_importación_y_exportación_1[j][0]:
            contador += int(Rutas_de_importación_y_exportación_1[j][1])
    Valor_total_de_importaciones_y_exportaciones_3.append([Rutas_de_importación_y_exportación_2[i],contador])
    
Valor_total_de_importaciones_y_exportaciones_3.sort(key=lambda x:x[1],reverse=True)

conteo=0
ciclo=[]
for i in range(0,len(Valor_total_de_importaciones_y_exportaciones_3),1):
    conteo += Valor_total_de_importaciones_y_exportaciones_3[i][1]
    if conteo <= (Valor_total_de_importaciones_y_exportaciones_2 * 0.8):
        ciclo.append(Valor_total_de_importaciones_y_exportaciones_3[i][0])

"""==========>"""
print("\n"*2,"\t"*5,"Los paises con un enfoque que genera el 80% del total de ex/importaciones es: ","\n")
print(ciclo,"\n")
"""==========>"""

"""La forma de orden de los paises es de mayor a menor en cuestion de valor total de la ruta que hizo ese medio de transporte, por lo que la forma en como aparecen los
paises en la lista son los que tienen mayor valor de ex/importacion de la base de datos con la condicion que la suma de estos nos den  el 80% del valor total de todas las
ex/importaciones."""


"""-----------------------------------------------------------------------------------------------------------------------------------------------------------------"""
