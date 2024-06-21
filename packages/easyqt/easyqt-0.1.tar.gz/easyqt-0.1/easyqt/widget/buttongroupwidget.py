from PyQt5 import QtWidgets, QtCore

from easyqt.widget import basicwidget


class ButtonGroupWidget(basicwidget.BasicWidget):
    """
    A group of widgets with horizontal or vertical layout.

    EXAMPLE::

            buttonList = [('test1', 'TestONE'), ('test2', 'TestTWO')]
            fw = ButtonGroupWidget(button_list=buttonList, label='My Test', exclusive=True)
            fw.show()

    """
    FONT_GRAY = 'color: rgb(160, 160, 160)'

    buttonClicked = QtCore.pyqtSignal(QtWidgets.QPushButton)

    def __init__(self, button_list=None, label=None, vertical=False, exclusive=False, exclusive_color='#46c878'):
        """

        :param button_list:     *(list(tuple))* list of string tuples. [(name, label)]
        :param label:           *(str)* visible label or "title" for the button group
        :param vertical:        *(bool)* if True will lay buttons out vertically
        :param exclusive:       *(bool)* if True will highlight button clicked and ghost the rest
                                via get_exclusive_button() or get_exclusive_button_name()
        :param exclusive_color  *(str)* hex colour to use if exclusive option is True
        """
        super(ButtonGroupWidget, self).__init__(vertical=vertical)

        self.button_list = button_list or []
        self.exclusive = exclusive
        self.exclusive_color = exclusive_color

        if label:
            label = QtWidgets.QLabel(label)
            self.basic_layout.addWidget(label)

        for each in self.button_list:
            button = QtWidgets.QPushButton(each[1])
            button.setObjectName(each[0])
            button.exclusive = False
            button.clicked.connect(self.button_clicked)
            self.basic_layout.addWidget(button)

    def __getattr__(self, item):

        # Get button by dot notation
        b = self.get_button_by_name(item)

        if b:
            return b
        else:
            return super(ButtonGroupWidget, self).__getattribute__(item)

    def get_all_buttons(self):
        return self.findChildren(QtWidgets.QPushButton)

    def get_button_by_name(self, name):
        """
        Returns the QPushButton that has name matching name passed
        :param name:
        :return:
        """
        for each in self.get_all_buttons():
            if each.objectName() == name:
                return each

    def button_clicked(self):
        """
        This executes when a button is clicked.

        :return:
        """
        button = self.sender()

        if self.exclusive:

            button.setStyleSheet('background-color: {}'.format(self.exclusive_color))
            button.exclusive = True

            for each in [x for x in self.get_all_buttons() if x.objectName() != button.objectName()]:
                each.exclusive = False
                each.setStyleSheet(self.FONT_GRAY)

        self.buttonClicked.emit(button)

    def get_exclusive_button(self):
        """
        :return:    *(QtGui.QPushButton)*
        """
        if not self.exclusive:
            raise RuntimeError('This ButtonGroupWidget has not been instantiated with param exclusive = True')

        for each in self.get_all_buttons():
            if each.exclusive:
                return each

    def get_exclusive_button_name(self):
        """
        :return:    *(str)* name of the exclusive button
        """
        return self.get_exclusive_button().objectName()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    buttonList = [('test1', 'TestONE'), ('test2', 'TestTWO')]
    fw = ButtonGroupWidget(button_list=buttonList, label='My Test', exclusive=True, vertical=True)
    fw.show()

    app.exec_()
