---
title: 'MusicCodes '
slug: musiccodes
tags:
- flask
- sqlite
- latex
date: "2014-04-01T15:34:00+02:00"
author: marvin
draft: false
---

![musiccodes](/images/musiccodes.jpg)

Ich war mal davor eine kleine Plattenfirma zu gründen. Eine Plattenfirma die nur Vinyl heraus bringt. Man könnte mich sogar als Record-Collector bezeichnen. Es gab eine Zeit in der ich im Laden doch eher zur CD gegriffen habe. Grund war die digitalisierung der Stücke um sie überall hören zu können. Dies änderte sich dramatisch nachdem vielen neuen Platten ein kleiner Zettel mit einem Downloadcode beilagen. Meist wird sowas von Drittfirmen angeboten. Es war einfach mal an der Zeit zu schauen wie man das gleiche mit ein paar Zeilen Code selber bauen könnte. Zutaten: flask-Zeugs, sqlite und LaTeX. Entstanden ist [MusicCodes](https://github.com/xsteadfastx/MusicCodes). Man kann eine Datenbank anlegen in der die erzeugten Codes liegen und ein Feld in dem festgehalten wird wie oft das File schon runtergeladen wurde. Es gibt eine Option um neue Codes zu erzeugen und der Datenbank hinzuzuügen. Man hat auch die Möglichkeit den Download-Counter zurück zusetzen. Für Testzwecke kann man per `run` die Webapp starten. Natürlich geht das ganze auch per [gunicorn](http://gunicorn.org/). Nun kommen wir zu den ausdruckbaren Gutscheincodes. Ich habe noch nie etwas mit LaTeX gemacht bzw. machen müssen. Die Anzahl der Dokumente die ich so anlege, hält sich in Grenzen. Aber für diesen Zweck wäre es perfekt. Es ist sogar möglich per [Jinja2](http://jinja.pocoo.org/) Templates für LaTeX anzulegen und zu benutzen. Dies macht alles schön einfach und man kann per for-loop in dem Template rum machen. Man muss nur die Start-, und Endstrings anpassen damit LaTeX kompatibler Code erzeugt wird. Die Coupons sollten nicht größer als A8 sein damit ich besonders viele auf ein A4-Papier drucken kann. Das war dann die nächste Hürde. Aber dank [includepdf](http://www.namsu.de/Extra/pakete/Pdfpages.html) kann man mehrere PDFs auf ein größeres platzieren. Was mich an LaTeX so abschreckt ist die unüberschaubarkeit von Erweiterungen und Distributionen. Vor allem der Stand der Distributionen in den Linux Distributionen. Irgendwie scheint immer was zu fehlen. Der Befehl `tlmgr` failed immer. Ich konnte ihn noch nicht zum laufen bekommen. Wenn ich Zugriff zu richten Internetz habe, werde ich mir mal eine ganze LaTeX-Distribution anschauen.  


Alles zusammen knuppern und [fertich](https://github.com/xsteadfastx/MusicCodes)...    