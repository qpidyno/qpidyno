"""Generuje animowane banery SVG dla profilu GitHub w stylu rowienski-interactive.pl.

Uzycie:
    python narzedzia/generuj.py                 - odbudowuje wszystkie grafiki
    python narzedzia/generuj.py --statystyki    - tylko karte z liczbami (tak robi to GitHub Action)

Dane do karty z liczbami pobiera z GitHub GraphQL API. Token bierze ze zmiennej
srodowiskowej GH_TOKEN albo GITHUB_TOKEN; bez tokena probuje lokalnego `gh`.
"""

from __future__ import annotations

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path(__file__).parent))

from svg_lib import (  # noqa: E402
    CZERWIEN,
    CZERWIEN_TEKST,
    LINIA,
    LINIA2,
    MGLA,
    MLEKO,
    PANEL,
    POPIOL,
    SADZA,
    SREBRO,
    mono,
    rajdhani,
    tekst,
)

LOGIN = "qpidyno"
WYJŚCIE = pathlib.Path(__file__).parent.parent / "assets"

WSPÓLNE_STYLE = """
    @media (prefers-reduced-motion: reduce) {
      * { animation: none !important; }
      .rev { transform: scaleX(1) !important; }
      .wjazd { opacity: 1 !important; transform: none !important; }
    }
"""


def romb(cx: float, cy: float, r: float, klasa: str = "") -> str:
    """Znak marki - romb z poswiata, jak logo na stronie."""
    w = r * 0.80
    d = f"M {cx:.1f} {cy - r:.1f} L {cx + w:.1f} {cy:.1f} L {cx:.1f} {cy + r:.1f} L {cx - w:.1f} {cy:.1f} Z"
    d2 = (
        f"M {cx:.1f} {cy - r * 0.62:.1f} L {cx + w * 0.62:.1f} {cy:.1f} "
        f"L {cx:.1f} {cy + r * 0.62:.1f} L {cx - w * 0.62:.1f} {cy:.1f} Z"
    )
    k = f' class="{klasa}"' if klasa else ""
    return f"""<g{k} filter="url(#poswiata)">
      <path d="{d}" fill="{PANEL}" stroke="{CZERWIEN}" stroke-width="1.6"/>
      <path d="{d2}" fill="none" stroke="{CZERWIEN_TEKST}" stroke-width="0.9" opacity="0.65"/>
      {tekst(rajdhani(700), "R", cx, cy + r * 0.30, r * 0.92, MLEKO, wyśrodkuj=True)}
    </g>"""


def defs_wspólne(szer: int, wys: int) -> str:
    return f"""<defs>
    <pattern id="siatka" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" stroke="#ffffff" stroke-width="1" opacity="0.024"/>
    </pattern>
    <radialGradient id="zarzewie" cx="18%" cy="88%" r="78%">
      <stop offset="0%" stop-color="{CZERWIEN}" stop-opacity="0.20"/>
      <stop offset="55%" stop-color="{CZERWIEN}" stop-opacity="0.05"/>
      <stop offset="100%" stop-color="{CZERWIEN}" stop-opacity="0"/>
    </radialGradient>
    <linearGradient id="biegacz" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{CZERWIEN}" stop-opacity="0"/>
      <stop offset="45%" stop-color="{CZERWIEN_TEKST}" stop-opacity="1"/>
      <stop offset="100%" stop-color="{CZERWIEN}" stop-opacity="0"/>
    </linearGradient>
    <linearGradient id="skan" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{CZERWIEN}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{CZERWIEN}" stop-opacity="0.13"/>
      <stop offset="100%" stop-color="{CZERWIEN}" stop-opacity="0"/>
    </linearGradient>
    <filter id="poswiata" x="-60%" y="-60%" width="220%" height="220%">
      <feGaussianBlur stdDeviation="3.2" result="rozmycie"/>
      <feMerge>
        <feMergeNode in="rozmycie"/>
        <feMergeNode in="SourceGraphic"/>
      </feMerge>
    </filter>
  </defs>"""


def tło(szer: int, wys: int) -> str:
    return f"""<rect width="{szer}" height="{wys}" fill="{SADZA}"/>
  <rect width="{szer}" height="{wys}" fill="url(#siatka)"/>
  <rect width="{szer}" height="{wys}" fill="url(#zarzewie)"/>"""


# --------------------------------------------------------------------------- HERO


