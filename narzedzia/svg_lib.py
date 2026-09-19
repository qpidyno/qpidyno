"""Zamiana tekstu na sciezki SVG przy uzyciu oryginalnych fontow strony."""

from __future__ import annotations

import pathlib

from fontTools.misc.transform import Transform
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont

FONTS_DIR = pathlib.Path(__file__).parent / "fonty"

# Paleta z tailwind.config.js strony rowienski-interactive.pl
SADZA = "#08080B"
NOC = "#0A0A0E"
PANEL = "#0C0C11"
LINIA = "#16161D"
LINIA2 = "#26262F"
MLEKO = "#EDEDF2"
SREBRO = "#C4C4CE"
POPIOL = "#9A9AA8"
MGLA = "#7E7E8A"
CZERWIEN = "#E60000"
CZERWIEN_TEKST = "#FF2D2D"
ZIELEN = "#8BE04E"


class Krój:
    """Jeden krój w jednej grubosci - laczy podzbiory latin i latin-ext."""

    _cache: dict[str, "Krój"] = {}

    def __init__(self, nazwy: list[str]) -> None:
        self.fonty = [TTFont(str(FONTS_DIR / n)) for n in nazwy]
        self._cmapy = [f.getBestCmap() for f in self.fonty]
        self._zestawy = [f.getGlyphSet() for f in self.fonty]

    @classmethod
    def weź(cls, rodzina: str, waga: int) -> "Krój":
        klucz = f"{rodzina}-{waga}"
        if klucz not in cls._cache:
            cls._cache[klucz] = cls(
                [f"{rodzina}-{waga}-latin.woff2", f"{rodzina}-{waga}-latin-ext.woff2"]
            )
        return cls._cache[klucz]

    def _glif(self, znak: str):
        kod = ord(znak)
        for i, cmap in enumerate(self._cmapy):
            if kod in cmap:
                return i, cmap[kod]
        return None, None

    def ścieżka(self, tekst: str, rozmiar: float, tracking: float = 0.0) -> tuple[str, float]:
        """Zwraca (atrybut d, szerokosc w px). Baseline w y=0, tekst nad nia.

        tracking podawany w em, tak jak letter-spacing w CSS.
        """
        części: list[str] = []
        x = 0.0
        for znak in tekst:
            if znak == " ":
                idx, gname = self._glif(" ")
                if idx is None:
                    x += rozmiar * 0.28 + rozmiar * tracking
                    continue
            idx, gname = self._glif(znak)
            if idx is None:
                x += rozmiar * 0.5 + rozmiar * tracking
                continue

            font = self.fonty[idx]
            zestaw = self._zestawy[idx]
            upem = font["head"].unitsPerEm
            skala = rozmiar / upem

            pen = SVGPathPen(zestaw, ntos=lambda v: f"{v:.2f}")
            tpen = TransformPen(pen, Transform(skala, 0, 0, -skala, x, 0))
            zestaw[gname].draw(tpen)
            d = pen.getCommands()
            if d:
                części.append(d)

            x += font["hmtx"][gname][0] * skala + rozmiar * tracking

        if tekst and tracking:
            x -= rozmiar * tracking
        return " ".join(części), x

    def szerokość(self, tekst: str, rozmiar: float, tracking: float = 0.0) -> float:
        return self.ścieżka(tekst, rozmiar, tracking)[1]


def tekst(
    krój: Krój,
    treść: str,
    x: float,
    y: float,
    rozmiar: float,
    kolor: str,
    tracking: float = 0.0,
    opacity: float | None = None,
    klasa: str | None = None,
    wyśrodkuj: bool = False,
    dodatkowe: str = "",
) -> str:
    d, szer = krój.ścieżka(treść, rozmiar, tracking)
    if not d:
        return ""
    if wyśrodkuj:
        x = x - szer / 2
    atrybuty = [f'd="{d}"', f'fill="{kolor}"']
    atrybuty.append(f'transform="translate({x:.2f} {y:.2f})"')
    if opacity is not None:
        atrybuty.append(f'opacity="{opacity}"')
    if klasa:
        atrybuty.append(f'class="{klasa}"')
    if dodatkowe:
        atrybuty.append(dodatkowe)
    return "<path " + " ".join(atrybuty) + "/>"


def rajdhani(waga: int = 700) -> Krój:
    return Krój.weź("rajdhani", waga)


def mono(waga: int = 500) -> Krój:
    return Krój.weź("jetbrains-mono", waga)
