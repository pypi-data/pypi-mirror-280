from PyQt5 import QtWidgets
from easyqt.window import dockingwindow


class DockingWidget(QtWidgets.QDockWidget):

    def __init__(self, name=None, title=None, *args):
        super(DockingWidget, self).__init__(*args)

        self.docking_window = dockingwindow.DockingWindow(name=name, title=title)
        self.setWidget(self.docking_window)

    def set_main_widget(self, widget):
        self.docking_window.setCentralWidget(widget)

    def __getattr__(self, item):
        try:
            # Pass all __getattr__ calls direct to docking_window. As this widget is simply a look through
            return getattr(self.docking_window, item)
        except AttributeError:
            return super(DockingWidget, self).__getattribute__(item)
