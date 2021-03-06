---
title: 'tatort-graph '
slug: tatort-graph
tags:
- tatort
- graphviz
- svg
date: "2014-03-13T10:30:00+01:00"
author: marvin
draft: false
---

![tatort-graph](/images/tatort-graph.png)

Hat ja nur zwei Wochen gedauert. Ich habe mit einem [Scraper](http://scrapy.org/) Tatort Daten abgegriffen und in ein JSON-File gegossen. Es sind die Daten von über 900 Tatort-Episoden. Nun war mir erstmal nicht so ganz klar was ich mit den Daten anfangen wollte. Also beschloss ich eine Tatort-API zu bauen und es versuchen die Daten zu visualisieren. Mit beiden habe ich gar keine Erfahrung. Ich habe mit matplotlib angeschaut und bin an den Möglichkeiten verzweifelt. Absolut üerfordert. Ich erinnerte mich an [Graphviz](http://www.graphviz.org/). Es kann aus einem einfachen Format, mit Relationen, Graphen erzeugen. Ich fing an [pygraphviz](http://pygraphviz.github.io/) zu benutzen. Am Anfang stand ich ähnlich auf dem Schlauch. Wo war der Unterschied zwischen "Nodes" und "Edges"? Edges definieren Verbindungen zwischen zwei Nodes. Sind diese nicht explizit deklariert werden sie durch die Edge-Verbindung auch als Nodes betrachtet. Ich stand vor einem Haufen an Problemen. Ich musste die richtige Graphen-Art finden. Ein Layout was nach oben skalierte. Die graphviz-Option "-Goverlap=scale" half. Diese skaliert den Output soweit wie möglich. Desweiteren setzte ich auf "sfdp". Das ist besonders für große Graphen geeignet. Bei sovielen Verbindungen waren die Graphen so riesig das sie nicht mehr zu bearbeiten waren. Gimp schmierte ab, libpng versagte und imagemagik legte sofort die Ohren an. Was funktionierte, war Inkscape. Mit inkscape kann man auch aus der Kommandozeile aus PNGs aus SVGs exportieren. Aus dem, mit pygraphviz generierten, SVG machte ich ein 150MB großes PNG. Dieses versuchte ich mit vielen Methoden in Tiles zu schneiden. Keine Chance. [gdal2tiles](http://www.gdal.org/gdal2tiles.html) brauche 6 Tage um dann kaputte Tiles zu aus zuwerfen. Viel Gefrickel brachte keine Lösung. Da das SVG relativ klein war (1,7MB), sollte es möglich sein es direkt im Browser anzusehen. Unbenutzbar bei so einem riesen Ding. Natürlich will man zoom und scrollen, mit allem und viel scharf. [svgpan](https://code.google.com/p/svgpan/) ist ein kleines Javascript welches man in das SVG einbindet und es so "browsable" macht. Die nötigen Anpassungen zu finden war wieder die Hölle. Natürlich undokumentiert. Es muss noch ein "viewport"-Tag um den SVG-Inhalt gesponnen werden. Trotzdem funktionierte es im Firefox nicht. Wofür gibt es GitHub? Mal nach Forks ausschaugehalten und fündig geworden. [SVGPan_fixed](https://github.com/iascchen/SVGPan_fixed) brachte die Erlösung. Damit funktionierte es. Alles habe ich in ein Script gegossen mit dem man die Graphviz-Sachen bauen kann und die Anpassungen an dem SVG vornimmt. Yeah. Endlich geht es mal voran.

Das Script findet ihr [hier](https://github.com/xsteadfastx/tatort-graph). Und kann jemand mal [docopt](http://docopt.org/) ein Denkmal bauen?

Anschauen kann es [hier](http://xsteadfastx.github.io/tatort-graph/sfdp.web.svg). Sieht ersmal nach Fliegendreck auf dem Monitor aus, man kann mit dem Mausrad aber reinzoomen. Viel Spaß...  