def hero() -> str:
    szer, wys = 900, 250
    rj = rajdhani(700)
    mn = mono(500)

    nazwa_d, nazwa_w = rj.ścieżka("ROWIEŃSKI INTERACTIVE", 25, 0.05)
    hasło1 = "Budujemy rzeczy, które potem"
    hasło2 = "same pracują."
    h1_w = rj.szerokość(hasło1, 38)
    h2_w = rj.szerokość(hasło2, 38)

    prawy = "// GITHUB · QPIDYNO"
    prawy_w = mn.szerokość(prawy, 10, 0.18)

    style = f"""<style>
    .znak {{ transform-box: fill-box; transform-origin: 50% 50%;
             animation: wejscie-znaku 900ms cubic-bezier(.34,1.42,.5,1) both, tetno 3.4s ease-in-out 1s infinite; }}
    .rev {{ transform-box: fill-box; transform-origin: left center;
            animation: odslon 780ms cubic-bezier(.22,1,.36,1) 160ms both; }}
    .podpis {{ animation: wjazd-gora 700ms cubic-bezier(.22,1,.36,1) 420ms both; }}
    .h1 {{ animation: wjazd-dol 760ms cubic-bezier(.22,1,.36,1) 300ms both; }}
    .h2 {{ animation: wjazd-dol 760ms cubic-bezier(.22,1,.36,1) 460ms both, zar 3.2s ease-in-out 1.4s infinite; }}
    .meta {{ animation: pojaw 700ms ease-out 700ms both; }}
    .biegacz {{ animation: przesuw 2.6s cubic-bezier(.65,0,.35,1) 900ms infinite; }}
    .skanowanie {{ animation: skanuj 7s linear 1.2s infinite; }}
    .tetnica {{ animation: puls-zywy 2.4s ease-in-out infinite; }}

    @keyframes wejscie-znaku {{
      0%   {{ opacity: 0; transform: scaleX(.08) scale(.7) rotate(-20deg); }}
      55%  {{ opacity: 1; transform: scaleX(1.06) scale(1.1) rotate(4deg); }}
      78%  {{ transform: scale(.96) rotate(-2deg); }}
      100% {{ opacity: 1; transform: none; }}
    }}
    @keyframes tetno {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: .74; }} }}
    @keyframes odslon {{ from {{ transform: scaleX(0); }} to {{ transform: scaleX(1); }} }}
    @keyframes wjazd-gora {{ from {{ opacity: 0; transform: translateY(-6px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes wjazd-dol {{ from {{ opacity: 0; transform: translateY(14px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes pojaw {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes przesuw {{
      0%   {{ transform: translateX(-180px); }}
      100% {{ transform: translateX({szer}px); }}
    }}
    @keyframes skanuj {{
      0%   {{ transform: translateX(-340px); }}
      60%  {{ transform: translateX({szer}px); }}
      100% {{ transform: translateX({szer}px); }}
    }}
    @keyframes puls-zywy {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: .3; }} }}
{WSPÓLNE_STYLE}  </style>"""

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{szer}" height="{wys}" viewBox="0 0 {szer} {wys}" role="img" aria-label="Rowieński Interactive - software house">
  {defs_wspólne(szer, wys)}
  <clipPath id="ramy"><rect width="{szer}" height="{wys}"/></clipPath>
  <clipPath id="odsloniecie"><rect class="rev" x="98" y="34" width="{nazwa_w + 4:.0f}" height="34"/></clipPath>
  {style}
  <g clip-path="url(#ramy)">
    {tło(szer, wys)}
    <rect class="skanowanie" x="0" y="0" width="340" height="{wys}" fill="url(#skan)"/>

    <rect x="0" y="0" width="{szer}" height="2" fill="{CZERWIEN}" opacity="0.9"/>

    {romb(58, 60, 25, "znak")}

    <g clip-path="url(#odsloniecie)">
      <path d="{nazwa_d}" fill="{MLEKO}" transform="translate(98 58)"/>
    </g>
    <g class="podpis">
      {tekst(mn, "SOFTWARE HOUSE", 100, 78, 10, CZERWIEN_TEKST, tracking=0.30)}
    </g>

    <g class="meta">
      {tekst(mn, prawy, szer - 40 - prawy_w, 50, 10, MGLA, tracking=0.18)}
      <rect x="{szer - 40 - prawy_w:.0f}" y="58" width="{prawy_w:.0f}" height="1" fill="{LINIA2}"/>
    </g>

    <g class="h1">{tekst(rj, hasło1, 40, 158, 38, MLEKO)}</g>
    <g class="h2">{tekst(rj, hasło2, 40, 200, 38, CZERWIEN_TEKST)}</g>

    <g class="meta">
      <circle class="tetnica" cx="{szer - 118:.0f}" cy="196" r="3.2" fill="{CZERWIEN}"/>
      {tekst(mn, "NA ŻYWO", szer - 108, 200, 10, POPIOL, tracking=0.22)}
    </g>

    <rect x="0" y="{wys - 18}" width="{szer}" height="1" fill="{LINIA}"/>
    <g clip-path="url(#ramy)">
      <rect class="biegacz" x="0" y="{wys - 18}" width="180" height="1.6" fill="url(#biegacz)"/>
    </g>
    {tekst(mono(400), "Wszystko, co tu widzisz, działa naprawdę - nie makiety.", 40, wys - 26, 10, MGLA, tracking=0.08)}
  </g>
