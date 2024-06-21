from PyQt5 import QtWidgets

from easyqt.widget import basicwidget

# TODO: Not functioning yet


class CollapsibleWidget(basicwidget.BasicWidget):

    def __init__(self, vertical=True, panel_vertical_layout=True, length=200):
        super(CollapsibleWidget, self).__init__(vertical=vertical)

        # Data
        self.length = length

        # Widget
        self.header_widget = basicwidget.BasicWidget(vertical=not vertical)
        self.panel_widget = basicwidget.BasicWidget(vertical=panel_vertical_layout)

        # Layout
        self.basic_layout.addWidget(self.header_widget)
        self.basic_layout.addWidget(self.panel_widget)

    def add_widget_to_header(self, widget):
        self.header_widget.basic_layout.addWidget(widget)

    def add_widget_to_panel(self, widget):
        self.panel_widget.basic_layout.addWidget(widget)


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    cw = CollapsibleWidget()

    cw.header_widget.basic_layout.addWidget(QtWidgets.QLabel('testo!'))
    cw.panel_widget.basic_layout.addWidget(QtWidgets.QLabel('PANO!!'))
    cw.show()

    sys.exit(app.exec_())
