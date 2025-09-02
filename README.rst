Lizenzen
========

.. code-block:: bash

    $ git clone git@github.com:hbz/lizenzen.git
    $ cd lizenzen
    $ python3 -m venv _venv
    $ . _venv/bin/activate
    $ pip install -r requirements.txt
    $ make dirhtml
    $ python3 -m http.server --directory _build/dirhtml/
    $ rsync -avn -e ssh _build/dirhtml/ ojs:/srv/www/lizenzen.hbz-nrw.de/lizenzen/