</svg>
"""


# ------------------------------------------------------------------- STAN WARSZTATU

PROJEKTY = [
    ("PODIVO", "SYSTEM DLA KLINIK", "DEMO ONLINE", CZERWIEN_TEKST),
    ("BACKHAUL", "SYMULACJA TRANSPORTOWA", "W PRODUKCJI", SREBRO),
    ("SYNDYKAT: KOD ULICY", "TEKSTOWE MMO", "ZAWIESZONY", MGLA),
    ("MNICH", "TŁUMACZ MODÓW", "DO POBRANIA", SREBRO),
    ("NO BACKGROUND BOSS", "OBRÓBKA GRAFIKI", "DO POBRANIA", SREBRO),
]


def stan_warsztatu() -> str:
    szer = 900
    góra = 108
    krok = 58
    wys = góra + krok * len(PROJEKTY) + 8

    rj = rajdhani(600)
    mn5 = mono(500)
    mn4 = mono(400)

    style_wierszy = "\n".join(
        f"    .w{i} {{ animation: wjazd-bok 620ms cubic-bezier(.22,1,.36,1) {240 + i * 110}ms both; }}"
        for i in range(len(PROJEKTY))
    )

    style = f"""<style>
    .naglowek {{ animation: pojaw 600ms ease-out both; }}
{style_wierszy}
    .tetnica {{ animation: puls-zywy 2.4s ease-in-out infinite; }}
    .buduje {{ animation: miganie 2.2s ease-in-out 1.2s infinite; }}
    .kreska {{ transform-box: fill-box; transform-origin: left center;
               animation: rozciagnij 900ms cubic-bezier(.22,1,.36,1) 200ms both; }}

    @keyframes wjazd-bok {{ from {{ opacity: 0; transform: translateX(-16px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes pojaw {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes puls-zywy {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: .3; }} }}
    @keyframes miganie {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: .5; }} }}
    @keyframes rozciagnij {{ from {{ transform: scaleX(0); }} to {{ transform: scaleX(1); }} }}
{WSPÓLNE_STYLE}  </style>"""

    wiersze = []
    for i, (nazwa, opis, status, kolor) in enumerate(PROJEKTY):
        y = góra + i * krok
        status_w = mn5.szerokość(status, 9, 0.16)
        pole_w = status_w + 26
        pole_x = szer - 40 - pole_w
        klasa_statusu = ' class="buduje"' if status == "W PRODUKCJI" else ""
        wiersze.append(
            f"""    <g class="w{i}">
      <rect x="40" y="{y - 26}" width="{szer - 80}" height="{krok - 10}" fill="{PANEL}" opacity="0.6"/>
      <rect x="40" y="{y - 26}" width="2" height="{krok - 10}" fill="{kolor}" opacity="0.75"/>
      {tekst(rj, nazwa, 60, y - 2, 19, MLEKO, tracking=0.02)}
      {tekst(mn4, opis, 60, y + 15, 9, MGLA, tracking=0.14)}
      <g{klasa_statusu}>
        <rect x="{pole_x:.0f}" y="{y - 8:.0f}" width="{pole_w:.0f}" height="24" fill="none" stroke="{kolor}" stroke-width="1" opacity="0.55"/>
        {tekst(mn5, status, pole_x + 13, y + 8, 9, kolor, tracking=0.16)}
      </g>
    </g>"""
        )

    tytuł_w = mn5.szerokość("STAN WARSZTATU", 11, 0.24)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{szer}" height="{wys}" viewBox="0 0 {szer} {wys}" role="img" aria-label="Stan warsztatu - lista projektów">
  {defs_wspólne(szer, wys)}
  {style}
  <rect width="{szer}" height="{wys}" fill="{SADZA}"/>
  <rect width="{szer}" height="{wys}" fill="url(#siatka)"/>
  <rect x="24" y="16" width="{szer - 48}" height="{wys - 32}" fill="none" stroke="{LINIA2}" stroke-width="1"/>

  <g class="naglowek">
    {tekst(mn5, "STAN WARSZTATU", 40, 44, 11, SREBRO, tracking=0.24)}
    <circle class="tetnica" cx="{szer - 118:.0f}" cy="40" r="3.2" fill="{CZERWIEN}"/>
    {tekst(mn5, "NA ŻYWO", szer - 108, 44, 10, POPIOL, tracking=0.22)}
  </g>
  <rect class="kreska" x="40" y="52" width="{tytuł_w:.0f}" height="1.6" fill="{CZERWIEN}"/>

{chr(10).join(wiersze)}
</svg>
"""


# ------------------------------------------------------------------------ DZIELNIK


def dzielnik() -> str:
    szer, wys = 900, 6
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{szer}" height="{wys}" viewBox="0 0 {szer} {wys}" role="img" aria-label="">
  <defs>
    <linearGradient id="bieg" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0%" stop-color="{CZERWIEN}" stop-opacity="0"/>
      <stop offset="50%" stop-color="{CZERWIEN_TEKST}" stop-opacity="1"/>
      <stop offset="100%" stop-color="{CZERWIEN}" stop-opacity="0"/>
    </linearGradient>
    <clipPath id="ram"><rect width="{szer}" height="{wys}"/></clipPath>
  </defs>
  <style>
    .b {{ animation: p 3.4s cubic-bezier(.65,0,.35,1) infinite; }}
    @keyframes p {{ 0% {{ transform: translateX(-220px); }} 100% {{ transform: translateX({szer}px); }} }}
    @media (prefers-reduced-motion: reduce) {{ .b {{ animation: none; }} }}
  </style>
  <g clip-path="url(#ram)">
    <rect y="2" width="{szer}" height="1" fill="{LINIA2}"/>
    <rect class="b" y="1.6" width="220" height="2" fill="url(#bieg)"/>
  </g>
