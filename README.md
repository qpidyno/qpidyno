<div align="center">
  <a href="https://rowienski-interactive.pl">
    <img src="assets/hero.svg" alt="Rowieński Interactive - software house" width="900">
  </a>
</div>

<br>

<div align="center">
  <a href="https://rowienski-interactive.pl"><img src="https://img.shields.io/badge/rowienski--interactive.pl-E60000?style=for-the-badge&logoColor=EDEDF2&labelColor=08080B" alt="Strona"></a>
  <a href="https://podivo.pl"><img src="https://img.shields.io/badge/podivo.pl-0C0C11?style=for-the-badge&logoColor=EDEDF2&labelColor=08080B" alt="Podivo"></a>
  <a href="https://polskigaming.rowienski-interactive.pl"><img src="https://img.shields.io/badge/polski_gaming-0C0C11?style=for-the-badge&logoColor=EDEDF2&labelColor=08080B" alt="Polski Gaming"></a>
</div>

<br>

<img src="assets/naglowek-kim.svg" alt="Kim jestem" width="900">

Nazywam się **Mateusz Rowieński** i prowadzę jednoosobowy warsztat, który właśnie
zamienia się w firmę. Nie pokazuję makiet ani szablonów - tylko rzeczy, które można
otworzyć i sprawdzić: system dla klinik działający online, grę w produkcji i programy
na Windowsa gotowe do pobrania.

Odpowiadam za wszystko: architekturę, kod, bazy danych, serwery i bezpieczeństwo, ale
też za to, jak produkt wygląda i jak się go używa. **Claude Code to narzędzie, nie
współautor** - przyspiesza pisanie kodu i zdejmuje ze mnie powtarzalną robotę, dzięki
czemu jeden człowiek ogarnia tyle projektów naraz. Struktura, decyzje projektowe
i odpowiedzialność za to, co trafia na produkcję, zostają po mojej stronie.

**AI nie tylko w chmurze.** MNICH tłumaczy pliki gier i modów lokalnie, na polskim
modelu **Bielik**, uruchomionym na karcie graficznej użytkownika - żaden tekst nie
wychodzi poza jego komputer. NBB usuwa tło z grafik tak samo: model liczy u odbiorcy,
bez konta i bez wysyłania zdjęć na cudzy serwer. Potrafię postawić model lokalnie
i wpiąć go w program tak, żeby wykonywał konkretną robotę, a nie był ozdobą.

Większość repozytoriów jest prywatna, bo to produkty komercyjne, więc zamiast kodu
**pokazuję tu, jak one wyglądają.**

<img src="assets/dzielnik.svg" alt="" width="900">

<img src="assets/naglowek-warsztat.svg" alt="Co zbudowałem" width="900">

### PODIVO - system rezerwacji dla klinik podologicznych

Pacjent znajduje specjalistę i rezerwuje termin w kilka sekund, a klinika dostaje
panel do zarządzania grafikiem. Działa online, z aplikacjami mobilnymi,
na moich własnych serwerach.

> **Wersja online działa na danych testowych.** Kliniki, specjaliści i wolne terminy,
> które widać po wejściu, są przykładowe - to demo do klikania, a nie kartoteka
> prawdziwych gabinetów.

<a href="https://podivo.pl">
  <img src="assets/podivo-booking.jpg" alt="Podivo - wyszukiwanie i rezerwacja wizyty" width="900">
</a>

<table>
  <tr>
    <td width="50%">
      <img src="assets/podivo-biznes.jpg" alt="Podivo - logowanie do panelu klinik" width="440">
      <p><sub><b>PANEL KLINIKI</b> - logowanie dla gabinetów, z grafikiem i obsługą wizyt.</sub></p>
    </td>
    <td width="50%">
      <p><b>W środku:</b></p>
      <ul>
        <li>rezerwacje online z potwierdzeniem SMS</li>
        <li>panel biznesowy dla klinik + sekcja pomocy</li>
        <li>własny serwer zdjęć gabinetów</li>
        <li>osobne bazy danych dla pacjentów, klinik i kartotek</li>
        <li>aplikacje na Androida</li>
      </ul>
      <p><a href="https://podivo.pl"><b>-> podivo.pl</b></a></p>
    </td>
  </tr>
</table>

<img src="assets/dzielnik.svg" alt="" width="900">

### BACKHAUL - A Trucking Company Sim

