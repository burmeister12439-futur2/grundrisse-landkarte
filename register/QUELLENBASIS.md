# Quellenbasis GRUNDRISSE

Stand: 2026-09-03

## Wo die Quellen liegen

Der Handapparat liegt auf Klaus' Rechner, nicht im Repositorium:

| Etikett im Register | Ordner auf dem Rechner |
|---|---|
| `Material/...` | `lab-aktuell/Material/Themen/...` |
| Werkstatt-Notizen | `lab-aktuell/Publikationen/Werkstatt-Notizen` |

Rund 6,7 GB. Das kommt nicht ins Repositorium und soll auch nicht.

## Was das Register jetzt leistet

`2026-09-03_..._v15.xlsx` hat zwei neue Spalten gegenüber v14:

- **Datei (Material/Themen)**: der Pfad relativ zu `Material/Themen`.
- **Zuordnung**: wie sicher die Zuordnung ist.

| Zuordnung | Zeilen | Bedeutung |
|---|---|---|
| geprüft | 13 | von Hand kontrolliert |
| sicher | 80 | automatisch, hohe Übereinstimmung |
| wahrscheinlich | 43 | automatisch, mittlere Übereinstimmung, ungeprüft |
| offen | 0 | keine |

Zusammen 136 Zeilen mit Herkunft `Bibliothek`. Die übrigen 68 Zeilen
stammen aus Welt-Kanon, Signalen, Kumli-Stream und eigenen Arbeiten und
zeigen nicht auf den Handapparat.

v14 bleibt unverändert liegen. v15 ergänzt, es ersetzt nichts.

## Keine offenen Fälle

Zwei Zeilen waren zunächst offen. Beide ließen sich über die Spalte
`Herausgeber / Institution` auflösen, die der automatische Abgleich nicht
ausgewertet hatte.

| Nr | Herausgeber im Register | Datei |
|---|---|---|
| 4 | K. Steinmüller, Z. f. Zukunftsforschung, 2012 | `ZF/2024/Steinmüller-ZF.pdf` |
| 133 | Zukunftsinstitut (Horx), 2021 | `ZF/2021/Zukunftsinstitut-2021.pdf` |

Nr. 4 wird zusätzlich durch `foresight_D/foresight Master/2026-08-18_Grundrisse-der-Zukunft_v1.html`
gestützt, dort steht: Startfassung nach Steinmüller, Zukunftsforschung in Deutschland.

Lehre daraus: Ein Titelabgleich allein reicht nicht. Herausgeber und Jahr
gehören in jeden Abgleich.

## Regel ab jetzt

Eine neue Registerzeile bekommt entweder einen Link oder einen Dateipfad.
Ohne beides heißt der Verifikationsstand `bibliografisch`, nicht `verifiziert`.

## Was HAL prüfen kann und was nicht

HAL sieht nur das Repositorium. Er kann das Register prüfen, die
Dokumente unter `dokumente/` und alles Weitere, was hier liegt. Er kann
den Handapparat nicht öffnen.

Braucht er eine Quelle, nennt er die Registernummer. Die Spalte `Datei`
sagt dann genau, welche Datei gemeint ist. Sie wird als Textauszug in
`quellen/` abgelegt, einzeln und nur bei Bedarf.

Prüft jemand eine Aussage gegen eine Quelle, die nicht im Repositorium
liegt, ist das Ergebnis ein Bericht und keine Prüfung. Das gehört so in
den Lieferschein.
