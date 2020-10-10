from typing import List
from aqt import gui_hooks, mw as main_window
from aqt.editor import Editor
from aqt.browser import Browser
from aqt.addcards import AddCards
from aqt import utils
from aqt import qt
from anki import hooks
from anki.notes import Note
from . import ui
from .data import rtkfill


def cb_on_deck_browser_will_show(deck_browser: Browser):
    # deck_browser.sidebarDockWidget.setContentsMargins(100, 100, 100, 100)
    dock_widget = qt.QDockWidget(deck_browser)
    dock_widget.setAllowedAreas(qt.Qt.RightDockWidgetArea)
    dock_widget.setFeatures(qt.QDockWidget.NoDockWidgetFeatures)
    dock_widget.setTitleBarWidget(qt.QWidget(None))
    deck_browser.addDockWidget(qt.Qt.RightDockWidgetArea, dock_widget)

    view_widget = qt.QWidget()

    hbox = qt.QHBoxLayout()
    hbox.setContentsMargins(0, 0, 0, 0)
    view_widget.setLayout(hbox)
    dock_widget.setWidget(view_widget)

    stories = ui.AddCardsKoohieWebview()
    stories.setMinimumWidth(600)
    stories.go_to_koohie()
    hbox.addWidget(stories)


    # deck_browser.sidebarDockWidget.setVisible(True)

    # widget = qt.QWidget()
    # hbox = qt.QHBoxLayout(widget)
    # hbox.addWidget(qt.QPushButton("ZZZZ"))
    # deck_browser.parentWidget().setCentralWidget(widget)


    # q_dock_widget = qt.QDockWidget("WOOOOW")
    # deck_browser.addDockWidget(qt.Qt.RightDockWidgetArea, q_dock_widget)
    #
    # deck_browser.form.tableView
    # deck_browser.layout().addWidget(qt.QPushButton("ZZZZZZZZZZZ"))
    # deck_browser.form.gridLayout.addWidget(qt.QPushButton("Zzzzzzzz"), 0, 4)
    # brow_lay = deck_browser.layout()
    # t = str(type(brow_lay))
    # utils.showInfo(t)
    # editor = deck_browser.editor
    # if editor is not None:
    #     editor.web.parent().parent()


gui_hooks.browser_will_show.append(cb_on_deck_browser_will_show)
