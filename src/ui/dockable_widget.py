from aqt.qt import QDockWidget, QResizeEvent, Qt
from aqt.main import AnkiQt
from aqt import pyqtSignal


class DockableWidget(QDockWidget):
    closed = pyqtSignal()

    def __init__(self, title, parent):
        super(DockableWidget, self).__init__(title, parent)

    def closeEvent(self, evt):
        self.closed.emit()
        QDockWidget.closeEvent(self, evt)

    def resizeEvent(self, evt):
        assert isinstance(evt, QResizeEvent)
        # SyncConfig.doc_size = (evt.size().width(),
        #                        evt.size().height())
        super(DockableWidget, self).resizeEvent(evt)
        evt.accept()


def add_dock(main_window: AnkiQt):
    dock = DockableWidget("The Dock", main_window)
    main_window.addDockWidget(Qt.RightDockWidgetArea, dock)
    # main_window.addDockWidget(Qt.RightDockWidgetArea, DockableWidget("The Dock", DockableWidget))
