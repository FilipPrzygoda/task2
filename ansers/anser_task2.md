# Zadanie 2 

## 1. Skan
Repozytorium (6 commitów) przeskanowano przy użyciu narzędzia **Gitleaks**, co ujawniło **3 wycieki** dopasowane do reguły `private-key`:

- **`deployment.key`** (commit `bc17b7d`) - klucz prywatny RSA
- **`deployment2.key`** (commit `de9d7b8`) - identyczna kopia klucza `deployment.key`
- **`awscredentials.json`** (commit `bc17b7d`) - klucz prywatny zapisany w pliku JSON

## 2. Weryfikacja wyników
- **Brak False Positive:** Gitleaks pominął zwykłe wystąpienia słowa `password` w kodzie (np. pustą zmienną `String password = "";` w `StudentController.java`).
- **Weryfikacja klucza:**
  - Polecenie `openssl rsa -check -noout` dla plików `deployment.key` oraz `deployment2.key` zwróciło komunikat `RSA key ok` – tylko ten klucz jest poprawny i możliwy do wykorzystania.
  - W pliku `awscredentials.json` polecenie `openssl pkey -check` zwróciło błąd (`Could not find private key`), ponieważ autor nadpisał część klucza ciągami `SASDASDA` i nie da się go użyć.
- **Dodatkowa weryfikacja ręczna (False Negative skanera):** Przeszukanie historii poleceniem `git grep -i "password"` wykazało zahardkodowane hasła do bazy danych w `application.properties` (`spring.datasource.password=h2` oraz `spring.database.password=1qaz@WSX`), których Gitleaks nie wykrył przez zbyt niską entropię.

## 3. Rekomendacja naprawcza
1. Unieważnić i wygenerować nowe pary kluczy oraz zmienić hasła do bazy danych.
2. Usunąć pliki `deployment.key`, `deployment2.key` oraz `awscredentials.json` z całej historii repozytorium (np. za pomocą `git filter-repo`) oraz dodać ich wzorce (`*.key`, `*credentials*.json`) do `.gitignore`.
3. Zastąpić hasła w `application.properties` odwołaniami do zmiennych środowiskowych (np. `${DB_PASSWORD}`).
