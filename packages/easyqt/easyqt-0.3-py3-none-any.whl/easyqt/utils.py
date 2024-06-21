from PyQt5.QtWidgets import QWidget


def center_widget_in_another(widget1: QWidget, widget2: QWidget):
    parent_rect = widget2.window().rect()
    geo = widget1.geometry()
    geo.moveCenter(parent_rect.center())
    widget1.setGeometry(geo)
