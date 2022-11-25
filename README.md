# Wprowadzenie do Systemów Wizyjnych

## Politechnika Poznańska, Instytut Robotyki i Inteligencji Maszynowej

<p align="center">
  <img width="180" height="180" src="./readme_files/logo.svg">
</p>

# **Projekt zaliczeniowy: zliczanie cukierków**

Wraz z postępem technologicznym w obszarze sensorów wizyjnych wzrosło zapotrzebowanie na rozwiązania umożliwiające automatyzację procesów z wykorzystaniem wizyjnej informacji zwrotnej. Ponadto rozwój naukowy w zakresie algorytmów przetwarzania obrazu umożliwia wyciąganie ze zdjęć takich informacji jak ilość obiektów, ich rozmiar, położenie, a także orientacja. Jedną z aplikacji wykorzystujących przetwarzanie obrazu jest automatyczna kontrola ilości obiektów na linii produkcyjnej wraz z rozróżnieniem ich klasy np. w celu ich sortowania w dalszym kroku.

## Changelog
**Ostatnia edycja:** 25.11.2022


## Zadanie

Zadanie projektowe polega na przygotowaniu algorytmu wykrywania i zliczania kolorowych cukierków znajdujących się na zdjęciach. Dla uproszczenia zadania w zbiorze danych występują jedynie 4 kolory cukierków:
- czerwony
- żółty
- zielony
- fioletowy

Wszystkie zdjęcia zostały zarejestrowane "z góry", ale z różnej wysokości i pod różnym kątem. Ponadto obrazy różnią się między sobą poziomem oświetlenia oraz oczywiście ilością cukierków.

Poniżej przedstawione zostało przykładowe zdjęcie ze zbioru danych i poprawny wynik detekcji dla niego:

```bash
{
  ...,
  "37.jpg": {
    "red": 2,
    "yellow": 2,
    "green": 2,
    "purple": 2
  },
  ...
}
```

<p align="center">
  <img width="750" height="500" src="./data/37.jpg">
</p>

## Struktura projektu

