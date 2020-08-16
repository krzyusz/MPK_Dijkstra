# MPK_Dijkstra

Projekt dotyczy wyszukiwania najlepszych połączeń pomiędzy przystankami, na podstawie realnych danych (zebranych z rozkładu jazdy MPK po liniach miejskich, oraz
google Maps Matrix API). Graf tworzony jest z plików tekstowych umieszczonych w folderze "przystanki" i przechowywany jest w pamięci programu jako słownik.
Rozmiar grafu to 630 wierzchołków (przystanków) i ok. 1380 połączeń. 
Do wyszukiwania najlepszej trasy używany jest algorytm Dijkstry, stosowany odpowiednio dla odległości lub czasu trwania podróży między węzłami.
Aby program poprawnie funkcjonował należy umieścić folder "przystanki" w tym samym folderze co plik wykonywalny.