Symulacja firmy transportowej na mapie Polski i Europy: zlecenia, trasy, flota
i kierowcy z własnym morale, zmęczeniem i lojalnością. Budowana w Godot 4 na C#.
**W produkcji.**

<img src="assets/backhaul-menu.jpg" alt="Backhaul - menu główne z mapą tras" width="900">

<img src="assets/backhaul-art.jpg" alt="Backhaul - zarządzanie kierowcami" width="900">

<sub>Menu główne i panel kierowców. Każdy kierowca ma staż, języki, wynagrodzenie i charakter,
a morale potrafi spadać tygodniami, jeśli się go nie pilnuje.</sub>

<img src="assets/dzielnik.svg" alt="" width="900">

### POLSKI GAMING - portal gier i konfigurator PC

Newsy, recenzje i agregowane oceny gier plus konfigurator, który pokazuje wyłącznie
podzespoły pasujące do siebie. Bez zgadywania i bez list, które nic nie znaczą.

<a href="https://polskigaming.rowienski-interactive.pl">
  <img src="assets/polski-gaming.jpg" alt="Polski Gaming - strona główna portalu" width="900">
</a>

<img src="assets/dzielnik.svg" alt="" width="900">

### ROWIEŃSKI INTERACTIVE - wizytówka warsztatu

Strona, z której wzięła się kolorystyka tego profilu. Pięć języków, zero szablonów,
100% kodu pisanego od zera.

<a href="https://rowienski-interactive.pl">
  <img src="assets/wizytowka.jpg" alt="Rowieński Interactive - strona główna" width="900">
</a>

<img src="assets/dzielnik.svg" alt="" width="900">

<img src="assets/naglowek-stan.svg" alt="Stan warsztatu" width="900">

<img src="assets/stan-warsztatu.svg" alt="Stan warsztatu - Podivo, Backhaul, Syndykat, Mnich, No Background Boss" width="900">

<img src="assets/dzielnik.svg" alt="" width="900">

<img src="assets/naglowek-serwery.svg" alt="Własne serwery" width="900">

Nic z tego nie stoi na hostingu z półki. Mam trzy maszyny, które sam postawiłem
i sam utrzymuję: dwie w serwerowni i jedną u siebie.

**Serwer aplikacji** obsługuje to, co widzą ludzie - strony, panele klientów, zdjęcia
i pliki oraz firmową pocztę. **Serwer bazy danych** stoi osobno i trzyma dane wszystkich
systemów: konta, rezerwacje, kartoteki. Rozdzieliłem je celowo, bo ruch z internetu
nigdy nie powinien dotykać danych bezpośrednio - obie maszyny rozmawiają ze sobą wyłącznie
prywatnym, szyfrowanym połączeniem, którego z zewnątrz w ogóle nie widać.
**Serwer domowy** trzyma archiwum projektów i kopie zapasowe, a przy okazji obsługuje
dysk sieciowy i multimedia.

<img src="assets/infrastruktura.svg" alt="Infrastruktura - serwer aplikacji i serwer bazy danych spięte prywatnym tunelem, obok serwer domowy" width="900">

| | |
|---|---|
| **Systemy** | Linux (Debian) - ten sam, na którym stoi duża część internetu |
| **Rozdzielenie** | każda usługa w osobnym, odizolowanym kontenerze |
| **Połączenie** | prywatny, szyfrowany tunel między maszynami, niewidoczny z sieci |
| **Szyfrowanie** | certyfikaty HTTPS odnawiane automatycznie, bez ręcznej roboty |
| **Poczta** | własny serwer pocztowy z podpisem potwierdzającym nadawcę |
| **Ochrona** | zapora sieciowa, limity zapytań, pułapki na boty, filtr ruchu |
| **Nadzór** | monitoring całą dobę, z powiadomieniem, gdy coś odstaje od normy |
| **Kopie** | codzienne kopie zapasowe plus niezależne archiwum u mnie |

Wszystkie usługi na serwerze aplikacji mieszczą się razem w około **85 MB pamięci** -
bo narzędzia dobieram do serwera, a nie odwrotnie. Kiedy trzeba było uruchomić pocztę,
popularne gotowce odpadły przy kilku gigabajtach, więc poszło rozwiązanie, które
robi dokładnie to samo za ułamek tego.

<img src="assets/dzielnik.svg" alt="" width="900">

<img src="assets/naglowek-stanowisko.svg" alt="Na czym pracuję" width="900">

<img src="assets/stanowisko.svg" alt="Jednostka robocza - specyfikacja komputera i stanowiska" width="900">

