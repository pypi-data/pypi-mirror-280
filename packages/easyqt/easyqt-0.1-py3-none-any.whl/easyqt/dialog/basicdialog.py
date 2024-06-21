from PyQt5 import QtWidgets
from easyqt.widget import basicwidget


class BasicDialog(QtWidgets.QDialog):

    def __init__(self, title=None, vertical=True, width=None, auto_exec=False):
        super(BasicDialog, self).__init__()

        self.title = title or ''

        self.result_ = None  # For storing the result() as a string, e.g. "accept"

        # Widgets
        self.basicWidget = basicwidget.BasicWidget(vertical=vertical)
        self.vBoxLayout = QtWidgets.QVBoxLayout()

        # Layout
        self.vBoxLayout.addWidget(self.basicWidget)
        self.setLayout(self.vBoxLayout)

        self.basic_layout = self.basicWidget.layout()

        # Format
        if width:
            assert isinstance(width, int)
            self.basicWidget.setMinimumWidth(width)

        self.setWindowTitle(self.title)

        if auto_exec:
            self.exec_()

    def reject(self):
        self.result_ = 'reject'
        super(BasicDialog, self).reject()

    def accept(self):
        self.result_ = 'accept'
        super(BasicDialog, self).accept()


if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets
    app = QtWidgets.QApplication(sys.argv)

    pd = BasicDialog(vertical=True)

    but = QtWidgets.QPushButton('something')
    pd.basic_layout.addWidget(but)

    pd.exec_()
