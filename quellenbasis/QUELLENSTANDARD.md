# Quellenstandard GRUNDRISSE

Stand: 2026-09-03. Grundlage: Analyse aller 204 Zeilen des Registers in `register/`.

## Warum es diesen Standard gibt

Das Register versammelt sehr verschiedene Dinge: begutachtete Aufsätze,
Gutachten wissenschaftlicher Beiräte, Fachbücher, Beratungsstudien,
Zeitungsartikel und eigene Arbeiten. Alle haben ihren Platz. Aber sie
haben nicht dasselbe Gewicht, und bis jetzt sah man ihnen das nicht an.

Der Standard trennt deshalb zwei Fragen, die leicht durcheinandergeraten:
**Was ist die Quelle?** und **Wozu benutzen wir sie?**

## Die sechs Güteklassen

Die Spalte `Güte` im Register trägt eine dieser Klassen.

| Klasse | Was das ist | Zeilen |
|---|---|---|
| **A** | Begutachtet. Fachzeitschrift mit Peer Review, wissenschaftlicher Verlag, Working Paper einer Forschungseinrichtung. | 17 |
| **B** | Institutionell. Wissenschaftlicher Beirat, Ressortforschung, Bundes- oder EU-Behörde, internationale Organisation, außeruniversitäres Institut, Stiftung mit Forschungsauftrag. | 76 |
| **C** | Fachbuch oder benannter Fachautor. Monographie ohne förmliche Begutachtung, aber mit Autorschaft, die einsteht. | 48 |
| **D** | Kommerziell oder interessengebunden. Beratung, Unternehmen, Verband, Trendhaus, Berufsverband. | 44 |
| **E** | Journalistisch oder Zeitdokument. Zeitungsartikel, Rundfunkbeitrag, politisches Dokument. | 8 |
| **F** | Eigenes Werk. Arbeiten von Klaus Burmeister, D2030 und D2045. | 8 |
| **?** | Ungeklärt. Herausgeber im Register noch offen. | 3 |

Die Klasse sagt, **welcher Art** eine Quelle ist, nicht ob sie gut ist.
Ein SPIEGEL-Artikel von 1966 ist als Zeitzeugnis unersetzlich und als
Beleg für eine Sachaussage untauglich. Beides gleichzeitig.

## Die Regel

> **Belegfähig sind A, B und C.**
> **D und E belegen keine Aussage.** Sie stehen im Register als
> Gegenstand oder als Zeitzeugnis, und das ist gewollt.
> **F belegt nur die eigene Position**, nie eine fremde Tatsache.

Wenn auf der Seite ein Satz steht und eine Registernummer dahinter, muss
diese Nummer A, B, C oder F tragen. Der Prüfer bricht sonst ab.

Dass 44 Zeilen in Klasse D stehen, ist kein Mangel. Das Register bildet
das Feld ab, und zum Feld gehört sein kommerzieller Pol. Die Zeile zum
Megatrend-Report des Zukunftsinstituts sagt das selbst: sie ist als
`Pol A der Trend-Achse` aufgenommen, nicht als Beleg.

## Was die Analyse gefunden hat

Von den auf der Seite zitierten Registernummern war **eine falsch**:

Für den Satz „Der Club of Rome hat 1972 den endlichen Planeten benannt“
stand Nr. 20. Das ist ein SPIEGEL-Interview von 2022 über den Bericht,
also Klasse E. Der Bericht selbst steht im Register als **Nr. 164, The
Limits to Growth, Meadows u.a., 1972**, Klasse C. Die Zitation ist
korrigiert.

Genau dafür ist der Standard da. Der Fehler war nicht die Quelle, sondern
die Verwechslung von Zeugnis und Beleg.

## Grenzfälle, offen benannt

- **Stiftungen** stehen in B, tragen aber eine Agenda. Bertelsmann ist
  keine Behörde. Wer eine Stiftungsstudie als Beleg nutzt, sollte die
  Trägerschaft im Satz nennen.
- **Auftragsforschung** wie Prognos, Z_punkt oder ScMI steht in D, auch
  wenn methodisch sauber gearbeitet wird. Der Auftraggeber gehört zur
  Quelle.
- **Ressortforschung** wie UBA und BBSR steht in B. Sie ist staatlich
  gebunden, aber fachlich begutachtet.
- **Eigene Arbeiten** in F sind unser Ausgangspunkt, nicht unser Beweis.
  Die Szenarien von 2018 und 2024 belegen nicht, dass ihre Bedingungen
  nicht mehr ausreichen. Das ist unsere These über sie.

## Wie die Klassifikation entstanden ist

Regelbasiert über die Spalte `Herausgeber / Institution`, danach von Hand
durchgesehen. Sie ist ein Arbeitsstand, keine letzte Instanz. Wer eine
Einstufung für falsch hält, ändert sie und begründet es im Commit.

Drei Zeilen bleiben `?`, weil dort im Register `[prüfen]` steht. Sie
dürfen nichts belegen, solange das so ist.
