from PyQt5 import QtWidgets


class ScrollArea(QtWidgets.QScrollArea):

    def __init__(self, auto_scroll=False, **kwargs):
        super(ScrollArea, self).__init__(**kwargs)

        self.auto_scroll = auto_scroll

        if auto_scroll:
            # Passes the maximum of the range to do_scroll method
            self.verticalScrollBar().rangeChanged.connect(lambda x, y: self.do_scroll(y))

    def do_scroll(self, value):
        """ Scrolls the area to the value passed. I think its in pixels? """
        self.verticalScrollBar().setValue(value)
