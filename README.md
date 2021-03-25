# Jacobi-method
Jacobi method (determinate the solutions of linear equations) + some tests with results writing to .csv file

## Polish Description
Częściowy opis w języku angielskim zawarty jest w komentarzu w pliku jacobi_method.py 
(A partial description in English is included in the comment in the file jacobi_method.py)

### Opis plików
- Plik jacobi_method.py zawiera jedną z metod rozwiązywania układów równań liniowych - metodę Jacobiego bez uwzględniania zamiany wierszy w przypadku występowania zer na diagonali. Metoda jedynie sprawdza czy macierz jest silnie diagonalnie dominująca, lecz nie blokuje algorytmu w przeciwnym przypadku. Szczegółowy opis tej metody znajduje się pod linkiem: https://en.wikipedia.org/wiki/Jacobi_method (język angielski),
- Plik jacobi_method_tests.py zawiera 4 testy jednostkowe jednej instancji wraz z funkcją zapisującą wyniki uzyskane powyższą metodą (funkcja: write_to_file) do pliku .csv. 
### Uzyskane wyniki

Wyniki uzyskane z wykorzystaniem powyższej metody nie są w każdym przypadku rozwiązaniami idealnymi. W przypadku macierzy, które są silnie diagonalnie dominujące, rozwiązania są w większości przypadków równe tym prawdziwym (przy przybliżeniu do 2 miejsc po przecinku). Problemem tej metody numerycznej, rozwiązywania układów równań liniowych, może być: wspomniany wyżej problem braku zamiany wierszy w przypadku wykrycia zer na diagonali, skończona dokładność obliczeń wykonywanych przez komputer oraz zapisu liczb, złe uwarunkowanie macierzy czy zbyt mały dobór ilości iteracji przez algorytm.
