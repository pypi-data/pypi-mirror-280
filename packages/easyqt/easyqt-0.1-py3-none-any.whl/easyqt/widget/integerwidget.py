from easyqt.widget import fieldwidget

from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtCore import QRegExp


class IntegerWidget(fieldwidget.FieldWidget):

    def __init__(self, size=1):
        super(IntegerWidget, self).__init__(label=None)

        rx = QRegExp('^[1-9]'.format(size))
        validator = QRegExpValidator(rx)

        self.text_field.setValidator(validator)

    def get_integer(self) -> int:
        value = self.text_field.text()
        if value and value.isdigit():
            return int(value)


if __name__ == '__main__':
    import sys
    from PyQt5 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)

    iw = IntegerWidget()
    iw.show()

    sys.exit(app.exec_())
