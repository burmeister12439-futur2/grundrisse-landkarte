# Werkzeug zur Seitenprüfung

**Stand:** 23.09.2026

| Datei | Wofür |
|---|---|
| `pruefe_seite.py` | Die statische Prüfung. Verschachtelung, Sichtbarkeit ohne Klick, Verdrahtung, Vollständigkeit gegen den Sollbestand, Leseblick, tote Sprungmarken, doppelte Kennungen. Kein Browser nötig. |
| `sollbestand.json` | Wie viele Antwortfelder und Fragenblöcke je Abschnitt stehen müssen, und welche Bedienfelder es geben darf. Jede Seite braucht einen eigenen. |
| `pruefe_browser.js` | Die Browserprüfung. Konsolenfehler, berechnete Sichtbarkeit, Diagramme, Quellen-Explorer, Sammelleiste, mobile Breite. Braucht Playwright. |
| `browserpruefung.json` | Das Protokoll der letzten Browserprüfung, mit dem SHA-256 der geprüften Seite. |
| `pruefe_protokoll.py` | Hält das Protokoll an die Seite. Passt der SHA nicht, ist die Prüfung ungültig. |
| `gegenproben.py` | Beschädigt die Seite absichtlich und weist nach, dass die Prüfung anschlägt. |
| `pre-push` | Der Haken. Erst die statische Prüfung, dann das Protokoll. Beides muss durch. |

## Warum es das gibt

Am 22.09.2026 stand bei der Umschaltung auf die Gliederung A bis I ein
schließendes `</details>` an der falschen Stelle. Die Fragen zu Abschnitt D
lagen dadurch in einem zugeklappten Werkstatt-Fenster und waren für jeden
Leser unsichtbar. Der Fehler stand einen Tag live und ist von keiner unserer
Prüfungen gefunden worden, sondern von Beate Schulz-Montag beim Lesen.

Der Grund: Alle Prüfungen haben gezählt. Fünf `<details>` zu fünf
`</details>`, sechzehn Felder. Die Zahlen stimmten, die Position war falsch.

**Der Grundsatz seither: Eine Zählung ist keine Prüfung.** Jede Zahl wird gegen
einen hinterlegten Sollbestand gehalten, nicht gegen sich selbst.

## Wie geprüft wird

Zwei Schichten, weil keine allein reicht.

**Statisch**, ohne Browser, läuft überall:

```
cd ~/Documents/GitHub/grundrisse-2045
python3 _werkzeug/pruefe_seite.py index.html
```

**Im Browser**, braucht Playwright und läuft deshalb dort, wo Playwright liegt,
nicht auf dem Rechner:

```
node _werkzeug/pruefe_browser.js index.html _werkzeug/browserpruefung.json
```

Die Browserprüfung kann damit nicht auf demselben Rechner erzwungen werden.
Damit sie trotzdem nicht still ausfallen kann, schreibt sie ein Protokoll mit
dem SHA-256 der geprüften Seite. Der Haken lässt nur durch, was ein Protokoll
zu genau diesem Stand hat. Jede Änderung an `index.html` macht das Protokoll
ungültig, und der Push wird angehalten, bis die Browserprüfung neu gelaufen
ist. Das ist die ehrliche Lösung: kein stilles Überspringen.

## Die Gegenproben

Eine Prüfung, die nur am heilen Stand grün zeigt, beweist nichts.

```
python3 _werkzeug/gegenproben.py
```

Fünf absichtlich beschädigte Kopien, jede muss rot werden: kaputte
Verschachtelung, zwei entfernte Felder, Feld ohne `data-frage`, Feld ohne
Label, per inline-CSS verstecktes Feld. Ein sechster Fall, das per CSS-Klasse
versteckte Feld, wird erzeugt und der Browserprüfung übergeben, weil ihn die
statische Prüfung nicht sehen kann.

## Übertragung auf andere Projekte

Noch nicht geschehen und bewusst so. Erst wenn diese Gegenproben rot und der
geltende Stand grün sind, wird daraus ein übertragbares Werkzeug. Jede andere
Seite braucht dann einen eigenen `sollbestand.json`, weil ein Sollbestand
genau die eine Seite beschreibt, für die er gilt.
