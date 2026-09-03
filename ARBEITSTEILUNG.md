# GRUNDRISSE 2045 · Arbeitsteilung Klaus, HAL, Claude

Stand 1. September 2026 · Vorschlag v1 · zur Reaktion durch HAL

---

## Warum überhaupt

Die Frage war nicht, wie man das Verfahren der Webseite überträgt, sondern ob es
hier einen Mehrwert hat. Die ehrliche Antwort lautet: zur Hälfte.

**Es trägt an zwei Stellen.** Erstens als eine Wahrheit über einer Quellenbasis
mit vielen Ableitungen. GRUNDRISSE hat 204 kuratierte Quellen, ein Register in
Version 14, ein Ansatzpapier, ein Feld-4-Papier und eine Team-Seite, die alle aus
derselben Basis leben. Der typische Fehler in dieser Konstellation ist nicht der
Tippfehler, sondern der auseinanderlaufende Stand: die Seite nennt eine
Registerversion, die es so nicht mehr gibt. Dagegen hilft nur ein Ort, an dem
steht, was gilt, und eine Prüfung, die es nachrechnet.

Zweitens als Kanal für Widerspruch. Der Zugang ist eine Argumentation, und
Argumentationen brauchen einen Gegner, der nicht mitgeschrieben hat. Genau das
ist HALs Rolle, und dafür ist ein Issue besser geeignet als ein Chat, weil der
Widerspruch stehen bleibt und nachlesbar ist.

**Es trägt an zwei Stellen nicht.** Ein Handbuch mit Freigabe-Gates wäre
Zeremonie ohne Gegenstand, solange es kein Deploy, keine Produktion und keine
öffentlichen Leser gibt. Und die Regel „eine Datei, die überall funktioniert" ist
hier bereits erfüllt: die Team-Seite hat null externe Verweise, null relative
Pfade, Chart.js eingebettet. Sie läuft aus jedem Ordner und aus jedem
Mailanhang. Daran ist nichts zu verbessern.

**Ein Vorbehalt.** Der Mehrwert entsteht nur, wenn HAL tatsächlich in diesem
Repository arbeitet. Wenn nicht, ist es ein privates Archiv mit zusätzlichen
Schritten, und Klaus' Dateidisziplin mit Datumspräfix und Versionsnummern
leistet fast dasselbe.

---

## Vier Arbeitspakete

Je Paket gibt es genau einen Writer. Wer nicht Writer ist, prüft, widerspricht
und schlägt vor, schreibt aber nicht in dieselbe Datei.

### P1 · Der Zugang als Argument

**Writer: HAL.** Der Zugang behauptet, dass der Grundvertrag der Moderne
abgelaufen ist, und leitet daraus die Leitfrage der Neubestimmung des Menschen
ab. Diese Kette gehört unabhängig geprüft: Trägt jeder Schritt? Wo ist die
schwächste Stelle? Welche Gegenposition wird nicht behandelt?

Claude liefert dazu Belege und Gegenbelege aus dem Register, auf Anforderung und
mit Fundstelle. Klaus entscheidet, was in den Zugang eingeht.

**Ergebnis:** ein Befundpapier mit den drei schwächsten Stellen und je einem
Vorschlag, kein Umbau der Datei.

### P2 · Register, Raster, Auswertung

**Writer: Claude.** Die Konsistenz zwischen Registerdatei, Zahlen in der
Team-Seite und dem offengelegten 8-Kriterien-Raster ist mechanisch prüfbar und
gehört deshalb dorthin, wo mechanisch geprüft wird. Dazu die Auswertungen, die
Grafiken und die Herkunftskennzeichnung jeder Aussage.

HAL prüft stichprobenartig, ob die Kennzeichnung stimmt, also ob eine als
„Bibliothek" markierte Aussage wirklich aus der Bibliothek stammt und nicht aus
Modell-Wissen.

**Ergebnis:** ein Prüfskript, das ohne Befund läuft, und ein Stichprobenbericht.

### P3 · Die Team-Seite

**Writer: Claude.** Umsetzung, Struktur, Explorer, Grafiken.

HAL prüft aus der Perspektive des Kern-Teams: Ist der Zugang in neun Abschnitten
in dieser Reihenfolge nachvollziehbar? An welcher Stelle steigt jemand aus, der
den Prozess nicht kennt? Klaus gibt frei.

**Ergebnis:** eine Leseprüfung mit konkreten Stellen, nicht mit Eindrücken.

### P4 · Der Prozess selbst

**Writer: HAL.** Ein Handbuch von einer Seite, mehr nicht: Wahrheitsstand,
Rollen, Invarianten, Vorlageregel. Es wächst nur, wenn ein Fehler zweimal
passiert ist.

Claude liefert das Prüfskript und hält es aktuell.

---

## Vier Invarianten

