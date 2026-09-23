# Prüfung dieses Projekts

**Stand:** 23.09.2026

Die Prüfwerkzeuge liegen seit dem 23.09.2026 nicht mehr hier, sondern im
gemeinsamen Prüfkern `webpruefer`. In diesem Ordner bleibt nur, was zu diesem
Projekt gehört.

| Datei | Wofür |
|---|---|
| `../_pruefprofil.json` | Was an dieser Seite geprüft wird und mit welcher Fassung des Kerns. |
| `../pruefen.sh` | Der Anker. Findet den Kern, prüft seine Fassung, führt die Prüfungen aus. |
| `../einrichten.sh` | Richtet die Prüfung auf einem neuen Rechner ein: Kern holen, Abhängigkeiten, Haken, erste Prüfung. |
| `browserpruefung.json` | Das Protokoll der letzten Browserprüfung, mit dem SHA-256 von Seite und Prüfer. |
| `Archiv/` | Die bisherigen lokalen Prüferdateien. Abgelöst, nicht gelöscht. |

## Aufruf

```
cd ~/Documents/GitHub/grundrisse-2045
./pruefen.sh
```

Auf einem neuen Rechner einmalig `./einrichten.sh`. Ist der Kern als Submodul
eingebunden, genügt dort `git submodule update --init`.

Der Kern liegt seit dem 23.09.2026 als Submodul `_pruefer` im Projekt, in der
Fassung, die das Profil verlangt. Auf einem neuen Rechner genügt

```
git submodule update --init
```

Gefunden wird er über `WEBPRUEFER`, `./_pruefer` oder den Nachbarordner
`../webpruefer`, in dieser Reihenfolge. Kein fest verdrahteter persönlicher
Pfad. Fehlt er oder trägt er eine andere Fassung als das Profil erwartet,
bricht `pruefen.sh` laut ab, mit Rückgabe 2 und der Abhilfe im Klartext.

Die Browserprüfung braucht Playwright und läuft dort, wo Playwright liegt:

```
node <kern>/pruefkern/pruefe_browser.js index.html _werkzeug/browserpruefung.json
```

## Die Ablösung, nachgewiesen

Am 23.09.2026 sind alter und neuer Prüfer nebeneinander gelaufen. Die
statische Prüfung lieferte am geltenden Stand Zeile für Zeile dieselbe
Ausgabe, 36 Zeilen, ohne einen Unterschied. Die Browserprüfung ist im Kern
bytegleich, SHA-256 `99335550…`. Alle Gegenproben schlagen auch mit dem Kern
fehl. Erst danach sind die bisherigen Dateien ins `Archiv` gezogen. An
`index.html` wurde dabei nichts geändert.

Dabei ist ein echter Fehler im Nachweis selbst aufgefallen: Die Gegenproben
meldeten zunächst Rückgabe 1 ohne einen einzigen Befund, weil die beschädigten
Kopien nicht im Profil standen und der Prüfer deshalb abbrach, statt zu
prüfen. Eine rote Ampel aus dem falschen Grund ist kein Nachweis. Der Kern
verlangt jetzt Rückgabe 1 **und** mindestens einen Befund.

## Warum der Haken nicht die Absicherung ist

Der `pre-push`-Haken ruft nur `pruefen.sh` auf. Er wird nicht mit dem
Repositorium übertragen und ist damit eine Bequemlichkeit, keine dauerhafte
Absicherung. Die dauerhafte Absicherung ist der Aufruf von `pruefen.sh` dort,
wo die Veröffentlichung entsteht.
