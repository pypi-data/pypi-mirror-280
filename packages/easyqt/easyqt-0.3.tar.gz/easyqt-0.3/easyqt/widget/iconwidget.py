from pathlib import Path

from easyqt.widget import basicwidget
from PyQt5 import QtGui, QtWidgets


class IconWidget(basicwidget.BasicWidget):
    """
    A small 15x15 px widget for displaying an icon.
    """
    def __init__(self, icon_path: Path = None, width: int = 32, height: int = 32):
        """

        :param icon_path:   *(Path)* icon filepath to display initially
        :param width:       *(int)*
        :param height:       *(int)*
        """
        super(IconWidget, self).__init__(vertical=True)

        # Data
        self.icon_path = icon_path
        self.width = width
        self.height = height

        # Widgets
        self.icon = QtWidgets.QLabel()

        # Formatting
        # self.icon.setGeometry(width, height, 0, 0)

        # Layout
        self.basic_layout.addWidget(self.icon)

        # Initial
        if icon_path.is_file():
            self.set_icon(icon_path=self.icon_path)

    def set_icon(self, icon_path: Path = None):
        """

        :param icon_path:
        :return:
        """
        if not icon_path.is_file():
            # Skip if path doesn't exist and make icon invisible
            self.icon.setVisible(False)
            return

        self.icon.setVisible(True)
        pix = QtGui.QPixmap(str(icon_path.absolute()))
        pix = pix.scaledToWidth(self.width)
        self.icon.setPixmap(pix)


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)

    path = Path('/home/test.jpg')
    fw = IconWidget(icon_path=path)
    fw.show()

    sys.exit(app.exec_())
