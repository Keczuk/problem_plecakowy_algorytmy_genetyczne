# Problem plecakowy – algorytm genetyczny

Ten projekt pokazuje, jak można rozwiązać klasyczny problem plecakowy przy użyciu algorytmu genetycznego.  
Całość została napisana w Pythonie i uzupełniona o prosty interfejs graficzny, dzięki czemu algorytm można łatwo przetestować bez zaglądania w kod.

Projekt powstał jako połączenie teorii z praktyką – chodziło nie tylko o samo rozwiązanie problemu, ale też o pokazanie, jak taki algorytm faktycznie działa krok po kroku.

---

## Co robi program?

Program pozwala użytkownikowi:
- dodać własne przedmioty (waga i wartość),
- ustawić maksymalną wagę plecaka,
- uruchomić algorytm genetyczny,
- zobaczyć, które przedmioty zostały wybrane i jaka jest ich łączna wartość.

Algorytm sam szuka najlepszego zestawu przedmiotów, pilnując, aby nie został przekroczony limit wagi.

---

## Jak to działa?

Każde rozwiązanie jest zapisane jako ciąg zer i jedynek, gdzie:
- `1` oznacza, że przedmiot jest w plecaku,
- `0` oznacza, że przedmiot został pominięty.

Algorytm tworzy populację takich rozwiązań i z każdą kolejną generacją:
- wybiera lepsze osobniki,
- łączy je ze sobą,
- wprowadza losowe zmiany (mutacje).

Jeśli dane rozwiązanie przekracza dopuszczalną wagę, jest automatycznie odrzucane.

---

## Interfejs graficzny

Zamiast pracy w konsoli, program posiada prosty interfejs graficzny oparty o bibliotekę Tkinter.  
Dzięki temu:
- łatwo zmieniać dane wejściowe,
- szybko sprawdzić różne przypadki,
- wygodnie pokazać działanie algorytmu na zajęciach lub podczas prezentacji.

---

## Technologie

- Python  
- Tkinter  
- algorytm genetyczny (własna implementacja)

---

## Dlaczego warto zajrzeć do repozytorium?

Projekt pokazuje:
- praktyczne zastosowanie algorytmu genetycznego,
- prostą i czytelną implementację,
- połączenie algorytmu optymalizacyjnego z GUI.

Może być dobrym punktem wyjścia do dalszych eksperymentów lub rozbudowy projektu.

---

Szczegółowy opis algorytmu, parametrów oraz przykłady działania znajdują się w osobnym pliku PDF.
