from random import randint

def genera_aleatorio(tam):
    lista = []
    while len(lista) < tam:
        a = randint(1,9)
        if a not in lista:
            lista.append(a)
    return lista
    

def captura_numero(tam):
    lista = []
    while len(lista) != tam:

        print ""
        print ""
        lista = [int(x) for x in list(raw_input("Ingrese un entero de " + str(tam) + " digitos: "))]
        print ""
    return lista




def comparar (l1, l2):
    pica = 0
    fija = 0
    for i in range (len (l1)):
        if l1 [i] in l2:
            if l1 [i] == l2 [i]:
                fija += 1
            else:
                pica += 1
    return fija, pica




def oportunidades (ale, tam):
    lista = []
    for i in range (tam):
        a = captura_numero(3)
        fija, pica = comparar (ale, a)
        if fija == 3:
            print "Felicidades, ganaste!"
            lista.append ([lista_a_cadena (a), pica, fija])
            break
        else:
            print "!Sigue intentando!  "
            print ""
            print "fijas: " + str (fija) + "      picas: " + str (pica)
            lista.append ([lista_a_cadena (a), pica, fija])
            
    

    print ""
    print ""
    print "el numero que buscabas es el: " + str (lista_a_cadena (ale))
    print ""
    print ""
    return lista

def lista_a_cadena(lista):
    cad=""
    for i in lista:
        cad+=str(i)
    return cad


ale = genera_aleatorio(3)
print lista_a_cadena(ale)
resultados = oportunidades (ale, 5)
for i in resultados:
    print "el numero ingresado fue: " + str (i[0]) + " obtuvo " + str (i[2]) + " fijas " + " y " + str (i[1]) + " picas"

