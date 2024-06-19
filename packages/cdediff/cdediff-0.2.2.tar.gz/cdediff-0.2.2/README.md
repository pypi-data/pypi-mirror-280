# Übersicht

`cdediff` ist ein Komandozeilenwerkzeug um partielle Exporte von CdEDB-Veranstaltungen in eine menschenlesbare Form zu bringen, sowie um übersichtliche Änderungszusammenfassungen zwischen den Zuständen zu verschiedenen Zeitpunkten zu generieren.

Der primär angedachte Anwendungsfall ist die Verwendung als `difftool` mit `git`.

## Installation und Voraussetzungen

Die minimal erforderliche Python-Version ist `3.10`. `cdediff` kann via pip installiert und aktualisiert werden.

    pip install cdediff

    pip install --upgrade cdediff

Nach einer Aktualisierung sollte ggf. die Anbindung an EventKeeper neu etabliert werden, siehe "Anbindung an EventKeeper".

## Verwendung

Im Ordner `tests` stehen zwei beispielhafte partielle Exporte zu Testzwecken zur Verfügung.

Die beiden Exporte (des gleichen Events) können wie folgt verglichen werden:

    # if venv is not active:
    . venv/bin/activate

    python3 -m cdediff difftool tests/a.json tests/b.json --mode reg
    # or
    python3 -m cdediff difftool tests/a.json tests/b.json --mode event
    # or
    python3 -m cdediff difftool tests/a.json tests/b.json --mode all

## Anbindung an EventKeeper

CdEdiff kann in einem EventKeeper repository installiert und für die Anzeige von git diffs verwendet werden:

    # if venv is not active:
    . venv/bin/activate

    # Bei installation via pip:
    python3 -m cdediff <path_to_event_keeper> --mode reg
    # or
    python3 -m cdediff <path_to_event_keeper> --mode event
    # or
    python3 -m cdediff <path_to_event_keeper> --mode all

    cd <path_to_event_keeper>
    git diff <some revision>

Um eine andere Ansicht einzurichten, kann das Setup-Skript einfach erneut mit anderen Argumenten ausgeführt werden. Um die Verwendung im Repository zu deaktivieren kann das `--remove` Argument verwendet werden:

    # if venv is not active:
    . venv/bin/activate

    python3 -m cdediff <path_to_event_keeper> --remove

# Entwicklung

Um an `cdediff` zu arbeiten, solltest du das Repository klonen, ein virtual environment einrichten und dieses Paket inklusive der development dependencies installieren:

    # Clone repository
    git clone ssh://gitea@tracker.cde-ev.de:20009/orgas/cdediff.git
    cd cdediff

    # Setup venv
    python3 -m venv venv
    . venv/bin/activate

    # Install package with dev dependencies.
    pip install -e .[dev]
