import numpy as np

### 1. Tworzenie i modyfikowanie tablic
### **Pytanie:** Jak utworzyć tablicę NumPy zawierającą liczby od 0 do 9?
### Ćwiczenie: Utwórz jednowymiarową tablicę o wartości od 0 do 9.

a1 = np.arange(10)
print(a1)

# - **Pytanie:** Jak utworzyć macierz 3x3 wypełnioną zerami?
#     - Ćwiczenie: Stwórz macierz 3x3 wypełnioną zerami oraz macierz 4x4 wypełnioną jedynkami.

a2 = np.zeros((3,3), int)
a3 = np.ones((4,4), int)
print(a2, a3)

# - **Pytanie:** Jak stworzyć tablicę NumPy o wymiarach 2x5 wypełnioną losowymi wartościami z przedziału [0, 1]?
#     - Ćwiczenie: Stwórz tablicę o wymiarach 2x5 wypełnioną losowymi wartościami.

# ### 2. Operacje na tablicach
# - **Pytanie:** Jak dodać do siebie dwie tablice NumPy o takich samych wymiarach?
#     - Ćwiczenie: Utwórz dwie tablice NumPy o wymiarach 2x2 i dodaj je do siebie.

# - **Pytanie:** Jak przemnożyć elementy dwóch tablic o takich samych wymiarach?
#     - Ćwiczenie: Utwórz dwie tablice 3x3 i wykonaj ich elementowe mnożenie.

# - **Pytanie:** Jak znaleźć sumę elementów tablicy NumPy?
#     - Ćwiczenie: Stwórz dowolną tablicę i oblicz sumę jej wszystkich elementów oraz sumy wzdłuż wybranych osi.

# ### 3. Indeksowanie i selekcja
# - **Pytanie:** Jak wybrać podzbiór elementów z tablicy NumPy za pomocą warunków logicznych?
#     - Ćwiczenie: Utwórz tablicę losowych liczb całkowitych i wybierz z niej tylko liczby większe od 5.

# - **Pytanie:** Jak zmienić kształt (reshape) tablicy NumPy?
#     - Ćwiczenie: Utwórz tablicę o wymiarach 1x9 i przekształć ją w macierz o wymiarach 3x3.

# - **Pytanie:** Jak znaleźć indeksy elementów spełniających określony warunek?
#     - Ćwiczenie: Utwórz tablicę liczb losowych i znajdź indeksy wszystkich elementów większych od 0.5.

# ### 4. Operacje statystyczne
# - **Pytanie:** Jak obliczyć średnią, medianę, wariancję i odchylenie standardowe tablicy NumPy?
#     - Ćwiczenie: Utwórz tablicę 5x5 z losowymi wartościami i oblicz powyższe statystyki.

# - **Pytanie:** Jak znaleźć wartość minimalną i maksymalną w tablicy NumPy?
#     - Ćwiczenie: Stwórz tablicę losowych liczb całkowitych i znajdź w niej wartości minimalne i maksymalne, a także ich indeksy.

# ### 5. Złożone operacje
# - **Pytanie:** Jak wykonać operację transpozycji macierzy w NumPy?
#     - Ćwiczenie: Stwórz macierz 4x4, a następnie przetransponuj ją.

# - **Pytanie:** Jak wykonać mnożenie macierzy?
#     - Ćwiczenie: Stwórz dwie macierze 3x3 i wykonaj ich mnożenie macierzowe (nie elementowe).

# - **Pytanie:** Jak połączyć (concatenate) dwie tablice NumPy wzdłuż określonej osi?
#     - Ćwiczenie: Utwórz dwie tablice o wymiarach 2x3 i połącz je wzdłuż osi 0 oraz wzdłuż osi 1.

# ### 6. Zapis i odczyt danych
# - **Pytanie:** Jak zapisać i odczytać tablicę NumPy do/z pliku?
#     - Ćwiczenie: Zapisz dowolną tablicę do pliku tekstowego (np. CSV) oraz odczytaj ją z powrotem do tablicy NumPy.

# Te pytania i ćwiczenia pomogą Ci odświeżyć i wzmocnić podstawowe umiejętności pracy z biblioteką `NumPy`.