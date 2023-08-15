from aqt import mw as main_window
from aqt.editor import Editor
from aqt import utils, qt
from typing import Optional
from . import ui
from .data import rtkfill
from aqt import gui_hooks

BTN_TEXT_RTK = "RTK Fill"
CMD_RTK_FILL = "run_fill_rtk"
CMD_STORIES_TOGGLE = "toggle_stories"

# These are to be Global
add_cards_layout: Optional[qt.QHBoxLayout] = None
stories_browser: Optional[ui.AddCardsKoohieWebview] = None
stories_browser_displayed = False


def make_editor_ui_updates(buttons: list[str], editor: Editor):
    updated_btns = add_editor_buttons(buttons, editor)
    init_koohie_browser(editor)
    return updated_btns


def update_editor_layout(editor: Editor):
    global add_cards_layout
    add_cards_layout = ui.change_add_window_layout(editor)


def add_editor_buttons(buttons: list[str], editor: Editor):
    buttons.append(
        ui.make_editor_ui_button(editor, CMD_RTK_FILL, on_rtk_fill_btn_pressed, label=BTN_TEXT_RTK))
    buttons.append(
        ui.make_editor_ui_button(editor,
                                 CMD_STORIES_TOGGLE,
                                 on_koohie_btn_pressed,
                                 icon="cup-hot-fill.svg"))
    return buttons


def init_koohie_browser(editor: Editor):
    global stories_browser, stories_browser_displayed

    if add_cards_layout is None:
        update_editor_layout(editor)

    stories_browser = ui.AddCardsKoohieWebview()
    stories_browser_displayed = False
    ui.add_stories_view_to_hbox(add_cards_layout, stories_browser)
    stories_browser.go_to_koohie()
    stories_browser.setVisible(stories_browser_displayed)


def on_rtk_fill_btn_pressed(editor: Editor):
    col = main_window.col
    rtkfill.maybe_fill_editor_rtk_data(col, editor, stories_browser)


def on_koohie_btn_pressed(editor: Editor):
    print("koohie")
    global stories_browser, stories_browser_displayed
    if stories_browser is None or cpp_browser_deleted(stories_browser):
        print("No stories browser")
        init_koohie_browser(editor)

    stories_browser_displayed = not stories_browser_displayed
    print("Boolean: " + str(stories_browser_displayed))
    stories_browser.setVisible(stories_browser_displayed)


def cpp_browser_deleted(browser: ui.AddCardsKoohieWebview) -> bool:
    try:
        browser.url()
        return False
    except RuntimeError:
        return True


# Set up hooks
gui_hooks.editor_did_init_buttons.append(make_editor_ui_updates)
