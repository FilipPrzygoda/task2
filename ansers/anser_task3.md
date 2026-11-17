# Zadanie 3

## 1. Skan
Plik **`requirements-task.txt`** (18 pakietów) przeskanowano narzędziem **Safety**, wykrywając **17 podatności** w **5 pakietach**:
- **`flask` 2.3.3** (1) – Information Disclosure (ID `86909`)
- **`jinja2` 3.1.2** (5) – XSS (ID `64227`, `71591`) oraz RCE / Sandbox Escape (ID `76378`, `75976`, `74735`)
- **`mako` 1.2.4** (2) – Path Traversal / RCE (ID `98067`, `93670`)
- **`werkzeug` 2.3.7** (8) – DoS (ID `62019`, `73889`, `71595`, `82196`, `84324`, `86908`), Path Traversal (ID `73969`), RCE w debuggerze (ID `71594`)
- **`healpy` 1.8.0** (1) – podatny `libcurl` (ID `61774`)

## 2. Analiza podatności
W pakiecie **`jinja2` 3.1.2** wykryto podatność typu **RCE** (ID `75976` / **CVE-2025-27516**), pozwalającą na ucieczkę z piaskownicy. Wykorzystanie podatności jest możliwe po wywołaniu filtru `|attr` (funkcja `do_attr` z modułu `jinja2.filters`) w celu uzyskania niechronionego dostępu do metody `str.format` podczas renderowania szablonu w klasie **`SandboxedEnvironment`** (z modułu `jinja2.sandbox`). Po analizie kodu badanej aplikacji (`Flask_Book_Library`) ustalono, że klasa `SandboxedEnvironment` nie jest w ogóle wykorzystywana, w związku z czym prawdopodobieństwo wykorzystania tej podatności jest **minimalne**.
## 3. Rekomendacja naprawcza
1. Zaktualizować wersje pakietów w `requirements-task.txt` do bezpiecznych (`flask>=3.1.3`, `jinja2>=3.1.6`, `mako>=1.3.12`, `werkzeug>=3.1.6`, `healpy>=1.16.7`).
