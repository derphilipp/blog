Title: Beets und so 
Slug: beets-und-so
Date: 2014-03-11 11:05
Tags: beets, music


Musikverwaltung kann wirklich der Haß sein. Am Anfang waren es nur ein paar lose Ordner die man wiederrum lose in Ordner mit Artist-Namen steckte. Nichts besonderes. Mit einem Player wie [xmms](https://en.wikipedia.org/wiki/XMMS) (einen WinAmp-Klon für Linux) machte das auch keine großen Probleme. Man klickte durch die Ordner und wählte die Files aus die man hören wollte. Doch man wollte irgendwie mehr: Datenbanken mit allerlei Metadaten. Ich probierte [Amarok](https://en.wikipedia.org/wiki/Amarok_%28software%29) aus. Ein riesen Biest welches den Wunsch nach Musik im Keim erstickte. Es war so träge und häßlich wie die Nacht. Nach einem Anfall nach Minimalismus, benutze ich jahrelang [CMUS](https://en.wikipedia.org/wiki/Cmus). Ich war zufrieden. Dann kam mein erster iPOD und meinen Ausflug in die MacOSX-Welt. iTunes... was muss man dazu sagen. Ein dreckiges Stück Software zum abgewöhnen. Und es hatte nur ein Feature welches ich wirklich gut fand: Es verwaltete deine Musik. Änderte man einen Tag, veränderte er auch die Dateinamen und popelte das in die richtigen Verzeichnis. Ein Traum. Dann mein Wechsel zurück zu Linux auf dem Desktop. Ich fand keinen Ersatz für dieses Feature. Doch etwas viel Schöneres wurde mir offenbart: [MPD](http://www.musicpd.org/)! Ein Daemon den man schön laufen hat und mit Clients seiner Wahl bedienen kann. Ganz großes Kino. Als Client setze ich bis heute [ncmpcpp](http://ncmpcpp.rybczak.net/) ein. Ein Traum. Mit der verwaltung war es aber noch immer so ein Problem. Ich lernte [Musicbrainz](http://musicbrainz.org/) zu lieben. Das benutzte ich nicht nur jeden Tag, ich fütterte es auch mit vielen neuen Daten aus meiner Hardcore/Punk Sammlung. Musicbrainz ist sowas wie die Wikipedia der Musik-Metadaten, inklusive Cover Archiv. Ich benutzte [Picard](http://musicbrainz.org/doc/MusicBrainz_Picard) um Teile meiner Sammlung zu verifizieren und richtig zu taggen. Picard erkennt sogar per akustischen Fingerprint ungetaggte Files und packt alles schön in sein vordefiniertes Verzeichnis. Eigentlich war ich ganz zufrieden. Nun las ich von [Beets](http://beets.radbox.org/). Ein Musikverwaltungstool in Python. Was mich daran reizte: Man kann seine komplette Sammlung durch jagen und versucht alles richtig zu taggen und zu benennen. Mit den richtigen Plugins sucht er sogar noch das Cover und Genre raus. Gibt es mal etwas nicht bei Musicbrainz, kann per Plugin auch auf Discogs zugegriffen werden. Damit wäre fast alles abgedeckt. Ich habe mal eine Kopie meiner Sammlung gemacht und ein `beet import Musik.bkp` gestartet. Weil noch nicht alles durch Musicbrainz verifiziert war, musste ich noch viele Fragen beantworten. Bei einem bestimmten Prozenzsatz an Abweichungen bedarf es Userinteraktion. Ich bin soweit zufrieden das ich schon komplett umgestiegen bin. Es gibt doch noch ein paar Punkte, die ich klären will:

- Leere Verzeichnise bleiben übrig
- Ändert man Tags werden die Verzeichnise nicht angepasst
- Zieht er sich die Genres von last.fm, wieso schreibt er sie dann manchmal in die Files und manchmal nich