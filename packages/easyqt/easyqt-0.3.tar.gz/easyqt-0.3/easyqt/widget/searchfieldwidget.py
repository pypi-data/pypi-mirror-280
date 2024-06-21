from PyQt5 import QtWidgets, QtCore
from PyQt5.QtCore import Qt


class SearchFieldWidget(QtWidgets.QLineEdit):

    textEntered = QtCore.pyqtSignal(str)

    def __init__(self, string_list=None):
        super(SearchFieldWidget, self).__init__()

        self.returnPressed.connect(self._selection_made)
        self.setPlaceholderText('search..')

        # Initial
        if string_list:
            self.update_string_list(string_list)

    def _selection_made(self):
        """ Programmatically emit the selection currently made on signal textEntered """
        self.textEntered.emit(str(self.text()))

    def update_string_list(self, string_list):
        """ Recreates the string list """
        model = QtCore.QStringListModel()
        model.setStringList(string_list)

        completer = QtWidgets.QCompleter()
        completer.setModel(model)
        completer.setFilterMode(Qt.MatchContains)
        completer.setCaseSensitivity(Qt.CaseInsensitive)
        
        self.setCompleter(completer)


if __name__ == '__main__':

    import sys

    app = QtWidgets.QApplication(sys.argv)

    search_list = ['some', 'words', 'to', 'search', 'for', 'in', 'the', 'search', 'field', 'widget']
    sf = SearchFieldWidget(string_list=search_list)
    sf.show()

    sys.exit(app.exec_())
