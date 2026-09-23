#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""pruefe_protokoll.py — haelt das Protokoll der Browserpruefung an die Seite.

Die Browserpruefung braucht Playwright und laeuft deshalb nicht auf diesem
Rechner, sondern dort, wo Playwright liegt. Damit sie trotzdem nicht still
ausfallen kann, schreibt sie ein Protokoll mit dem SHA-256 der geprueften
Seite. Dieses Werkzeug prueft dreierlei und wird vom Push-Haken aufgerufen:

  1 Das Protokoll gibt es.
  2 Sein SHA-256 ist der der Seite, die gleich hochgeladen wird. Jede
    Aenderung an der Seite macht das Protokoll also ungueltig.
  3 Sein Ergebnis lautet bestanden.

Aufruf:  python3 _werkzeug/pruefe_protokoll.py <seite> <protokoll.json>
Rueckgabe: 0 bestanden, 1 Befunde.
"""
import sys, os, json, hashlib

def main(seite, prot):
    print("\n8 Protokoll der Browserpruefung")
    if not os.path.exists(prot):
        print("   BEFUND  es gibt kein Protokoll %s. Die Browserpruefung ist nie gelaufen." % prot)
        return 1
    ist = hashlib.sha256(open(seite, "rb").read()).hexdigest()
    try:
        d = json.load(open(prot, encoding="utf-8"))
    except Exception as e:
        print("   BEFUND  das Protokoll ist nicht lesbar: %s" % e); return 1
    fehler = 0
    if d.get("sha256") != ist:
        print("   BEFUND  das Protokoll gehoert zu einem anderen Stand der Seite.")
        print("           Seite      %s" % ist)
        print("           Protokoll  %s" % d.get("sha256"))
        print("           Die Browserpruefung muss fuer diesen Stand neu laufen.")
        fehler = 1
    if d.get("ergebnis") != "bestanden":
        print("   BEFUND  die Browserpruefung war nicht bestanden: %s" % "; ".join(d.get("befunde", [])))
        fehler = 1
    if not fehler:
        print("   in Ordnung, Browserpruefung bestanden am %s, passend zu diesem Stand"
              % d.get("zeitpunkt", "(ohne Zeitpunkt)"))
    return fehler

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Aufruf: pruefe_protokoll.py <seite> <protokoll.json>"); sys.exit(1)
    sys.exit(main(sys.argv[1], sys.argv[2]))