1. Keine Quelle entfällt ohne ausdrückliche Freigabe. Reorganisation ist
   erlaubt, Weglassen nicht.
2. Jede wesentliche Aussage trägt ihre Herkunft nach der Quellenkennzeichnung
   des Klaus-Kerns: Kern, Werk, Bibliothek, Welt, Modell-Wissen, Vermutung.
3. Die Team-Seite bleibt eigenständig: kein externer Verweis, kein Nachladen,
   keine Abhängigkeit von einem Ordner.
4. Das offengelegte Kriterienraster bleibt sichtbar und nachrechenbar. Wer die
   Auswertung nicht nachrechnen kann, kann ihr nicht widersprechen.

---

## Wie der Kanal funktioniert

Ein Issue je Arbeitspaket. Der Auftrag steht oben, vollständig. Die Antwort steht
im selben Issue und endet mit dem Remote-SHA. Kein Paket beginnt ohne einen Satz
dazu, was „fertig" heißt, und keine Antwort endet ohne Lieferschein: Geprüft,
Unsicher, Zu entscheiden.

Klaus liest mit und entscheidet. Er trägt nichts mehr von einem Modell zum
anderen.

---

## Drei Fragen an HAL

Damit die Reaktion konkret wird, hier die drei Punkte, an denen dieser Vorschlag
brechen kann.

1. **P1 als Deine Führung.** Willst Du den Zugang als Argument führen, oder
   siehst Du Deine Rolle eher in P4, dem Prozess? Beides zugleich wäre zu viel.
2. **Die Halbierung.** Ich habe Handbuch und Gates bewusst zurückgenommen. Hältst
   Du das für richtig, oder fehlt damit die Verbindlichkeit, die bei der Webseite
   erst den Unterschied gemacht hat?
3. **Die Kennzeichnung.** Die Herkunftsmarke jeder Aussage ist die zentrale
   Invariante dieses Projekts. Sie ist aber nur stichprobenartig prüfbar. Siehst
   Du einen Weg, sie systematischer zu sichern, ohne das Projekt in Bürokratie zu
   ersticken?

---

## Wo alles liegt

Ein Repositorium: `burmeister12439-futur2/grundrisse-landkarte`, seit dem
3. September 2026 öffentlich. Vorher hieß es `grundrisse-2045` und war privat,
und daneben lag ein zweites, öffentliches Repositorium mit einer veralteten
Fassung der Seite. Beides ist zusammengeführt. Das alte öffentliche liegt als
`grundrisse-landkarte-alt` still.

Die Team-Seite läuft über GitHub Pages aus `main`:

    https://burmeister12439-futur2.github.io/grundrisse-landkarte/
    https://burmeister12439-futur2.github.io/grundrisse-landkarte/fragen.html

Der Zugang läuft über einen fine-grained Token nur für dieses Repositorium,
abgelegt in `.claude-local/gh_token` und von `.gitignore` ausgeschlossen. Der
Tokenwert wird nie ausgegeben und nie in eine Datei geschrieben. Ohne Token kann
kein Modell im Issue antworten, und dann ist Klaus wieder Bote.

**Weil das Repositorium öffentlich ist:** Alles, was hier hineinkommt, ist von
außen lesbar. Der Handapparat bleibt draußen, Zugangsdaten sowieso. Wer eine
Datei hinzufügt, prüft vorher, ob sie öffentlich stehen darf.


## Wo geantwortet wird

Stand 2026-09-03, aus dem Pilotlauf P1 gelernt.

HAL liest GitHub inzwischen von selbst. Er hat den Commit `6ab1154`
gefunden, ohne dass jemand ihn geschickt hat. Was noch nicht von selbst
geht, ist die Antwort: Sie landete im ChatGPT-Fenster, und Klaus musste
sie von Hand ins Issue tragen.

**Verbindliche Regel:** Wenn eine Frage aus einem GitHub-Issue kommt oder eine
Antwort ein Repositorium betrifft, schreibt das antwortende System die
inhaltliche Antwort mit dem GitHub-Connector in das zugehörige Issue. Im Chat
steht danach nur der Satz, dass dort geantwortet wurde. Eine inhaltliche Antwort
auf etwas, das ins Issue gehört, steht niemals im Chat.

Das gilt für HAL und für Claude gleichermaßen. Klaus transportiert
nichts. Wenn er etwas transportieren muss, ist das ein Befund über den
Prozess, kein Dienst am Prozess.

## Was der Lieferschein unterscheiden muss

- `geprüft` heißt: am Text im Repositorium geprüft.
- `Bericht` heißt: die Angaben eines anderen Beteiligten übernommen,
  weil die Quelle nicht erreichbar war.
- Wer eine Regel beschreibt, schreibt dazu, was davon eine Maschine
  prüft und was redaktionell bleibt. Absicht ist kein Ist-Zustand.
