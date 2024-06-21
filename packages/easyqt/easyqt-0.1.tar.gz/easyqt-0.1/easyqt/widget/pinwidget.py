from PyQt5 import QtWidgets, QtGui, QtCore

from easyqt.widget import basicwidget
from easyqt.widget.integerwidget import IntegerWidget


class PinWidget(basicwidget.BasicWidget):
    completedPin = QtCore.pyqtSignal(str)
    firstIndex = QtCore.pyqtSignal()

    def __init__(self, count=4, reset_on_complete=True, width=30, height=40, font_size=20):
        super(PinWidget, self).__init__(vertical=False)

        self.count = count
        self.reset_on_complete = reset_on_complete

        i = 0

        for each in range(self.count):
            int_field = IntegerWidget(size=1)
            int_field.index = i
            int_field.valueSet = False
            int_field.setFixedSize(width, height)
            int_field.text_field.setFont(QtGui.QFont("Arial", font_size))
            self.basic_layout.addWidget(int_field)

            int_field.text_field.textChanged.connect(self.process_pins)

            i += 1

    def process_pins(self, _):

        int_widget: IntegerWidget = self.sender().parent()

        if not int_widget.get_integer():
            return

        int_widget.valueSet = True

        pin_number = self.get_pin_number()
        if len(pin_number) == self.count:
            self.complete_pin(pin_number)
        else:
            if int_widget.index == 0:
                self.firstIndex.emit()

            widget = self.get_next_empty_field()
            if widget:
                widget.focus()

    def complete_pin(self, value):
        self.completedPin.emit(value)
        if self.reset_on_complete is True:
            self.reset()

    def reset(self):
        for each in self.get_integer_widgets():
            each.valueSet = False
            each.clear()

        widget = self.get_integer_widget_by_index(0)
        if widget:
            widget.focus()

    def get_integer_widget_by_index(self, index) -> IntegerWidget:
        for each in self.get_integer_widgets():
            if each.index == index:
                return each

    def get_next_empty_field(self) -> IntegerWidget:
        for each in self.get_integer_widgets():
            if each.valueSet is False:
                return each

    def get_pin_number(self) -> str:

        pin_number = ''

        for each in self.get_integer_widgets():
            if not each.valueSet:
                continue

            pin_number += str(each.get_integer())

        return pin_number

    def get_integer_widgets(self) -> [IntegerWidget]:
        return sorted(self.findChildren(IntegerWidget), key=lambda x: x.index)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    wdg = PinWidget(count=4, width=80, height=100, font_size=60)
    wdg.show()
    wdg.completedPin.connect(lambda x: print(x))
    sys.exit(app.exec_())