</svg>
"""


# ---------------------------------------------------------------------- STATYSTYKI

# Odcienie marki zamiast kolorow GitHuba - profil ma zostac monochromatyczny z czerwienia.
ODCIENIE = ["#E60000", "#FF2D2D", "#C4C4CE", "#9A9AA8", "#7E7E8A", "#5A5A66", "#3C3C46"]


def statystyki(dane: dict) -> str:
    szer, wys = 900, 250
    rj = rajdhani(700)
    mn5 = mono(500)
    mn4 = mono(400)

    metryki = [
        (str(dane["commity"]), "COMMITÓW W 12 MIES."),
        (str(dane["repozytoria"]), "REPOZYTORIÓW"),
        (str(dane["jezyki_ile"]), "JĘZYKÓW W UŻYCIU"),
        (dane["od"], "PISZĘ KOD OD"),
    ]

    kafle = []
    kol_szer = (szer - 80) / 4
    for i, (liczba, etykieta) in enumerate(metryki):
        x = 40 + i * kol_szer
        kolor = CZERWIEN_TEKST if i == 0 else MLEKO
        kafle.append(
            f"""    <g class="m{i}">
      {tekst(rj, liczba, x, 86, 42, kolor)}
      {tekst(mn4, etykieta, x + 2, 106, 8.5, MGLA, tracking=0.16)}
    </g>"""
        )
        if i:
            kafle.append(f'    <rect x="{x - 18:.0f}" y="52" width="1" height="60" fill="{LINIA2}"/>')

    # Skumulowany pasek jezykow
    pasek_x, pasek_y, pasek_w, pasek_h = 40, 152, szer - 80, 14
    segmenty = []
    legenda = []
    biegnace_x = float(pasek_x)
    leg_x = 40.0
    for i, (nazwa, procent) in enumerate(dane["jezyki"]):
        w = pasek_w * procent / 100
        kolor = ODCIENIE[min(i, len(ODCIENIE) - 1)]
        segmenty.append(
            f'      <rect class="seg s{i}" x="{biegnace_x:.1f}" y="{pasek_y}" '
            f'width="{max(w - 1.5, 1):.1f}" height="{pasek_h}" fill="{kolor}"/>'
        )
        biegnace_x += w

        podpis = f"{nazwa} {procent:.1f}%"
        podpis_w = mn4.szerokość(podpis, 9, 0.1)
        legenda.append(
            f"""    <g class="l{i}">
      <rect x="{leg_x:.0f}" y="{pasek_y + 40:.0f}" width="8" height="8" fill="{kolor}"/>
      {tekst(mn4, podpis, leg_x + 14, pasek_y + 48, 9, SREBRO if i < 2 else POPIOL, tracking=0.1)}
    </g>"""
        )
        leg_x += podpis_w + 34

    style_m = "\n".join(
        f"    .m{i} {{ animation: wjazd 700ms cubic-bezier(.22,1,.36,1) {150 + i * 110}ms both; }}"
        for i in range(len(metryki))
    )
    style_s = "\n".join(
        f"    .s{i} {{ animation-delay: {600 + i * 90}ms; }}" for i in range(len(dane["jezyki"]))
    )
    style_l = "\n".join(
        f"    .l{i} {{ animation: pojaw 500ms ease-out {900 + i * 80}ms both; }}"
        for i in range(len(dane["jezyki"]))
    )

    przypis = f"Liczone razem z repozytoriami prywatnymi - stąd {dane['commity']}, a nie zero."

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{szer}" height="{wys}" viewBox="0 0 {szer} {wys}" role="img" aria-label="Statystyki GitHub">
  {defs_wspólne(szer, wys)}
  <style>
{style_m}
    .seg {{ transform-box: fill-box; transform-origin: left center;
            animation: rozciagnij 700ms cubic-bezier(.22,1,.36,1) both; }}
{style_s}
{style_l}
    .naglowek {{ animation: pojaw 600ms ease-out both; }}
    @keyframes wjazd {{ from {{ opacity: 0; transform: translateY(12px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes pojaw {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes rozciagnij {{ from {{ transform: scaleX(0); }} to {{ transform: scaleX(1); }} }}
{WSPÓLNE_STYLE}    @media (prefers-reduced-motion: reduce) {{ .seg {{ transform: scaleX(1) !important; }} }}
  </style>
  <rect width="{szer}" height="{wys}" fill="{SADZA}"/>
  <rect width="{szer}" height="{wys}" fill="url(#siatka)"/>
  <rect x="24" y="16" width="{szer - 48}" height="{wys - 32}" fill="none" stroke="{LINIA2}" stroke-width="1"/>

  <g class="naglowek">
    {tekst(mn5, "LICZBY", 40, 44, 11, SREBRO, tracking=0.24)}
    <rect x="40" y="52" width="{mn5.szerokość("LICZBY", 11, 0.24):.0f}" height="2" fill="{CZERWIEN}"/>
    {tekst(mn4, przypis, szer - 40 - mn4.szerokość(przypis, 9, 0.08), 44, 9, MGLA, tracking=0.08)}
  </g>

{chr(10).join(kafle)}

  <g>
{chr(10).join(segmenty)}
  </g>
  {tekst(mn4, "ROZKŁAD JĘZYKÓW", 40, 144, 8.5, MGLA, tracking=0.18)}

{chr(10).join(legenda)}
</svg>
"""


# ------------------------------------------------------------------ INFRASTRUKTURA

