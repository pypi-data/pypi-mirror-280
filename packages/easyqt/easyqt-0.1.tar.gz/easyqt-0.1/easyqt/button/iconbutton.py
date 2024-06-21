from PyQt5 import QtGui, QtWidgets


class IconButton(QtWidgets.QPushButton):

    def __init__(self, icon_path, *args):
        super(IconButton, self).__init__(*args)

        icon = QtGui.QIcon(icon_path)
        self.setIcon(icon)
