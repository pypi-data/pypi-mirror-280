from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from easyqt.widget import basicwidget


class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, name=None, title=None, vertical=True, fixed_width=None, fixed_height=None):
        """

        :param name:
        :param title:
        :param vertical:
        :param fixed_width:
        :param fixed_height:
        """

        super(MainWindow, self).__init__()

        self.title = title

        if name is None:
            name = 'MainWindow'

        self.name = str(name)

        # Set object name and window title
        self.setObjectName(self.name)
        if title:
            self.setWindowTitle(str(title))
        else:
            self.setWindowTitle(self.name)

        self.mainWidget = basicwidget.BasicWidget(vertical=vertical)
        self.setCentralWidget(self.mainWidget)
        self.basic_layout = self.mainWidget.layout  # overrides self.layout builtin method

        # fixed heights
        if fixed_width:
            self.setFixedWidth(int(fixed_width))
        if fixed_height:
            self.setFixedWidth(int(fixed_height))

        self.setWindowFlags(Qt.Window)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    wdg = MainWindow(name='Main Window')
    wdg.show()

    sys.exit(app.exec_())
