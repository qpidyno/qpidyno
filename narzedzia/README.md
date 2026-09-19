# Narzędzia profilu

Grafiki w `assets/` nie są rysowane ręcznie - generuje je `generuj.py`.
Jeśli trzeba coś zmienić (kolor, tekst, pozycję), zmienia się w skrypcie
i puszcza generowanie od nowa, a nie edytuje gotowy plik SVG.

## Odbudowanie grafik

```bash
pip install fonttools brotli
python narzedzia/generuj.py              # wszystkie grafiki
python narzedzia/generuj.py --statystyki # tylko karta z liczbami
```

Dane do karty z liczbami lecą z GitHub GraphQL API. Lokalnie wystarczy zalogowany
`gh` - skrypt sam weźmie z niego token. W GitHub Actions token idzie przez
zmienną `GH_TOKEN`.

## Dlaczego teksty są zamienione na krzywe

README na GitHubie nie wykonuje CSS-a ani JavaScriptu, a obrazek SVG nie może
pobrać czcionki z internetu. Gdyby napisy były zwykłym `<text>`, u każdego
odwiedzającego wyświetliłyby się domyślnym krojem systemowym i cała typografia
marki by się rozjechała. Dlatego `svg_lib.py` zamienia każdy znak na ścieżkę
wektorową, korzystając z tych samych plików czcionek, co strona. Efekt: wygląda
identycznie wszędzie, bez pobierania czegokolwiek.

Animacje są w CSS wewnątrz pliku SVG - to jedyna forma ruchu, jaką GitHub
przepuszcza w README. Każda grafika respektuje też ustawienie systemowe
„ogranicz animacje".

## Automat odświeżający liczby

`.github/workflows/statystyki.yml` raz dziennie przelicza statystyki i commituje
`assets/statystyki.svg`, jeśli liczby się zmieniły.

**Wymaga jednorazowej konfiguracji:** sekret `STATYSTYKI_TOKEN` w ustawieniach
repozytorium (Settings → Secrets and variables → Actions). Ma to być osobisty
token klasyczny z dwoma uprawnieniami:

- `read:user` - bez niego GitHub nie poda liczby prywatnych commitów i karta
  pokazałaby zero, bo publicznych commitów tu nie ma;
- `repo` - bez niego API nie widzi prywatnych repozytoriów, więc licznik
  repozytoriów i rozkład języków wyszłyby puste.

Sekret nie pojawia się w logach, a workflow uruchamia się wyłącznie z
harmonogramu albo ręcznie - nie da się go wywołać z zewnątrz przez pull request.

## Zrzuty ekranu

`assets/*.jpg` to zrzuty z działających serwisów i grafiki z repozytorium gry.
Nie są generowane automatycznie - podmienia się je ręcznie, gdy zmieni się wygląd
któregoś z produktów.
