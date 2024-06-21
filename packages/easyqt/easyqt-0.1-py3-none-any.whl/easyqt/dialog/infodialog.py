from typing import Optional

from PyQt5 import QtWidgets
from PyQt5.QtGui import QGuiApplication

from easyqt.dialog import basicdialog


class InfoDialog(basicdialog.BasicDialog):

    def __init__(self,
                 title: str = None,
                 message: str = None,
                 vertical: bool = True,
                 auto_exec: bool = False,
                 copy_button: bool = True):
        super(InfoDialog, self).__init__(vertical=vertical, auto_exec=False)

        self.title = title or 'Info'
        self.message = message or ''

        self.messageLabel = QtWidgets.QLabel(self.message)

        self.basic_layout.addWidget(self.messageLabel)

        if copy_button:
            self.copy_button = QtWidgets.QPushButton('Copy')
            self.basic_layout.addWidget(self.copy_button)
            self.copy_button.clicked.connect(self.copy_message_to_clipboard)

        self.setWindowTitle(self.title)

        if auto_exec:
            self.exec_()

    def copy_message_to_clipboard(self):
        cb = QGuiApplication.clipboard()
        cb.clear(mode=cb.Clipboard)
        cb.setText(self.message, mode=cb.Clipboard)

    def pop(self, message: Optional[str] = None):
        """
        quick popup message  and call exec_
        :param message: *(str)* message to display. If None will take original message
        :return:
        """
        self.message = message
        self.messageLabel.setText(message)

        self.exec_()


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)

    pd = InfoDialog(title='Warning', message='This is a detailed error message', vertical=True)

    pd.exec_()
