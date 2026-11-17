# Zadanie 1

## 1. Zidentyfikowana podatność
Podczas testowania aplikacji w zakładce http://127.0.0.1:5000/customers/ (dodawaniu nowego klienta) wykryto wyciek wrażliwych danych osobowych w logach konsolowych aplikacji. 

W logach jawnie zapisywane były następujące dane:
* **PESEL** (`Pesel`)
* **Imię i nazwisko** (`Name`)
* **Pełny adres zamieszkania:** miasto (`City`), ulica (`Street`) oraz numer lokalu (`AppNo`)

**Przykład logu przed poprawką:**
```text
Getting: Customer(ID: None, Name: Name, City: City, Age: 10, Pesel: 12345678901, Street: Street, AppNo: Appno)
```

## 2. Zastosowana poprawka
Zmodyfikowano metodę `__repr__` w modelu `Customer` (`project/customers/models.py`), zachowując oryginalny format logowania:
* Poprawne dane wrażliwe (PESEL, imię i nazwisko, miasto, ulica, numer lokalu) są maskowane w logach stałym ciągiem znaków `*****`.
* W przypadku pustych lub nieprawidłowych danych (PESEL niebędący ciągiem 11 cyfr) w logach wyświetla się komunikat `Empty or Invalid`.

**Przykład logu po poprawce:**
```text
Getting: Customer(ID: None, Name: *****, City: *****, Age: 21, Pesel: *****, Street: *****, AppNo: *****)
```
