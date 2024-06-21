import logging

from PyQt5 import QtWidgets


class BasicWidget(QtWidgets.QWidget):

    def __init__(self, vertical=True, margins=None, parent=None):
        super(BasicWidget, self).__init__(parent=parent)

        if margins is None:
            margins = [0, 0, 0, 0]

        self.setContentsMargins(margins[0], margins[1], margins[2], margins[3])

        if vertical:
            self.basic_layout = QtWidgets.QVBoxLayout()
        else:
            self.basic_layout = QtWidgets.QHBoxLayout()

        self.basic_layout.setSpacing(2)
        self.basic_layout.setContentsMargins(0, 0, 0, 0)
        self.setLayout(self.basic_layout)

        self.log = logging.getLogger(self.__repr__())

        # Set logger
        self.log.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        fmt = logging.Formatter('%(levelname)s:%(message)s')
        ch.setFormatter(fmt)

        self.log.addHandler(ch)

        self.setSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    wdg = BasicWidget(vertical=False)
    b = QtWidgets.QPushButton('test')

    wdg.basic_layout.addWidget(b)

    wdg.show()
