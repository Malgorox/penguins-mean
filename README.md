# Średnia masy ciała i długości płetwy pingwinów

Prosty skrypt w Pythonie (pandas), który liczy średnią masę ciała i średnią długość płetwy pingwinów w podziale na gatunki.

## Dane

Zbiór Palmer Penguins (344 pingwiny, 3 gatunki: Adelie, Chinstrap, Gentoo). Zawiera m.in. gatunek, wyspę, wymiary dzioba i płetwy, masę ciała i płeć. Źródło: https://github.com/allisonhorst/palmerpenguins. Plik `penguins.csv` jest dołączony do repozytorium.

## Co robi skrypt

1. Wczytuje `penguins.csv`.
2. Grupuje pingwiny według gatunku (`species`).
3. Liczy średnią z `body_mass_g` i `flipper_length_mm` dla każdego gatunku.
4. Zapisuje wynik do `wynik.csv` (3 wiersze, po jednym na gatunek).

## Uruchomienie

```
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python srednia.py
```

Po uruchomieniu w folderze pojawi się plik `wynik.csv`.