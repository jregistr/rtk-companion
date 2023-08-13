from aqt.editor import Editor
from aqt import qt
from aqt.addcards import AddCards

from typing import Callable, Optional

from ..project import support_files_path
from os import path

STRETCH_ADD_CARDS_LAYOUT = 10
STRETCH_STORIES_LAYOUT = 5


def make_editor_ui_button(editor: Editor,
                          cmd: str,
                          callback: Callable[[Editor], None],
                          label: str = "",
                          icon: Optional[str] = None):
    icon_path = None
    if icon is not None:
        icon_path = path.join(support_files_path, "icons", icon)
    return editor.addButton(icon=icon_path, cmd=cmd, label=label, func=callback)


# The default layout of the Add Cards window is a VBox. Since a webview
# will be placed on the right of the add fields and buttons, the layout
# must be changed into an HBox Layout.
# This function moves all UI elements from the old layout to a new VBox
# which becomes ultimately a child element of a new HBox layout.
def change_add_window_layout(add_cards_editor: Editor) -> qt.QHBoxLayout:
    add_cards: AddCards = add_cards_editor.web.parent().parent()
    assert (isinstance(add_cards, AddCards))
    old_vbox: qt.QLayout = add_cards.layout()
    new_vbox = qt.QVBoxLayout()

    # Push all UI objects from old vbox layout to a new one
    while old_vbox.count() > 0:
        ui_obj: qt.QLayoutItem = old_vbox.takeAt(0)
        if ui_obj.widget() is None or isinstance(ui_obj, qt.QLayout):
            new_vbox.addLayout(ui_obj.layout())
        else:
            new_vbox.addWidget(ui_obj.widget())

    trash = qt.QWidget()
    trash.setLayout(old_vbox)

    # All existing UI item now children of this basic widget
    existing_ui_parent = qt.QWidget()
    existing_ui_parent.setLayout(new_vbox)

    hbox_layout = qt.QHBoxLayout()
    hbox_layout.setContentsMargins(0, 0, 0, 0)
    hbox_layout.setSpacing(0)

    hbox_layout.addWidget(existing_ui_parent, STRETCH_ADD_CARDS_LAYOUT)
    add_cards.setLayout(hbox_layout)
    return hbox_layout


def add_stories_view_to_hbox(parent: qt.QHBoxLayout, stories_view):
    parent.addWidget(stories_view, STRETCH_STORIES_LAYOUT)
