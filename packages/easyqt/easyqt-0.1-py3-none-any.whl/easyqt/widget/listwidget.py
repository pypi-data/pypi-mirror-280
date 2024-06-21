from PyQt5 import QtWidgets, QtGui
from PyQt5.QtCore import Qt

from easyqt.widget import basicwidget


class ListWidget(basicwidget.BasicWidget):

    def __init__(self, vertical=True):
        super(ListWidget, self).__init__(vertical=vertical)

        self.basic_layout.setSpacing(0)

    def add_item(self, widget):
        self.basic_layout.addWidget(widget)

    def clear(self):
        for i in reversed(range(self.basic_layout.count())):
            self.basic_layout.itemAt(i).widget().setParent(None)


class ScrollableListWidget(basicwidget.BasicWidget):

    def __init__(self, vertical=True):
        super(ScrollableListWidget, self).__init__(vertical=True)

        self.listWidget = ListWidget(vertical=vertical)

        self.scrollArea = QtWidgets.QScrollArea()
        self.scrollArea.setBackgroundRole(QtGui.QPalette.Dark)
        self.basic_layout.addWidget(self.scrollArea)

        self.scrollArea.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setWidget(self.listWidget)

        self.listWidget.basic_layout.setAlignment(Qt.AlignTop)

    def add_item(self, widget):
        """
        Pass command through to listWidget

        :param widget:
        :return:
        """
        self.listWidget.add_item(widget)

    def clear(self):
        self.listWidget.clear()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    slw = ScrollableListWidget()

    for i in range(10):
        slw.add_item(QtWidgets.QLabel('testo!'))

    slw.show()

    sys.exit(app.exec_())