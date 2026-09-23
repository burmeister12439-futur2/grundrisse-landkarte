# Werkzeug zur Seitenprüfung

**Stand:** 23.09.2026

| Datei | Wofür |
|---|---|
| `pruefe_seite.py` | Die Prüfung, die am 22.09.2026 gefehlt hat. Verschachtelung, Sichtbarkeit ohne Klick, Leseblick, tote Sprungmarken, doppelte Kennungen. Rückgabe 0 oder 1. Nur Standardbibliothek, kein Browser. |
| `pre-push` | Der Haken, der die Prüfung vor jedem Push ausführt und ihn bei Befunden anhält. Installiert nach `.git/hooks/pre-push`. |

## Warum es das gibt

Am 22.09.2026 stand bei der Umschaltung auf die Gliederung A bis I ein
schließendes `</details>` an der falschen Stelle. Die Fragen zu Abschnitt D
lagen dadurch in einem zugeklappten Werkstatt-Fenster und waren für jeden
Leser unsichtbar. Der Fehler stand einen ganzen Tag lang live und ist von
keiner unserer Prüfungen gefunden worden, sondern von Beate Schulz-Montag am
23.09.2026 beim Lesen.

Der Grund, warum keine Prüfung ihn fand: Alle haben gezählt. Die Zahl der
`<details>` und `</details>` stimmte in jedem Commit, fünf zu fünf. Die Zahl
der Formularfelder stimmte, sechzehn. Falsch war nicht die Zahl, sondern die
Position, und Position prüft kein Zähler. Die Zählung hat den Fehler nicht
übersehen, sie hat ihn zugedeckt.

## Aufruf

```
cd ~/Documents/GitHub/grundrisse-2045
python3 _werkzeug/pruefe_seite.py index.html
```

## Gegenprobe

Das Werkzeug ist gegen den fehlerhaften Stand geprüft worden, Commit
`750b7eb` vom 23.09.2026, 08:59 Uhr. Es meldet dort alle fünf
Verschachtelungsfehler, nennt die drei unsichtbaren Elemente samt Fenster und
zeigt im Leseblick für Abschnitt D „kein Fragenblock, 0 Felder". Genau das,
was Beate gesehen hat. Gegen den heutigen Stand meldet es BESTANDEN.

Eine Prüfung, die nur am reparierten Stand grün zeigt, beweist nichts. Erst
die Gegenprobe am kaputten Stand zeigt, dass sie greift.
