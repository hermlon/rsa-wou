# rsa-wou
## RSA Implementation im WOU Mathematik
### Features
* Finden von der nächsten Primzahl nach einer generierten Zufallszahl
* Generieren von public- und privatekey (Berechnen des modularen Inverse mit erweitertem Euklidischen Algorithmus)
* Ver- und Entschlüsseln von Nachrichten

Beispiel:

`Zufällige Primzahlen p: 311, q: 557`

`Privater Schlüssel: d: 49993, n: 173227`

`Öffentlicher Schlüssel: e: 65537, n: 173227`

`Verschlüsselte Nachricht: [39992, 71924, 56832, 169753, 134465, 59657, 169753, 16682, 24245, 56832, 123241, 130797, 154615, 150230, 71924, 130797, 154615, 24245, 134465, 68570, 71924, 24245, 134465, 39992, 71924, 56832, 154615, 20521, 150230, 56832, 134465, 27280, 56832, 140750, 134465, 16682, 130797, 154615, 150810, 169753, 19786, 169753, 56832, 140750, 169753, 56832, 134465, 133752, 27280, 16682, 71924, 56832, 169753, 16682, 16682, 68570, 123241, 56832, 154977, 134465, 143423, 134465, 35077]`

`Entschlüsselte Nachricht: Eine Testnachricht mit Einhorn und schwebenden Businessman! 🦄 🕴`
