from PyQt5 import QtCore, QtWidgets
from easyqt.widget import basicwidget


class CheckBoxGroupWidget(basicwidget.BasicWidget):

    checkbox_state_changed = QtCore.pyqtSignal(tuple)

    def __init__(self, items=None, vertical=True):
        super(CheckBoxGroupWidget, self).__init__(vertical=vertical)

        self.items = items

        if items:
            self.add_items(items)

    def add_items(self, items):

        for each in items:
            self.add_item(each)

    def add_item(self, item):

        if isinstance(item, tuple):
            cb = QtWidgets.QCheckBox(item[1])
            cb.setObjectName(item[0])
        else:
            cb = QtWidgets.QCheckBox(item)
            cb.setObjectName(item)

        cb.stateChanged.connect(self._state_changed)
        self.basic_layout.addWidget(cb)

    def get_all_checkboxes(self):

        return self.findChildren(QtWidgets.QCheckBox)

    def get_checked_widgets(self):

        widgets = []

        for each in self.get_all_checkboxes():
            if each.isChecked() is True:
                widgets.append(each)

        return widgets

    def get_checked_names(self):

        return [x.objectName() for x in self.get_checked_widgets()]

    def _state_changed(self, state):

        if state == 0:
            state = False
        elif state == 1:
            raise NotImplementedError('Currently does not support Qt.PartiallyChecked state yet')
        elif state == 2:
            state = True

        checkbox_name = self.sender().objectName()

        self.checkbox_state_changed.emit((checkbox_name, state))


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    wdg = CheckBoxGroupWidget(items=[('a', 'A'), ('b', 'B'), ('c', 'C')])
    wdg.show()

    app.exec_()