VPS1 = [
    "strony i panele klientów",
    "serwer zdjęć i plików",
    "pamięć podręczna",
    "szyfrowanie HTTPS",
    "firmowa poczta",
]
VPS3 = [
    "bazy trzech systemów",
    "konta i logowanie",
    "dostęp do danych przez API",
    "powiadomienia na żywo",
    "codzienne kopie zapasowe",
]
DOM = [
    "archiwum projektów i kopie zapasowe",
    "dysk sieciowy i multimedia dla domu",
]


def infrastruktura() -> str:
    szer, wys = 900, 520
    rj = rajdhani(600)
    mn5 = mono(500)
    mn4 = mono(400)

    pan_w = 366
    lewy_x = 40
    prawy_x = szer - 40 - pan_w
    pan_y = 92
    pan_h = 196

    def panel(x: float, tytuł: str, adres: str, system: str, usługi: list[str], klasa: str) -> str:
        wiersze = "\n".join(
            tekst(mn4, u, x + 22, pan_y + 96 + i * 21, 9.5, POPIOL, tracking=0.06)
            for i, u in enumerate(usługi)
        )
        return f"""  <g class="{klasa}">
    <rect x="{x}" y="{pan_y}" width="{pan_w}" height="{pan_h}" fill="{PANEL}" stroke="{LINIA2}" stroke-width="1"/>
    <rect x="{x}" y="{pan_y}" width="{pan_w}" height="2" fill="{CZERWIEN}" opacity="0.8"/>
    {tekst(rj, tytuł, x + 22, pan_y + 36, 20, MLEKO, tracking=0.02)}
    {tekst(mn4, adres, x + 22, pan_y + 54, 9, MGLA, tracking=0.1)}
    {tekst(mn5, system, x + 22, pan_y + 76, 9.5, CZERWIEN_TEKST, tracking=0.14)}
    <rect x="{x + 22}" y="{pan_y + 82}" width="{pan_w - 44}" height="1" fill="{LINIA}"/>
{wiersze}
  </g>"""

    tunel_y = pan_y + pan_h + 34
    kropki = "\n".join(
        f'    <circle class="pakiet p{i}" cx="{lewy_x + 20}" cy="{tunel_y}" r="3" fill="{CZERWIEN_TEKST}"/>'
        for i in range(4)
    )
    style_p = "\n".join(f"    .p{i} {{ animation-delay: {i * 900}ms; }}" for i in range(4))

    opis_tunelu = "WireGuard   -   tunel prywatny, poza internetem"

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{szer}" height="{wys}" viewBox="0 0 {szer} {wys}" role="img" aria-label="Infrastruktura - dwa serwery VPS spięte WireGuardem">
  {defs_wspólne(szer, wys)}
  <style>
    .lewy {{ animation: wjazd-l 700ms cubic-bezier(.22,1,.36,1) 200ms both; }}
    .prawy {{ animation: wjazd-p 700ms cubic-bezier(.22,1,.36,1) 340ms both; }}
    .naglowek {{ animation: pojaw 600ms ease-out both; }}
    .tetnica {{ animation: puls 2.4s ease-in-out infinite; }}
    .pakiet {{ animation: plyn 3.6s linear infinite; opacity: 0; }}
{style_p}
    .strzalka {{ animation: pojaw 600ms ease-out 700ms both; }}
    @keyframes wjazd-l {{ from {{ opacity: 0; transform: translateX(-20px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes wjazd-p {{ from {{ opacity: 0; transform: translateX(20px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes pojaw {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes puls {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: .3; }} }}
    @keyframes plyn {{
      0%   {{ opacity: 0; transform: translateX(0); }}
      8%   {{ opacity: 1; }}
      92%  {{ opacity: 1; }}
      100% {{ opacity: 0; transform: translateX({szer - 2 * lewy_x - 40}px); }}
    }}
{WSPÓLNE_STYLE}  </style>
  <rect width="{szer}" height="{wys}" fill="{SADZA}"/>
  <rect width="{szer}" height="{wys}" fill="url(#siatka)"/>
  <rect width="{szer}" height="{wys}" fill="url(#zarzewie)"/>

  <g class="naglowek">
    {tekst(mn5, "INFRASTRUKTURA", 40, 44, 11, SREBRO, tracking=0.24)}
    <rect x="40" y="52" width="{mn5.szerokość("INFRASTRUKTURA", 11, 0.24):.0f}" height="2" fill="{CZERWIEN}"/>
    <circle class="tetnica" cx="{szer - 118:.0f}" cy="40" r="3.2" fill="{CZERWIEN}"/>
    {tekst(mn5, "PRODUKCJA", szer - 108, 44, 10, POPIOL, tracking=0.22)}
  </g>

  <g class="strzalka">
    {tekst(mn4, "internet", lewy_x + pan_w / 2 - mn4.szerokość("internet", 9, 0.16) / 2, 74, 9, MGLA, tracking=0.16)}
    <path d="M {lewy_x + pan_w / 2:.0f} 78 L {lewy_x + pan_w / 2:.0f} 90" stroke="{LINIA2}" stroke-width="1"/>
    <path d="M {lewy_x + pan_w / 2 - 3:.0f} 86 L {lewy_x + pan_w / 2:.0f} 91 L {lewy_x + pan_w / 2 + 3:.0f} 86" fill="none" stroke="{LINIA2}" stroke-width="1"/>
  </g>

{panel(lewy_x, "APLIKACJE", "2 vCore  ·  4 GB RAM  ·  140 GB", "Debian 12", VPS1, "lewy")}
{panel(prawy_x, "BAZA DANYCH", "6 vCore  ·  12 GB RAM  ·  100 GB NVMe", "Debian 13", VPS3, "prawy")}

  <line x1="{lewy_x + 20}" y1="{tunel_y}" x2="{szer - lewy_x - 20}" y2="{tunel_y}" stroke="{LINIA2}" stroke-width="1" stroke-dasharray="4 4"/>
{kropki}
  {tekst(mn4, opis_tunelu, szer / 2 - mn4.szerokość(opis_tunelu, 9, 0.1) / 2, tunel_y + 26, 9, MGLA, tracking=0.1)}

{dom_panel(szer, lewy_x, tunel_y + 62, prawy_x + pan_w / 2, rj, mn4, mn5)}
</svg>
"""


def dom_panel(szer: int, x: float, y: float, strzałka_x: float, rj, mn4, mn5) -> str:
    """Trzecia maszyna - serwer w domu, opisany bez szczegolow technicznych."""
    w = szer - 2 * x
    h = 96
    wiersze = "\n".join(
        tekst(mn4, "-  " + u, x + 200, y + 44 + i * 22, 9.5, POPIOL, tracking=0.06)
        for i, u in enumerate(DOM)
    )
    podpis = "kopie zapasowe"
    return f"""  <g class="dom">
    <path d="M {strzałka_x:.0f} {y - 56:.0f} L {strzałka_x:.0f} {y - 8:.0f}" stroke="{LINIA2}" stroke-width="1" stroke-dasharray="4 4"/>
    <path d="M {strzałka_x - 3:.0f} {y - 13:.0f} L {strzałka_x:.0f} {y - 7:.0f} L {strzałka_x + 3:.0f} {y - 13:.0f}" fill="none" stroke="{LINIA2}" stroke-width="1"/>
    {tekst(mn4, podpis, strzałka_x + 12, y - 30, 9, MGLA, tracking=0.1)}
    <rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{PANEL}" stroke="{LINIA2}" stroke-width="1"/>
    <rect x="{x}" y="{y}" width="{w}" height="2" fill="{SREBRO}" opacity="0.4"/>
    {tekst(rj, "SERWER DOMOWY", x + 22, y + 38, 20, MLEKO, tracking=0.02)}
    {tekst(mn4, "u nas, nie w chmurze", x + 22, y + 58, 9, MGLA, tracking=0.1)}
    <rect x="{x + 176}" y="{y + 20}" width="1" height="{h - 40}" fill="{LINIA}"/>
{wiersze}
  </g>"""


# ------------------------------------------------------------------- STANOWISKO

JEDNOSTKA = [
    ("KARTA GRAFICZNA", "MSI GeForce RTX 4080 SUPER VENTUS 3X OC 16GB", True),
    ("PROCESOR", "AMD Ryzen 9 9950X3D", True),
    ("CHŁODZENIE", "Arctic Liquid Freezer III ARGB 420  3x140 mm", False),
    ("PAMIĘĆ", "Corsair 96GB (2x48GB) DDR5 6000 CL30 VENGEANCE", True),
    ("PŁYTA GŁÓWNA", "MSI MAG X870 TOMAHAWK WIFI", False),
    ("DYSK NVMe I", "Lexar 1TB M.2 PCIe Gen4 NM790", False),
    ("DYSK NVMe II", "Lexar 2TB M.2 PCIe Gen4 NM790", False),
    ("KARTA DŹWIĘKOWA", "Sound Blaster AE-7", False),
    ("OBUDOWA", "Deepcool MORPHEUS", False),
    ("WENTYLATORY", "6x SILENTIUMPC Stella HP RGB 140", False),
    ("ZASILACZ", "Gigabyte UD1000GM PG5 1000W 80 Plus Gold", False),
]

OBRAZ = [
    ("MONITOR I", "LG UltraGear 32GS95UE-B OLED", True),
    ("MONITOR II", "BenQ ZOWIE XL2411", False),
    ("MYSZ", "Razer DeathAdder V4 Pro", False),
    ("KLAWIATURA", "Attack Shark x68HE PRO", False),
    ("PODKŁADKA", "Saturn PRO XXL SOFT RED", False),
]

DŹWIĘK = [
    ("STUDYJNE", "Beyerdynamic DT770 PRO LE", True),
    ("GAMINGOWE", "Logitech G PRO X 2 Lightspeed", False),
    ("GŁOŚNIKI", "Logitech Z906", False),
    ("MIKROFON", "Rode NT1 5th", True),
    ("INTERFEJS AUDIO", "RODE AI-1", False),
]


def stanowisko() -> str:
    szer = 900
    rj = rajdhani(600)
    mn5 = mono(500)
    mn4 = mono(400)

    krok = 27
    lewa_x = 40
    prawa_x = 468
    start_y = 112

    licznik = [0]

    def sekcja(x: float, y: float, tytuł: str, pozycje: list, etykieta_w: float) -> tuple[str, float]:
        części = [
            f"""    <g class="r{licznik[0]}">
      {tekst(mn5, tytuł, x, y, 10, CZERWIEN_TEKST, tracking=0.22)}
      <rect x="{x}" y="{y + 7}" width="{szer / 2 - 108:.0f}" height="1" fill="{LINIA}"/>
    </g>"""
        ]
        licznik[0] += 1
        for i, (etykieta, wartość, akcent) in enumerate(pozycje):
            wy = y + 26 + i * krok
            części.append(
                f"""    <g class="r{licznik[0]}">
      {tekst(mn4, etykieta, x, wy, 8.5, MGLA, tracking=0.12)}
      {tekst(mn4, wartość, x + etykieta_w, wy, 9.5, MLEKO if akcent else SREBRO, tracking=0.04)}
    </g>"""
            )
            licznik[0] += 1
        return "\n".join(części), y + 26 + len(pozycje) * krok

    lewa, dół_l = sekcja(lewa_x, start_y, "JEDNOSTKA", JEDNOSTKA, 118)
    prawa_1, dół_p = sekcja(prawa_x, start_y, "OBRAZ I STEROWANIE", OBRAZ, 118)
    prawa_2, dół_p2 = sekcja(prawa_x, dół_p + 22, "DŹWIĘK", DŹWIĘK, 118)

    wys = int(max(dół_l, dół_p2)) + 34

    style_r = "\n".join(
        f"    .r{i} {{ animation: wjazd 480ms cubic-bezier(.22,1,.36,1) {120 + i * 34}ms both; }}"
        for i in range(licznik[0])
    )

    podpis = "Na tym powstaje kod, grafika i dźwięk."

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{szer}" height="{wys}" viewBox="0 0 {szer} {wys}" role="img" aria-label="Stanowisko pracy - specyfikacja komputera">
  {defs_wspólne(szer, wys)}
  <style>
{style_r}
    .naglowek {{ animation: pojaw 600ms ease-out both; }}
    .tetnica {{ animation: puls 2.4s ease-in-out infinite; }}
    @keyframes wjazd {{ from {{ opacity: 0; transform: translateX(-10px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes pojaw {{ from {{ opacity: 0; }} to {{ opacity: 1; }} }}
    @keyframes puls {{ 0%,100% {{ opacity: 1; }} 50% {{ opacity: .3; }} }}
{WSPÓLNE_STYLE}  </style>
  <rect width="{szer}" height="{wys}" fill="{SADZA}"/>
  <rect width="{szer}" height="{wys}" fill="url(#siatka)"/>
  <rect width="{szer}" height="{wys}" fill="url(#zarzewie)"/>
  <rect x="24" y="16" width="{szer - 48}" height="{wys - 32}" fill="none" stroke="{LINIA2}" stroke-width="1"/>

  <g class="naglowek">
    {tekst(rj, "JEDNOSTKA ROBOCZA", 40, 58, 22, MLEKO, tracking=0.02)}
    {tekst(mn4, podpis, 40, 78, 9.5, MGLA, tracking=0.1)}
    <circle class="tetnica" cx="{szer - 118:.0f}" cy="52" r="3.2" fill="{CZERWIEN}"/>
    {tekst(mn5, "W UŻYCIU", szer - 108, 56, 10, POPIOL, tracking=0.22)}
  </g>
  <rect x="40" y="90" width="{szer - 80}" height="1" fill="{LINIA2}"/>
  <rect x="{szer / 2 - 18:.0f}" y="{start_y - 8}" width="1" height="{wys - start_y - 20}" fill="{LINIA}"/>

{lewa}
{prawa_1}
{prawa_2}
</svg>
"""


def nagłówek(tytuł: str, opis: str) -> str:
    """Pasek naglowka sekcji - mono uppercase + czerwona kreska, jak etykiety na stronie."""
    szer, wys = 900, 62
    mn5 = mono(500)
    mn4 = mono(400)
    tytuł_w = mn5.szerokość(tytuł, 12, 0.26)
    opis_w = mn4.szerokość(opis, 9.5, 0.12)

    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{szer}" height="{wys}" viewBox="0 0 {szer} {wys}" role="img" aria-label="{tytuł}">
  <style>
    .t {{ animation: p 600ms ease-out both; }}
    .o {{ animation: p 600ms ease-out 220ms both; }}
    .k {{ transform-box: fill-box; transform-origin: left center;
          animation: r 800ms cubic-bezier(.22,1,.36,1) 120ms both; }}
    .l {{ transform-box: fill-box; transform-origin: right center;
          animation: r 900ms cubic-bezier(.22,1,.36,1) 300ms both; }}
    @keyframes p {{ from {{ opacity: 0; transform: translateX(-10px); }} to {{ opacity: 1; transform: none; }} }}
    @keyframes r {{ from {{ transform: scaleX(0); }} to {{ transform: scaleX(1); }} }}
    @media (prefers-reduced-motion: reduce) {{
      * {{ animation: none !important; }}
      .k, .l {{ transform: scaleX(1) !important; }}
    }}
  </style>
  <rect width="{szer}" height="{wys}" fill="{SADZA}"/>
  <g class="t">{tekst(mn5, tytuł, 0, 26, 12, MLEKO, tracking=0.26)}</g>
  <rect class="k" x="0" y="36" width="{tytuł_w:.0f}" height="2" fill="{CZERWIEN}"/>
  <g class="o">{tekst(mn4, opis, 0, 54, 9.5, MGLA, tracking=0.12)}</g>
  <rect class="l" x="{szer - 260}" y="26" width="260" height="1" fill="{LINIA2}"/>
</svg>
"""


ZAPYTANIE = """
query($login: String!) {
  user(login: $login) {
    createdAt
    repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {
      totalCount
      nodes {
        languages(first: 12, orderBy: { field: SIZE, direction: DESC }) {
          edges { size node { name } }
        }
      }
    }
    contributionsCollection {
      totalCommitContributions
      restrictedContributionsCount
    }
  }
}
"""


def pobierz_z_api() -> dict:
    """Odpytuje GitHub GraphQL. Prywatne commity widac tylko z tokenem uzytkownika."""
    import json
    import os
    import subprocess
    import urllib.request

    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if not token:
        # Lokalnie wystarczy zalogowany `gh` - nie trzeba nigdzie wklejac tokena.
        try:
            token = subprocess.run(
                ["gh", "auth", "token"],
                capture_output=True,
                text=True,
                shell=(os.name == "nt"),
                timeout=20,
            ).stdout.strip()
        except (OSError, subprocess.SubprocessError):
            token = ""
    if not token:
        raise SystemExit(
            "Brak tokena. Lokalnie: `gh auth login`. "
            "W GitHub Actions: ustaw sekret STATYSTYKI_TOKEN (uprawnienie read:user)."
        )

    ciało = json.dumps({"query": ZAPYTANIE, "variables": {"login": LOGIN}}).encode("utf-8")
    żądanie = urllib.request.Request(
        "https://api.github.com/graphql",
        data=ciało,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": f"{LOGIN}-profil",
        },
    )
    with urllib.request.urlopen(żądanie, timeout=30) as odpowiedź:
        wynik = json.loads(odpowiedź.read().decode("utf-8"))

    if "errors" in wynik:
        raise SystemExit(f"GitHub API zwrocilo blad: {wynik['errors']}")
    return wynik


def wczytaj_dane() -> dict:
    """Sprowadza odpowiedz GitHub GraphQL do liczb na karte."""
    import datetime as dt

    user = pobierz_z_api()["data"]["user"]
    wkład = user["contributionsCollection"]

    rozmiary: dict[str, int] = {}
    for repo in user["repositories"]["nodes"]:
        for krawędź in repo["languages"]["edges"]:
            rozmiary[krawędź["node"]["name"]] = (
                rozmiary.get(krawędź["node"]["name"], 0) + krawędź["size"]
            )

    suma = sum(rozmiary.values()) or 1
    posortowane = sorted(rozmiary.items(), key=lambda p: -p[1])
    główne = [(n, r / suma * 100) for n, r in posortowane[:6]]
    reszta = sum(r for _, r in posortowane[6:]) / suma * 100
    if reszta > 0.5:
        główne.append(("Pozostałe", reszta))

    założone = dt.datetime.fromisoformat(user["createdAt"].replace("Z", "+00:00"))

    return {
        "commity": wkład["totalCommitContributions"] + wkład["restrictedContributionsCount"],
        "repozytoria": user["repositories"]["totalCount"],
        "jezyki_ile": len(rozmiary),
        "od": f"{założone.month:02d}.{założone.year}",
        "jezyki": główne,
    }


def zapisz(nazwa: str, treść: str) -> None:
    WYJŚCIE.mkdir(parents=True, exist_ok=True)
    plik = WYJŚCIE / nazwa
    plik.write_text(treść, encoding="utf-8")
    print(f"{plik}  {len(treść.encode('utf-8')) / 1024:.1f} KB")


if __name__ == "__main__":
    if "--statystyki" in sys.argv:
        zapisz("statystyki.svg", statystyki(wczytaj_dane()))
        raise SystemExit(0)

    zapisz("hero.svg", hero())
    zapisz("stan-warsztatu.svg", stan_warsztatu())
    zapisz("dzielnik.svg", dzielnik())

    nagłówki = {
        "naglowek-kim.svg": ("// KIM JESTEŚMY", "dwóch braci, pięć projektów, zero szablonów"),
        "naglowek-warsztat.svg": ("// CO ZBUDOWALIŚMY", "rzeczy, które można otworzyć i sprawdzić"),
        "naglowek-stan.svg": ("// STAN WARSZTATU", "co żyje, co powstaje, co czeka"),
        "naglowek-serwery.svg": ("// WŁASNE SERWERY", "stawiamy i utrzymujemy je sami, bez hostingu z półki"),
        "naglowek-stanowisko.svg": ("// NA CZYM PRACUJEMY", "sprzęt, przy którym to wszystko powstaje"),
        "naglowek-czym.svg": ("// CZYM PRACUJEMY", "stos technologiczny, bez upiększeń"),
        "naglowek-liczby.svg": ("// LICZBY", "commity prywatne też się liczą"),
        "naglowek-kontakt.svg": ("// KONTAKT", "odzywamy się tego samego dnia"),
    }
    for nazwa, (t, o) in nagłówki.items():
        zapisz(nazwa, nagłówek(t, o))

    zapisz("infrastruktura.svg", infrastruktura())
    zapisz("stanowisko.svg", stanowisko())
    zapisz("statystyki.svg", statystyki(wczytaj_dane()))
