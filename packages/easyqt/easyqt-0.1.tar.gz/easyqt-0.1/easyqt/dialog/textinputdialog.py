from PyQt5 import QtCore

from easyqt.dialog import basicdialog


class TextInputDialog(basicdialog.BasicDialog):
    textEntered = QtCore.pyqtSignal(str)

    def __init__(self, title=None, message=None, placeholder_text=None, vertical=True, width=None, auto_exec=False):
        super(TextInputDialog, self).__init__(title=title, vertical=vertical, width=width, auto_exec=False)

        # Data
        self.message = message
        self.text_ = None

        # Widgets
        self.lineEdit = QtWidgets.QLineEdit()
        self.messageLabel = QtWidgets.QLabel(str(self.message))

        # Layout
        if self.message:
            self.basic_layout.addWidget(self.messageLabel)

        self.basic_layout.addWidget(self.lineEdit)

        # Signal
        self.lineEdit.returnPressed.connect(self._selection_made)

        # Initial
        if placeholder_text:
            self.lineEdit.setPlaceholderText(str(placeholder_text))

        if auto_exec:
            self.exec_()

    def _selection_made(self):
        """ Programmatically emit the selection currently made on signal textEntered """
        self.text_ = str(self.lineEdit.text())

        self.textEntered.emit(self.text_)

        self.accept()


if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)

    pd = TextInputDialog(title='Input',
                         message='Please type something..',
                         placeholder_text='..anything..',
                         auto_exec=True)

    sys.exit(app.exec_())
