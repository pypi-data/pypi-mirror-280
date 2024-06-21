from PyQt5 import QtWidgets
from PyQt5.QtCore import QSize, Qt


class TableWidget(QtWidgets.QTableWidget):
    """
    A dictionary friendly table widget.

    # TODO: Add support for lists
    """

    def __init__(self,
                 rows: int = None,
                 columns: int = None,
                 horizontal_header_list: list[str] = None,
                 vertical_header_list: list[str] = None):
        """

        :param rows:                    *(int)* number of rows
        :param columns:                 *(int)* number of columns.
        :param horizontal_header_list:  *(list(str))* list of strings to add as the horizontal header (fields)
        :param vertical_header_list:    *(list(str))* list of strings to add as the vertical header (fields)
        """
        super(TableWidget, self).__init__()

        # Data # TODO: Consider using "orientation" property
        self.header_type = 'horizontal'  # useful for reference as to the orientation of header

        # Initial rows/columns
        self.setRowCount(rows or 0)
        self.setColumnCount(columns or 0)

        # Headers
        if horizontal_header_list:
            self.header_type = 'horizontal'
            self.add_horizontal_header_list(horizontal_header_list)
            # self.horizontalHeader().setStretchLastSection(True)
        else:
            self.horizontalHeader().setVisible(False)

        if vertical_header_list:
            self.header_type = 'vertical'
            self.add_vertical_header_list(vertical_header_list)
            # self.verticalHeader().setStretchLastSection(False)
            # self.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Fixed)
            # self.verticalHeader().setDefaultSectionSize(24)
        else:
            self.verticalHeader().setVisible(False)

        # Default functionality
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.display_right_click_menu)

    def sizeHint(self):
        horizontal = self.horizontalHeader()
        vertical = self.verticalHeader()
        frame = self.frameWidth() * 2
        return QSize(horizontal.length() + vertical.width() + frame,
                     vertical.length() + horizontal.height() + frame)

    def display_right_click_menu(self, pos):
        """ implement menu in subclass """
        pass

    def add_horizontal_header_list(self, header_list):
        """

        :param header_list:
        :return:
        """
        self.setColumnCount(len(header_list))
        self.setHorizontalHeaderLabels(header_list)

    def add_vertical_header_list(self, header_list):
        self.setRowCount(len(header_list))
        self.setVerticalHeaderLabels(header_list)

    def get_next_empty_row(self):
        return self.rowCount()

    def get_next_empty_column(self):
        return self.columnCount()

    def get_row_from_header_name(self, header_name):
        """
        Return the row index with header name matching name passed
        # IMPORTANT: When checking return value make sure to verify None type as using "if not" will appear False on
                     column 0 (first column)

        :param header_name: *(str)* name of header
        :return:
        """
        for idx in range(self.rowCount()):
            item = self.verticalHeaderItem(idx)
            if item.text() == header_name:
                return idx

        return None

    def get_column_from_header_name(self, header_name):
        """
        Return the column index with header name matching name passed
        # IMPORTANT: When checking return value make sure to verify None type as using "if not" will appear False on
                     column 0 (first column)

        :param header_name: *(str)* name of header
        :return:
        """
        print('column?')
        for idx in range(self.columnCount()):
            item = self.horizontalHeaderItem(idx)
            if item.text() == header_name:
                return idx

        return None

    def get_header_name_from_column(self, column):
        return self.horizontalHeaderItem(column).text()

    def get_header_name_from_row(self, row):
        return self.verticalHeaderItem(row).text()

    def get_all_items_in_column(self, column):
        items = []

        for row in range(self.rowCount()):
            items.append(self.item(row, column))

        return items

    def add_row(self, data):
        """
        Add a single row of data. Simple dict, 1 level deep. Override in subclass for more functionality
        :param data:    *(dict)*
        :return:
        """
        row = self.get_next_empty_row()
        self.insertRow(row)

        for key, value in data.items():
            col = self.get_column_from_header_name(header_name=key)

            if col is None:
                continue

            entry_widget = QtWidgets.QTableWidgetItem(str(value))
            self.setItem(row, col, entry_widget)

    def add_column(self, data):
        """
        Add a single row of data. Simple dict, 1 level deep. Override in subclass for more functionality
        :param data:    *(dict)*
        :return:
        """
        col = self.get_next_empty_column()
        self.insertColumn(col)

        for key, value in data.items():
            row = self.get_row_from_header_name(header_name=key)

            if row is None:
                continue

            entry_widget = QtWidgets.QTableWidgetItem(str(value))
            self.setItem(row, col, entry_widget)

    def add_row_data(self, data):
        """
        Add multiple rows of data. Dictionary, 2 levels deep.
        :param data:    *(dict(dict))*
        :return:
        """
        for key, value in data.KEYS:
            self.add_row(value)

    def clear(self):
        if self.header_type == 'vertical':
            self.setColumnCount(0)
        else:
            self.setRowCount(0)


if __name__ == '__main__':
    import sys
    import collections

    from PyQt5 import QtWidgets

    app = QtWidgets.QApplication(sys.argv)

    dat = collections.OrderedDict()

    dat['name'] = 'Chair'
    dat['project'] = 'ProjectA'
    dat['resource_type'] = 'component'

    tab = TableWidget(vertical_header_list=list(dat.keys()))
    tab.show()
    tab.add_column(dat)

    sys.exit(app.exec_())
