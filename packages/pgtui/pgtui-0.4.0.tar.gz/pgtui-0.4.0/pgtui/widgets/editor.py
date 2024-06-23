import logging
from asyncio import sleep
from os.path import exists
from typing import Optional

from pgcli.pgcompleter import Completion  # type: ignore
from textual import on, work
from textual.document._syntax_aware_document import SyntaxAwareDocument
from textual.widget import Widget

from pgtui.completer import QueryCompleter
from pgtui.widgets.autocomplete import AutocompleteMenu
from pgtui.widgets.text_area import SqlEditorTextArea

logger = logging.getLogger(__name__)


class SqlEditor(Widget):
    DEFAULT_CSS = """
    SqlEditor {
        layers: below above;

        SqlEditorTextArea {
            layer: below;
        }

        AutocompleteMenu {
            layer: above;
            display: none;
        }
    }
    """

    def __init__(self, completer: QueryCompleter, file_path: Optional[str]):
        super().__init__()
        self.file_path = file_path
        self.completer = completer
        self.text_area = SqlEditorTextArea(self.get_initial_text())
        self.dropdown = AutocompleteMenu()
        self.filter = ""

    def compose(self):
        yield self.text_area
        yield self.dropdown

    def get_initial_text(self) -> str:
        if self.file_path and exists(self.file_path):
            logger.info(f"Loading initial text from {self.file_path}")
            with open(self.file_path) as f:
                return f.read()
        return ""

    def get_dropdown_offset(self) -> tuple[int, int]:
        row, column = self.text_area.cursor_location
        # TODO: this depends on textarea styling
        return row + 2, column + 2

    def update(self):
        completions = self.get_completions()
        if completions:
            self.dropdown.update(completions)
        else:
            self.close()

    def open(self):
        self.text_area.is_autocomplete_open = True
        self.dropdown.styles.display = "block"

    def move_to_cursor(self):
        row, column = self.get_dropdown_offset()
        self.dropdown.styles.offset = column, row

    def is_open(self):
        return self.dropdown.styles.display == "block"

    def close(self):
        self.text_area.is_autocomplete_open = False
        self.dropdown.styles.display = "none"

    # Handle events

    @on(SqlEditorTextArea.Open)
    def on_open(self, _):
        self.update()
        self.move_to_cursor()
        self.open()

    @on(SqlEditorTextArea.Close)
    def on_close(self, _):
        self.close()

    @on(SqlEditorTextArea.Update)
    def on_update(self, _):
        self.move_to_cursor()
        self.update()

    @on(SqlEditorTextArea.Up)
    def on_up(self, _):
        self.dropdown.move_up()

    @on(SqlEditorTextArea.Down)
    def on_down(self, _):
        self.dropdown.move_down()

    @on(SqlEditorTextArea.PageUp)
    def on_page_up(self, _):
        self.dropdown.page_up()

    @on(SqlEditorTextArea.PageDown)
    def on_page_down(self, _):
        self.dropdown.page_down()

    @on(SqlEditorTextArea.Select)
    def on_select(self, _):
        if completion := self.dropdown.selected_completion:
            self.text_area.apply_completion(completion)

        self.close()

    @on(SqlEditorTextArea.Changed)
    def on_changed(self, event: SqlEditorTextArea.Changed):
        self.save_changes(event.text_area.text)

    @work(group="save", exclusive=True)
    async def save_changes(self, text: str):
        if not self.file_path:
            return

        await sleep(0.5)  # debounce

        # TODO: check for changes from other sources?
        logger.info("Saving changes...")
        with open(self.file_path, "w") as f:
            f.write(text)

    def get_completions(self) -> list[Completion]:
        """Returns the completions at current cursor position"""
        text = self.text_area.text
        document = self.text_area.document
        assert isinstance(document, SyntaxAwareDocument)
        index = document.get_index_from_location(self.text_area.cursor_location)
        return self.completer.get_completions(text, index)
