from typing import Callable, Any

from PyQt5 import QtCore
from PyQt5.QtWidgets import QPushButton

from easyqt.widget import basicwidget
from easyqt.widget.fieldwidget import FieldWidget


class LoginWidget(basicwidget.BasicWidget):
    """
        Widget used to log in to something
        """
    loginResult = QtCore.pyqtSignal(object)

    def __init__(self, login_process: Callable[[str, str], Any]):
        super(LoginWidget, self).__init__(vertical=True)
        self.login_process = login_process

        self.email_field = FieldWidget(label='Email')
        self.password_field = FieldWidget(label='Password', password=True)
        self.submit_button = QPushButton('Submit')

        self.submit_button.clicked.connect(self.handle_login)

        self.basic_layout.addWidget(self.email_field)
        self.basic_layout.addWidget(self.password_field)
        self.basic_layout.addWidget(self.submit_button)

    def handle_login(self):
        result = self.login_process(self.email_field.text(), self.password_field.text())
        self.loginResult.emit(result)


if __name__ == '__main__':
    import sys

    from PyQt5 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)

    def login_process(email, password):
        print(f'Email: {email}, Password: {password}')
        return 'Success'

    lw = LoginWidget(login_process)
    lw.show()

    sys.exit(app.exec_())