from aqt.editor import Editor
from aqt import qt
from aqt.addcards import AddCards

STRETCH_ADD_CARDS_LAYOUT = 1
STRETCH_STORIES_LAYOUT = 10


# Add a Button to the top left area of the Add Cards window next to the "Cards" and "Fields" buttons
# This area is made with HTML. The area of interest has a div with id=topbutsleft
# When these buttons are clicked, `pycmd` triggers a command that can be handled by
# wrapping editor.onBridgeCmd separately from the creation of this button.
def maybe_add_btn_to_top_left(editor: Editor, btn_text: str, btn_id: str, bridge_cmd: str):
    html_text = """
    (() => {
        var btn = document.getElementById('%s');
        if (!btn) {
            document.getElementById('topbutsleft').innerHTML += `<button id='%s' onclick='pycmd("%s")'>%s</button> `;
        }
        return []
    })();
    """ % (btn_id, btn_id, bridge_cmd, btn_text)
    editor.web.evalWithCallback(html_text, lambda _: None)


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
