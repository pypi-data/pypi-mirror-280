# Übersicht

`cdediff` ist ein Komandozeilenwerkzeug um partielle Exporte von CdEDB-Veranstaltungen in eine menschenlesbare Form zu bringen,
sowie um übersichtliche Änderungszusammenfassungen zwischen den Zuständen zu verschiedenen Zeitpunkten zu generieren.

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

    # same as `--mode reg`
    python3 -m cdediff difftool tests/a.json tests/b.json
    # or
    python3 -m cdediff difftool tests/a.json tests/b.json --mode reg
    # or
    python3 -m cdediff difftool tests/a.json tests/b.json --mode event
    # or
    python3 -m cdediff difftool tests/a.json tests/b.json --mode all

Es gibt drei verschiedene Ansichten:

- `reg`:
  - Zeige Unterschiede mit Fokus auf Anmeldungen. Wurde z.B. ein voller Kurs abgesagt, wird bei jedem der ehemaligen
    Kursteilnehmenden (und der Kursleitenden) die Änderung des zugeteilten Kurses angezeigt.
- `event`:
  - Zeige Unterschiede an der Veranstaltung selbst, sowie mit Fokus auf Unterkünfte und Kurse. Wurde z.B. ein voller
    Kurs abgesagt, wird für jeden Kurs (inklusive des abgesagten) eine Liste aller dazugekommenen, bzw. verlorenen
    Teilnehmenden angezeigt.
- `all`:
  - Zeig alle anderen Ansichten nacheinander an, getrennt von einer optischen Trennlinie.

## Anbindung an EventKeeper

CdEdiff kann in einem EventKeeper repository installiert und für die Anzeige von git diffs verwendet werden.
Bei der Initialisierung kann eine Ansicht angegeben werden. Dieser wird dann für `git diff` verwendet. Der Standard ist `--mode reg`

    # if venv is not active:
    . venv/bin/activate

    # same as `--mode reg`.
    python3 -m cdediff setup <path_to_event_keeper>
    # or
    python3 -m cdediff setup <path_to_event_keeper> --mode reg
    # or
    python3 -m cdediff setup <path_to_event_keeper> --mode event
    # or
    python3 -m cdediff setup <path_to_event_keeper> --mode all

    cd <path_to_event_keeper>

    git diff <some revision>
    # or
    git cdediff <some revision>

Um eine andere Ansicht zu verwenden können die folgenden git Aliase verwendet werden:

    git reg-diff
    git event-diff
    git all-diff

Um Änderungen zwischen zwei Zeitpunkten leichter anzeigen zu können, steht außerdem eine Hilfsfunktion zur Verfügung. Hier
können Zeitangaben wie `2 hours ago` gemacht werden. Mit `-v`, `-vv` und `-vvv` können zusätzliche Informationen, wie
die Anzahl der Commits oder die gesamte git history angezeigt werden.

    git cdediff-since "2 days ago"
    git cdediff-since "5 hours ago" "12:40"
    git reg-diff-since "2024-05-01" "2024-06-01" -v
    git event-diff-since "Jan 01 2024" -vv

Um eine andere Ansicht als Standard für `git diff` einzurichten, kann das Setup-Skript einfach erneut mit anderen Argumenten
ausgeführt werden. Um die Verwendung im Repository zu deaktivieren kann das `--remove` Argument verwendet werden:

    # if venv is not active:
    . venv/bin/activate

    python3 -m cdediff setup <path_to_event_keeper> --remove

### Einrichtung als reines Difftool

Falls gewünscht, kann `cdediff` auch als reines `difftool` eingerichtet werden. So behält `git diff` die reguläre Funktionsweise:

    # if venv is not active:
    . venv/bin/activate

    python3 -m cdediff setup <path_to_event_keeper> --no-diff

    cd <path_to_event_keeper>
    git diff  # Unverändert.

Stattdessen können die üblichen menschenlesbaren Ansichten wie folgt angezeigt werden:

    git cdediff  # Verwendet den bei Einrichtung angegebenen Modus. Default: reg.
    git reg-diff
    git event-diff
    git all-diff

### Implementationsdetails der Einrichtung

Bei der Aktivierung und/oder Deaktivierung von `cdediff` in einem Git repo wird eine eventuell vorhandene
`.gitattributes`-Datei gelöscht und/oder überschrieben.

Außerdem werden folgende Keys in der lokalen git Konfiguration gesetzt bzw. gelöscht. Die ursprünglichen Werte werden bei
Deaktivierung **nicht** wiederhergestellt:

- `diff.tool`
- `difftool.prompt`
- `difftool.cdediff.command`
- `difftool.reg.cmd`
- `difftool.event.cmd`
- `difftool.all.cmd`
- `alias.cdediff`
- `alias.reg-diff`
- `alias.event-diff`
- `alias.all-diff`
- `alias.cdediff-since`
- `alias.reg-diff-since`
- `alias.event-diff-since`
- `alias.all-diff-since`

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


## Neue Version

Um eine neue Version zu bauen:

    # Potentially deactivate venv.
    deactivate

    python3 -m build

Um die neue Version (bzw. alle neuen) auf PyPI zu veröffentlichen:

    # Potentially deactivate venv.
    deactivate

    # Alle Versionen
    python3 -m twine upload dist/*
    # Gezielt
    python3 -m twine upload dist/<X.Y.Z>*
