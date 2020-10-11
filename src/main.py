from aqt import gui_hooks, mw as main_window
from aqt.editor import Editor
from anki import hooks
from aqt import utils
from . import ui
from .data import rtkfill

BTN_TEXT_RTK = "RTK Fill"
BTN_TEXT_SHOW_STORIES = "Show Stories"
BTN_TEXT_HIDE_STORIES = "Hide Stories"
BRIDGE_CMD_RTK_FILL = "run_fill_rtk"
BRIDGE_CMD_STORIES_TOGGLE = "toggle_stories"

# These are to be Global
stories_browser = None
stories_browser_displayed = False


def cb_on_editor_did_load_hook(editor: Editor):
    global stories_browser, stories_browser_displayed
    if editor.addMode:
        ui.maybe_add_btn_to_top_left(editor, BTN_TEXT_RTK, "rtk-btn", BRIDGE_CMD_RTK_FILL)
        ui.maybe_add_btn_to_top_left(editor, BTN_TEXT_SHOW_STORIES, "rtk-stories",
                                     BRIDGE_CMD_STORIES_TOGGLE)
        add_cards_layout = ui.change_add_window_layout(editor)

        def init_browser():
            global stories_browser, stories_browser_displayed
            stories_browser = ui.AddCardsKoohieWebview()
            stories_browser.go_to_koohie()
            stories_browser_displayed = False

            ui.add_stories_view_to_hbox(add_cards_layout, stories_browser)
            stories_browser.setVisible(False)

        if stories_browser is None:
            init_browser()
        elif cpp_browser_deleted(stories_browser):
            init_browser()


def cpp_browser_deleted(browser: ui.AddCardsKoohieWebview) -> bool:
    try:
        browser.url()
        return False
    except RuntimeError:
        return True


def toggle_browser_visibility():
    global stories_browser_displayed
    if stories_browser is not None:
        stories_browser_displayed = not stories_browser_displayed
        stories_browser.setVisible(stories_browser_displayed)
    else:
        utils.showWarning("Stories Browser not initialized")


def cb_on_command_from_js_bridge(editor: Editor, cmd: str):
    global stories_browser
    if editor.addMode:
        if cmd == BRIDGE_CMD_RTK_FILL:
            col = main_window.col
            rtkfill.maybe_fill_editor_rtk_data(col, editor, stories_browser)
        elif cmd == BRIDGE_CMD_STORIES_TOGGLE:
            toggle_browser_visibility()


gui_hooks.editor_did_init.append(cb_on_editor_did_load_hook)
Editor.onBridgeCmd = hooks.wrap(Editor.onBridgeCmd, cb_on_command_from_js_bridge)
