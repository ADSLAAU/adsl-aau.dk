How to use this repository
==========================

This repository is mostly static, so if you want to make changes, you'll have to edit the HTML.
The exceptions to this are the "regnskab" and "referat" folders, because I didn't feel like making such long lists by hand.

## Adding a new referat or regnskab

1. Put your new files in the relevant folders.
2. Run the `build_referat.py` or `build_regnskab.py` scripts and copy the output into `index.html`.

(Oneliner for Linux users: `./build_referat.py >index.html`)

## Adding a new set of vedtægter

Ideally, the document's name should have format `YYYY-MM-DD.pdf` or `YYYY-MM-DD.docx`. Forgetting to do this won't break the website, but it will break my heart.

1. Put your new files in the relevant folders.
2. Update `index.html` in two places: The raw link, and the embed.
3. Add a link under `tidligere/index.html` (Despite the name, this list should also contain the current set).

To-Do List
==========

- Collapsible lists (for easier navigation through regnskab etc)
- Less code duplication between `build_referat.py` and `build_regnskab.py`

In a wider time-frame:
- Use some kind of static templating engine
- Reduce code duplication in HTML, perhaps through the static templating engine
- Separate HTML code and documents, to make it simpler to upload stuff, perhaps through the static templating engine
- Centralise workflows (perhaps by separating HTML from documents, and generating stuff through the static templating engine)

All this should preferably be done _without_ increasing code complexity too much.
**This website ought to be easy to modify by any programmer without any on-boarding except this readme file!**
