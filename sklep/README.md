# TeamRocketSupply

Prosty sklep internetowy stworzony w Django. Projekt umożliwia przeglądanie produktów, filtrowanie po kategoriach, wyszukiwanie oraz dodawanie produktów do koszyka.

## Funkcje
- strona główna z wyróżnionymi produktami
- wyszukiwarka produktów
- podział na kategorie
- podstrona szczegółów produktu
- koszyk oparty na sesji
- sekcja bestsellerów

## Technologie
- Python
- Django
- SQLite
- HTML / CSS

## Uruchomienie projektu

1. Sklonuj repozytorium lub pobierz pliki
2. Utwórz i aktywuj środowisko wirtualne
3. Zainstaluj zależności:

```bash
pip install -r requirements.txt
```

4. Wykonaj migracje:

```bash
python manage.py migrate
```

5. Uruchom serwer

```bash
python manage.py runserver
```

6. Otwórz w przeglądarce:
'http://127.0.0.1:8000/'