Szablon projektu zliczania cukierków na zdjęciach dostępny jest w serwisie [GitHub](https://github.com/PUTvision/WDPOProject) i ma następującą strukturę:

```bash
.
├── data
│   ├── 00.jpg
│   ├── 01.jpg
│   └── 02.jpg
├── readme_files
├── detect.py
├── README.md
└── requirements.txt
```

Katalog [`data`](./data) zawiera przykłady, na podstawie których w pliku [`detect.py`](./detect.py) przygotowany ma zostać algorytm zliczania cukierków. Funkcja `main` w pliku `detect.py` powinna pozostać bez zmian. 

### Wykorzystanie szablonu

W przypadku chęci wykorzystania przygotowanego szablonu oraz systemu kontroli wersji w postaci serwisu GitHub możliwe jest stworzenie własnego repozytorium na podstawie szablonu. W tym celu należy poprzez przycisk `Use this template` utworzyć nowe repozytorium wybierając swoje konto jako właściciela, nadając mu własną nazwę i obowiązkowo ustawiając widzialność jako **prywatne**. Powyższe kroki zostały przedstawione na załączonych zdjęciach.

<p align="center">
  <img width="900" height="200" src="./readme_files/create_repo_from_template_01.png">
</p>
<p align="center">
  <img width="600" height="500" src="./readme_files/create_repo_from_template_02.png">
</p>

### Biblioteki

Interpreter testujący projekty będzie miał zainstalowane biblioteki:
- [OpenCV](https://docs.opencv.org/master/) w wersji 4.5.3.56
- [NumPy](https://numpy.org/) w wersji 1.19.5
- [Click](https://palletsprojects.com/p/click/) w wersji 7.1.2
- [tqdm](https://tqdm.github.io/) w wersji 4.62.3

Natomiast w przypadku wykorzystania w projekcie dodatkowych bibliotek należy przygotować plik `requirements.txt`, zawierający informacje o dodatkowym pakiecie i jego wersji, zgodnie z poniższym przykładem:

```bash
scikit-image==0.18.3
matplotlib
```

Więcej informacji na temat zastosowania plików `requirements.txt` można znaleźć w:
- [What is the python requirements.txt?](https://www.idkrtm.com/what-is-the-python-requirements-txt/)
- [Use requirements.txt](https://www.jetbrains.com/help/pycharm/managing-dependencies.html)

### Wywołanie programu

Skrypt `detect.py` przyjmuje 2 parametry wejściowe:
- `data_path` - ścieżkę do folderu z danymi (zdjęciami)
- `output_file_path` - ścieżkę do pliku z wynikami

```bash
$ python3 detect.py --help

Options:
  -p, --data_path TEXT         Path to data directory
  -o, --output_file_path TEXT  Path to output file
  --help                       Show this message and exit.
```

W konsoli systemu Linux skrypt można wywołać z katalogu projektu w następujący sposób:

```bash
python3 detect.py -p ./data -o ./results.json
```

Konfiguracja parametrów wejściowych skryptu w środowisku PyCharm została opisana w pliku [PyCharm_input_configuration.md](./PyCharm_input_configuration.md).

## Przesyłanie rozwiązania

Stworzone rozwiązanie należy skompresować do formatu `ZIP`, a wyjściowy plik nazwać numerem indeksu (np. 123456.zip). Zadanie to można przykładowo zrealizować w systemach Linux z wykorzystaniem komendy systemowej `zip` w terminalu tak, jak to zostało przedstawione poniżej:

```bash
zip <NUMER INDEKSU>.zip detect.py requirements.txt
```

Skompresowany plik należy wstawić w odpowiednim miejscu na platformie eKursy.

**Uwaga:** w pliku `.zip` powinien znajdować się jedynie bezpośrednio plik `detect.py` oraz opcjonalnie `requirements.txt`.

## Ewaluacja rozwiązań

Przesłane rozwiązania zostaną sprawdzone pod kątem plagiatu oraz z wykorzystaniem poniższego wzoru ocenione będzie działanie algorytmu zliczania cukierków:  

<p align="center">
  <img src="https://latex.codecogs.com/svg.image?\bg_white&space;Mean&space;Absolute&space;Relative&space;Percentage&space;Error&space;[%]&space;=&space;\frac{100}{n}\sum_{t=0}^{n-1}\frac{\left|y_{r}-\widehat{y_{r}}\right|&space;&plus;&space;\left|y_{y}-\widehat{y_{y}}\right|&space;&plus;&space;\left|y_{g}-\widehat{y_{g}}\right|&space;&plus;&space;\left|y_{p}-\widehat{y_{p}}\right|}{y_{r}&plus;y_{y}&plus;y_{g}&plus;y_{p}}" title="\bg_white Mean Absolute Relative Percentage Error [%] = \frac{100}{n}\sum_{t=0}^{n-1}\frac{\left|y_{a}-\widehat{y_{a}}\right| + \left|y_{b}-\widehat{y_{b}}\right| + \left|y_{o}-\widehat{y_{o}}\right|}{y_{a}+y_{b}+y_{o}}" style="background-color: white"/>
</p>

Gdzie:
- ![](https://render.githubusercontent.com/render/math?math=n) oznacza liczbę obrazów
- ![](https://render.githubusercontent.com/render/math?math=y_x) oznacza rzeczywistą ilość danego koloru
- ![](https://render.githubusercontent.com/render/math?math=\widehat{y_x}) oznacza przewidzianą ilość danego koloru

Końcowy zbiór ewaluacyjny, na którym testowany będzie algorytm jest niepubliczny i niedostępny w czasie realizacji projektu. Do dyspozycji studentów w całości dostępny jest zbiór treningowy dostępny w katalogu [data](./data).
