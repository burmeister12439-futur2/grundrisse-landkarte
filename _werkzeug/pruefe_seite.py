#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pruefe_seite.py — die Pruefung, die am 22.09.2026 gefehlt hat.

Anlass: Bei der Umschaltung auf die Gliederung A bis I stand ein schliessendes
</details> an der falschen Stelle. Die Fragen zu Abschnitt D lagen dadurch in
einem zugeklappten Werkstatt-Fenster und waren fuer jeden Leser unsichtbar.
Keine unserer Pruefungen hat das gefunden, weil alle gezaehlt haben. Die Zahl
der <details> und </details> stimmte in jedem Commit, fuenf zu fuenf. Falsch
war die Position, und Position prueft kein Zaehler.

Dieses Werkzeug prueft deshalb drei Dinge, die ein Zaehler nicht sehen kann:

  1 Verschachtelung. Jedes oeffnende Element muss an der richtigen Stelle
    geschlossen werden, geprueft mit einem Stapel und nicht mit einer Summe.
  2 Sichtbarkeit. Kein Eingabefeld und keine Fragen-Ueberschrift darf in einem
    <details> ohne open-Attribut stehen. Wer die Seite liest, ohne zu klicken,
    muss alles sehen, was ihn zur Antwort auffordert.
  3 Leseblick. Ein Bericht darueber, was ein Leser mit geschlossenen Fenstern
    tatsaechlich sieht: je Abschnitt die Ueberschrift, die Fragenbloecke und
    die Zahl der sichtbaren Felder. Zum Ansehen, nicht zum Zaehlen.

Dazu die beiden alten Pruefungen, die schon einmal etwas gefunden haben:
tote Sprungmarken und doppelte Kennungen.