<img src="assets/dzielnik.svg" alt="" width="900">

<img src="assets/naglowek-czym.svg" alt="Czym pracuję" width="900">

<p>
  <img src="https://img.shields.io/badge/Claude_Code-0C0C11?style=for-the-badge&logo=anthropic&logoColor=E60000&labelColor=08080B" alt="Claude Code">
  <img src="https://img.shields.io/badge/React-0C0C11?style=for-the-badge&logo=react&logoColor=EDEDF2&labelColor=08080B" alt="React">
  <img src="https://img.shields.io/badge/Tailwind-0C0C11?style=for-the-badge&logo=tailwindcss&logoColor=EDEDF2&labelColor=08080B" alt="Tailwind CSS">
  <img src="https://img.shields.io/badge/Node.js-0C0C11?style=for-the-badge&logo=nodedotjs&logoColor=EDEDF2&labelColor=08080B" alt="Node.js">
  <img src="https://img.shields.io/badge/Fastify-0C0C11?style=for-the-badge&logo=fastify&logoColor=EDEDF2&labelColor=08080B" alt="Fastify">
</p>
<p>
  <img src="https://img.shields.io/badge/C%23-0C0C11?style=for-the-badge&logo=csharp&logoColor=EDEDF2&labelColor=08080B" alt="C#">
  <img src="https://img.shields.io/badge/Godot_4-0C0C11?style=for-the-badge&logo=godotengine&logoColor=EDEDF2&labelColor=08080B" alt="Godot 4">
  <img src="https://img.shields.io/badge/Python-0C0C11?style=for-the-badge&logo=python&logoColor=EDEDF2&labelColor=08080B" alt="Python">
  <img src="https://img.shields.io/badge/PostgreSQL-0C0C11?style=for-the-badge&logo=postgresql&logoColor=EDEDF2&labelColor=08080B" alt="PostgreSQL">
  <img src="https://img.shields.io/badge/Supabase-0C0C11?style=for-the-badge&logo=supabase&logoColor=EDEDF2&labelColor=08080B" alt="Supabase">
</p>
<p>
  <img src="https://img.shields.io/badge/Debian-0C0C11?style=for-the-badge&logo=debian&logoColor=EDEDF2&labelColor=08080B" alt="Debian">
  <img src="https://img.shields.io/badge/Docker-0C0C11?style=for-the-badge&logo=docker&logoColor=EDEDF2&labelColor=08080B" alt="Docker">
  <img src="https://img.shields.io/badge/nginx-0C0C11?style=for-the-badge&logo=nginx&logoColor=EDEDF2&labelColor=08080B" alt="nginx">
  <img src="https://img.shields.io/badge/WireGuard-0C0C11?style=for-the-badge&logo=wireguard&logoColor=EDEDF2&labelColor=08080B" alt="WireGuard">
  <img src="https://img.shields.io/badge/Capacitor-0C0C11?style=for-the-badge&logo=capacitor&logoColor=EDEDF2&labelColor=08080B" alt="Capacitor">
</p>

<img src="assets/dzielnik.svg" alt="" width="900">

<img src="assets/naglowek-liczby.svg" alt="Liczby" width="900">

<img src="assets/statystyki.svg" alt="Statystyki: 355 commitów w 12 miesięcy, 21 repozytoriów, rozkład języków" width="900">

<sub>Gotowe karty statystyk pokazałyby tu zero, bo wszystkie repozytoria są prywatne.
Ta liczy naprawdę - razem z commitami, których nie widać z zewnątrz.</sub>

<img src="assets/dzielnik.svg" alt="" width="900">

<img src="assets/naglowek-kontakt.svg" alt="Kontakt" width="900">

<p>
  <a href="https://rowienski-interactive.pl/kontakt"><img src="https://img.shields.io/badge/Porozmawiajmy_o_Twoim_projekcie-E60000?style=for-the-badge&logoColor=FFFFFF&labelColor=E60000" alt="Kontakt"></a>
  <a href="https://podivo.pl"><img src="https://img.shields.io/badge/Zobacz_demo_online-0C0C11?style=for-the-badge&logoColor=EDEDF2&labelColor=08080B" alt="Demo"></a>
</p>

<br>

<div align="center">
  <sub><b>Buduję rzeczy, które potem same pracują.</b></sub><br>
  <sub>Repozytoria produktów są prywatne - tutaj pokazuję, jak wyglądają od strony użytkownika.</sub>
</div>
