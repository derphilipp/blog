---
title: Python, urllib und CERTIFICATE_VERIFY_FAILED
slug: python-urllib-und-certificate-verify-failed
tags:
- python
- ssl
- alpinelinux
date: "2016-03-17T13:46:00+01:00"
author: marvin
draft: false
---
Da denkt man sich einfach "mal kurz mein [Blogging](https://github.com/xsteadfastx/blog.git)-Container neu bauen" und schon funktioniert nichts mehr. Es fing schon damit an das mein [Ansible Playbook](https://github.com/xsteadfastx/batcave.git) Probleme hatte Files herrunterzuladen. `urllib` brach immer mit `urlopen error [SSL: CERTIFICATE_VERIFY_FAILED]` ab. Wie aus dem nichts. Vor ein paar Wochen gab es keine Probleme mit der `urllib`. Es gab sogar ein [StackOverflow Posting](https://stackoverflow.com/questions/35762510/alpine-3-3-python-2-7-11-urllib2-causing-ssl-certificate-verify-failed) welches mir riet einfach mal die `ca-certificates` zu installieren. Das Paket war aber schon installiert. Nach viel googeln un verzweifeln bin ich auf eine [obskure Seite](http://qiita.com/runtakun/items/a7fae47bdac887db40f1) gestoßen von der ich kaum etwas verstand. Es gab wohl die Möglichkeit `urllib` über eine Environment-Variabel den Ort der CA-Zertifikate mitzuteilen. Dies scheint auch in der [PEP 476](https://www.python.org/dev/peps/pep-0476/#trust-database) so beschrieben. [requests](https://github.com/kennethreitz/requests/issues/2899) scheint dies per Default zu machen. Ein `export SSL_CERT_FILE=/etc/ssl/certs/ca-certificates.crt` fixed die Situation in Alpine Linux. Ich frage mich nur was sich in ein paar Wochen so verändert hat das dieses Problem auftritt.