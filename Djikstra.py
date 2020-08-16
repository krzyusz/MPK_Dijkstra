#coding=utf-8
import glob
import os
import codecs
import ast

#wczytywanie przystanków z plików
graf="{"
for file in glob.glob("./przystanki/*.txt"):
    graf=graf+"'"+os.path.basename(file).replace(".txt","")+"'"
    with codecs.open(file,'r',encoding='utf8') as f:
        graf=graf+":{"+f.read()[:-1]+"},"
graf=graf[:-1]
graf=graf+"}"
# zamiana str na dict
graf2 = ast.literal_eval(graf)
def dijkstra(graph, start, cel,tryb):
    najkrotszy_dystans = {}
    poprzednik = {}
    nieodwiedzone_wierz = graph
    infinity = 9999999
    sciezka = []
    for wezel in nieodwiedzone_wierz:#zapelnienie wszystkich wag na infinity poza startem
        najkrotszy_dystans[wezel] = infinity
    najkrotszy_dystans[start] = 0

    while nieodwiedzone_wierz:
        minwezel = None
        for wezel in nieodwiedzone_wierz: #wyszukiwanie wierzołka o najmniejszym koszcie
            if minwezel is None:
                minwezel = wezel
            elif najkrotszy_dystans[wezel] < najkrotszy_dystans[minwezel]:
                minwezel = wezel

        for podwezel, waga in graph[minwezel].items():#porównywanie wag wlasciwy algorytm djikstry
            if waga[tryb] + najkrotszy_dystans[minwezel] < najkrotszy_dystans[podwezel]:
                poprzednik[podwezel] = minwezel
                najkrotszy_dystans[podwezel] = waga[tryb] + najkrotszy_dystans[minwezel]
        nieodwiedzone_wierz.pop(minwezel)

    aktualny_wezel = cel
    while aktualny_wezel != start:
        try:
            sciezka.insert(0, aktualny_wezel)
            aktualny_wezel = poprzednik[aktualny_wezel]
        except KeyError:
            print('Nie można wyznaczyć trasy')
            break
    sciezka.insert(0, start)
    if najkrotszy_dystans[cel] != infinity:
        if tryb==0:
            print('Najkrótszy dystans to ' + str(najkrotszy_dystans[cel])+" m")
            print('Scieżka to: ' + str(sciezka))
        elif tryb==1:
            print('Najkrótszy czas to ' + str(najkrotszy_dystans[cel])+" s")
            print('Scieżka to: ' + str(sciezka))


#tryb 0 oblicza dla dlugosci, a tryb 1 dla czasu
start=input("Podaj przystanek początkowy: ")
cel=input("Podaj przystanek koncowy: ")
tryb=input("Podaj tryb:0 dla długości, 1 dla czasu: ")
dijkstra(graf2, start,cel,int(tryb))
