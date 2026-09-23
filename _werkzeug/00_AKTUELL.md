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
zwei Fingerabdrücken: dem SHA-256 der geprüften Seite und dem SHA-256 von
`pruefe_browser.js` selbst. Der Haken lässt nur durch, was zu beidem passt.
Jede Änderung an `index.html` macht das Protokoll ungültig, und jede Änderung
am Prüfer ebenso. Ohne den zweiten Fingerabdruck bliebe ein altes grünes
Protokoll zu einer unveränderten Seite gültig, während sich der Prüfer
darunter geändert hat. Das ist die ehrliche Lösung: kein stilles Überspringen.

### Die mobile Ausnahme

Ein Element darf breiter sein als der Schirm, wenn es in einem Kasten steckt,
den man seitlich schieben kann. Das ist bei der Quellentabelle Absicht.
Zulässig sind deshalb nur `overflow-x: auto` und `overflow-x: scroll`.
`overflow-x: hidden` gilt nicht als Ausnahme, von Klaus am 23.09.2026 gesetzt:
Es schneidet den Inhalt ab, ohne eine bedienbare Scrollmöglichkeit zu geben.
Was dort hinausragt, ist für den Leser schlicht weg.

Diese Verschärfung hat sofort einen Befund an der geltenden Seite gefunden.
Das Szenariokreuz in Abschnitt C stand in einem Kasten mit `overflow:hidden`
und war bei 390 Pixeln 409 Pixel breit. Die rechten 19 Pixel waren auf dem
Telefon abgeschnitten und nicht erreichbar. Der Kasten ist jetzt
`overflow-x:auto`, die abgerundeten Ecken bleiben, das Kreuz lässt sich
schieben.

## Die Gegenproben

Eine Prüfung, die nur am heilen Stand grün zeigt, beweist nichts.

```
python3 _werkzeug/gegenproben.py
```

Fünf absichtlich beschädigte Kopien für die statische Prüfung, jede muss rot
werden: kaputte Verschachtelung, zwei entfernte Felder, Feld ohne
`data-frage`, Feld ohne Label, per inline-CSS verstecktes Feld.

Drei weitere Kopien werden für die Browserprüfung erzeugt, weil die statische
Prüfung kein Stylesheet liest und keine Fensterbreite kennt: das per
CSS-Klasse versteckte Feld muss rot werden, eine 900 Pixel breite Tabelle in
einem Kasten mit `overflow-x:auto` muss grün bleiben, und dieselbe Tabelle in
einem Kasten mit `overflow-x:hidden` muss rot werden.

## Übertragung auf andere Projekte

Noch nicht geschehen und bewusst so. Erst wenn diese Gegenproben rot und der
geltende Stand grün sind, wird daraus ein übertragbares Werkzeug. Jede andere
Seite braucht dann einen eigenen `sollbestand.json`, weil ein Sollbestand
genau die eine Seite beschreibt, für die er gilt.