Aufruf:  python3 _werkzeug/pruefe_seite.py [datei ...]
Ohne Angabe wird index.html geprueft.
Rueckgabe: 0 bestanden, 1 Befunde. Nur Standardbibliothek, kein Browser.
"""
import sys, os
from html.parser import HTMLParser

LEER = {"area","base","br","col","embed","hr","img","input","link","meta",
        "param","source","track","wbr"}
# Elemente, die der Leser ohne Klick sehen muss
PFLICHT_SICHTBAR = {"textarea","input","select"}


class Seite(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stapel = []            # (tag, zeile, attrs)
        self.fehler = []            # Verschachtelung
        self.versteckt = []         # (was, zeile, fenster)
        self.ids = {}
        self.anker = []
        self.abschnitte = []        # (id, zeile)
        self.sicht = []             # Leseblick-Eintraege
        self._h = None              # laufende Ueberschrift
        self._htext = ""

    # --- Hilfen -------------------------------------------------------
    def _zu(self):
        """Name des naechsten geschlossenen <details> im Stapel, sonst None."""
        for tag, zeile, attrs in reversed(self.stapel):
            if tag == "details" and "open" not in attrs:
                return attrs.get("id") or ("Zeile %d" % zeile)
        return None

    def _abschnitt(self):
        for tag, zeile, attrs in reversed(self.stapel):
            if tag == "section":
                return attrs.get("id") or ("Zeile %d" % zeile)
        return "(ausserhalb)"

    # --- Parser -------------------------------------------------------
    def handle_starttag(self, tag, attrs):
        z = self.getpos()[0]
        a = {k: (v if v is not None else "") for k, v in attrs}
        if "id" in a:
            self.ids.setdefault(a["id"], []).append(z)
        if tag == "a" and a.get("href", "").startswith("#") and len(a["href"]) > 1:
            self.anker.append((a["href"][1:], z))
        if tag == "section":
            self.abschnitte.append((a.get("id") or str(z), z))
        if tag in PFLICHT_SICHTBAR:
            f = self._zu()
            if f:
                self.versteckt.append(("%s %s" % (tag, a.get("id") or a.get("data-frage") or ""), z, f))
            else:
                self.sicht.append(("feld", self._abschnitt(), z, a.get("data-frage") or a.get("id") or tag))
        if tag in ("h2", "h3", "h4"):
            self._h, self._htext = (tag, z, self._zu(), self._abschnitt()), ""
        if tag not in LEER:
            self.stapel.append((tag, z, a))

    def handle_data(self, d):
        if self._h is not None:
            self._htext += d

    def handle_endtag(self, tag):
        z = self.getpos()[0]
        if self._h is not None and tag == self._h[0]:
            name, zeile, fenster, absch = self._h
            t = " ".join(self._htext.split())
            if t.startswith("Fragen zu") or t.startswith("Weitere Fragen zu"):
                if fenster:
                    self.versteckt.append(("Ueberschrift „%s“" % t, zeile, fenster))
                else:
                    self.sicht.append(("fragenblock", absch, zeile, t))
            elif name in ("h2",) and not fenster:
                self.sicht.append(("ueberschrift", absch, zeile, t))
            self._h = None
        if tag in LEER:
            return
        if not self.stapel:
            self.fehler.append("Zeile %d: </%s> ohne oeffnendes Element" % (z, tag))
            return
        if self.stapel[-1][0] == tag:
            self.stapel.pop(); return
        # Fehlpaarung: suchen, wie weit zurueck
        for i in range(len(self.stapel) - 1, -1, -1):
            if self.stapel[i][0] == tag:
                offen = ", ".join("<%s> aus Zeile %d" % (t, l) for t, l, _ in self.stapel[i+1:])
                self.fehler.append(
                    "Zeile %d: </%s> schliesst, obwohl noch offen ist: %s" % (z, tag, offen))
                del self.stapel[i:]
                return
        self.fehler.append("Zeile %d: </%s> ohne oeffnendes Element" % (z, tag))


def pruefe(pfad):
    with open(pfad, encoding="utf-8") as f:
        roh = f.read()
    s = Seite(); s.feed(roh); s.close()

    befunde = []
    print("=" * 72)
    print("PRUEFUNG  %s" % pfad)
    print("=" * 72)

    print("\n1 Verschachtelung")
    if s.fehler:
        for f in s.fehler:
            print("   BEFUND  " + f)
        befunde.append("%d Verschachtelungsfehler" % len(s.fehler))
    if s.stapel:
        for t, z, _ in s.stapel:
            print("   BEFUND  <%s> aus Zeile %d wird nie geschlossen" % (t, z))
        befunde.append("%d nie geschlossene Elemente" % len(s.stapel))
    if not s.fehler and not s.stapel:
        print("   in Ordnung, der Stapel geht auf")

    print("\n2 Sichtbarkeit ohne Klick")
    if s.versteckt:
        for was, z, fenster in s.versteckt:
            print("   BEFUND  %s in Zeile %d steckt im geschlossenen Fenster „%s“" % (was, z, fenster))
        befunde.append("%d unsichtbare Pflichtelemente" % len(s.versteckt))
    else:
        print("   in Ordnung, kein Eingabefeld und keine Fragen-Ueberschrift im geschlossenen Fenster")

    print("\n3 Leseblick, was ein Leser ohne Klick sieht")
    je = {}
    for art, absch, z, text in s.sicht:
        je.setdefault(absch, {"h2": [], "bloecke": [], "felder": 0})
        if art == "ueberschrift": je[absch]["h2"].append(text)
        elif art == "fragenblock": je[absch]["bloecke"].append(text)
        else: je[absch]["felder"] += 1
    for absch, _z in s.abschnitte:
        d = je.get(absch)
        if not d: continue
        titel = d["h2"][0] if d["h2"] else "(ohne Ueberschrift)"
        bl = ", ".join(d["bloecke"]) if d["bloecke"] else "kein Fragenblock"
        print("   %-10s %-46s %s  |  %d Felder" % (absch, titel[:46], bl[:60], d["felder"]))

    print("\n4 Tote Sprungmarken")
    tot = sorted({n for n, z in s.anker if n not in s.ids})
    if tot:
        for n in tot: print("   BEFUND  #%s zeigt auf nichts" % n)
        befunde.append("%d tote Sprungmarken" % len(tot))
    else:
        print("   in Ordnung, alle %d Sprungmarken finden ihr Ziel" % len(s.anker))

    print("\n5 Doppelte Kennungen")
    dop = {k: v for k, v in s.ids.items() if len(v) > 1}
    if dop:
        for k, v in sorted(dop.items()):
            print("   BEFUND  id=\"%s\" steht in den Zeilen %s" % (k, ", ".join(map(str, v))))
        befunde.append("%d doppelte Kennungen" % len(dop))
    else:
        print("   in Ordnung, alle %d Kennungen sind eindeutig" % len(s.ids))

    print()
    if befunde:
        print("NICHT BESTANDEN: " + "; ".join(befunde))
    else:
        print("BESTANDEN")
    return 1 if befunde else 0


if __name__ == "__main__":
    dateien = sys.argv[1:] or ["index.html"]
    rc = 0
    for d in dateien:
        if not os.path.exists(d):
            print("Datei fehlt: %s" % d); rc = 1; continue
        rc = max(rc, pruefe(d))
    sys.exit(rc)
