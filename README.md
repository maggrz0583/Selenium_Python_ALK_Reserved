# Selenium_Python_ALK_Reserved
PROJEKT: AUTOMATYZACJA TESTÓW APLIKACJI WEBOWEJ W PYTHONIE

Adres strony internetowej: https://www.reserved.com/pl/pl/

Autor: Magdalena Niedziułka

**Opis projektu:**
Celem projektu jest przetestowanie obszaru wyszukiwania i sortowania produktów dla sklepu internetowego https://www.reserved.com/pl/pl/. W tym celu opracowano 5 przypadków testowych:
TC1: Rejestracja nowego użytkownika przy użyciu niepoprawnego adresu email
TC2: Sortowanie produktu (sukienek) od najniższej ceny
TC3: Filtrowanie produktu (sukienek) według rozmiaru 34
TC4: Filtrowanie produktu (sukienek) według ceny (do 100)
TC5: Filtrowanie produktu (sukienek) według cech (krótki rękaw)


**Przypadki testowe**
**ID 001: **Rejestracja nowego użytkownika przy użyciu niepoprawnego adresu email
Warunki wstępne:
1. Otwarta strona https://www.reserved.com/pl/pl/
2. Użytkownik nie jest zalogowany
Kroki:
1. Zaakceptuj pop-up dotyczący cookies
2. Najedź kursorem na "Konto" 
3. Kliknij "Zarejestruj się" - otwiera się strona rejestracji
4. Wpisz niepoprawny e-mail
5. Wpisz imię
6. Wpisz nazwisko
7. Wpisz hasło
8. Zaznacz zgodę na otrzymywanie informacji handlowych
9.Kliknij załóż konto
Oczekiwany rezultat:
1. Użytkownik otrzymuje informację "Wprowadź poprawne znaki" pojawiającą się pod polem.
2. Konto nie zostaje założone
3. Przeglądarka zostaje wyłaczona

**ID 002:** Sortowanie produktu (sukienek) od najniższej ceny
Warunki wstępne:
1. Otwarta strona https://www.reserved.com/pl/pl/
Kroki:
1. Zaakceptuj pop-up dotyczący cookies
2. W Menu głównym najedź kursorem na pozycję "Kobieta"
3. W rozwinietym podmenu kliknij na pozycję "Sukienki"
4. Kliknij na przycisk Sortuj
5. Zaznacz wartość "Ceny rosnąco"
6. Kliknij przycisk "Sortuj"
Oczekiwany rezultat:
1. System wyświetla listę produktów posortowanych od najniższej do najwyższej ceny
2. Przeglądarka zostaje wyłaczona

**ID 003:** Filtrowanie produktu (sukienek) według rozmiaru 34
Warunki wstępne:
1. Otwarta strona https://www.reserved.com/pl/pl/
Kroki:
1. Zaakceptuj pop-up dotyczący cookies
2. W Menu głównym najedź kursorem na pozycję "Kobieta"
3. W rozwinietym podmenu kliknij na pozycję "Sukienki"
4. Kliknij na przycisk Rozmiary
5. Zaznacz wartość "34"
6. Kliknij przycisk "Filtruj"
Oczekiwany rezultat:
1. System wyświetla listę produktów pofiltrowanych po wartości "34"
2. Przeglądarka zostaje wyłaczona

**ID 004:** Filtrowanie produktu (sukienek) według ceny (do 100)
Warunki wstępne:
1. Otwarta strona https://www.reserved.com/pl/pl/
Kroki:
1. Zaakceptuj pop-up dotyczący cookies
2. W Menu głównym najedź kursorem na pozycję "Kobieta"
3. W rozwinietym podmenu kliknij na pozycję "Sukienki"
4. Kliknij na przycisk Cena
5. W polu "cena do" wpisz wartość "100"
6. Kliknij przycisk "Filtruj"
Oczekiwany rezultat:
1. System wyświetla listę produktów do kwoty "100"
2. Przeglądarka zostaje wyłaczona

**ID 005:** Filtrowanie produktu (sukienek) według cech (krótki rękaw)
Warunki wstępne:
1. Otwarta strona https://www.reserved.com/pl/pl/
Kroki:
1. Zaakceptuj pop-up dotyczący cookies
2. W Menu głównym najedź kursorem na pozycję "Kobieta"
3. W rozwinietym podmenu kliknij na pozycję "Sukienki"
4. Kliknij na przycisk Cechy
5. Zaznacz wartość "krótki rękaw"
6. Kliknij przycisk "Filtruj"
Oczekiwany rezultat:
1. System wyświetla listę produktów pofiltrowanych według cechy: krótki rękaw
2. Przeglądarka zostaje wyłaczona
