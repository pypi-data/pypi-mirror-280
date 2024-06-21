from typing import Optional

from PyQt5 import QtWidgets

from easyqt.widget import buttongroupwidget
from easyqt.dialog import basicdialog

DEFAULT_BUTTON_LIST = [
    ('yes', 'Yes'),
    ('no', 'No'),
    ('cancel', 'Cancel'),
]


class ConfirmDialog(basicdialog.BasicDialog):

    def __init__(self, title=None, message=None, vertical=True, auto_exec=False,
                 button_list: Optional[tuple[str, str]]=None):
        super(ConfirmDialog, self).__init__(title=title, vertical=vertical, auto_exec=False)

        self.title = title or 'Confirm...'
        self.message = message or '..'
        self.button_list = button_list or DEFAULT_BUTTON_LIST

        # Widgets
        self.messageLabel = QtWidgets.QLabel(self.message)
        self.button_group = buttongroupwidget.ButtonGroupWidget(button_list=self.button_list)

        # Layout
        self.basic_layout.addWidget(self.messageLabel)
        self.basic_layout.addWidget(self.button_group)

        # Signals
        self.button_group.yes.clicked.connect(self.accept)
        self.button_group.no.clicked.connect(self.reject)
        self.button_group.cancel.clicked.connect(self.cancel_)

        self.setWindowTitle(self.title)

        if auto_exec:
            self.exec_()

    def cancel_(self):
        """

        :return:
        """
        self.result_ = 'cancel'
        self.reject()


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)

    pd = ConfirmDialog(title='Confirm something', message='are you sure?', vertical=True)

    pd.exec_()
