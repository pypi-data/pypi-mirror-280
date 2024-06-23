from __future__ import annotations

import uuid

from textual.app import App, ComposeResult

from pgtui.widgets.autocomplete import AutocompleteMenu

LINES = [str(uuid.uuid4()) for _ in range(15)]


class BoardApp(App):
    def compose(self) -> ComposeResult:
        yield AutocompleteMenu(LINES)


def main():
    app = BoardApp()
    app.run()
