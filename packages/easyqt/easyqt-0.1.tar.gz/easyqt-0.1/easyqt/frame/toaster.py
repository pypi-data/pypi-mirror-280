from typing import Optional

from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtCore import Qt, QEvent, QTimer, QPropertyAnimation
from PyQt5.QtWidgets import QStyle, QWidget


class Toaster(QtWidgets.QFrame):
    closed = QtCore.pyqtSignal()

    def __init__(self, *args, **kwargs):
        super(Toaster, self).__init__(*args, **kwargs)
        QtWidgets.QHBoxLayout(self)

        self.setSizePolicy(QtWidgets.QSizePolicy.Maximum,
                           QtWidgets.QSizePolicy.Maximum)

        self.setStyleSheet('''
            QToaster {
                border: 1px solid black;
                border-radius: 4px; 
                background: palette(window);
            }
        ''')
        # alternatively:
        # self.setAutoFillBackground(True)
        # self.setFrameShape(self.Box)

        self.timer = QTimer(singleShot=True, timeout=self.hide)

        if self.parent():
            self.opacityEffect = QtWidgets.QGraphicsOpacityEffect()
            self.setGraphicsEffect(self.opacityEffect)
            self.opacity_ani = QtCore.QPropertyAnimation(self.opacityEffect, b'opacity')
            # we have a parent, install an eventFilter so that when it's resized
            # the notification will be correctly moved to the right corner
            self.parent().installEventFilter(self)
        else:
            # there's no parent, use the window opacity property, assuming that
            # the window manager supports it; if it doesn't, this won't do
            # anything (besides making the hiding a bit longer by half a second)
            self.opacity_ani = QtCore.QPropertyAnimation(self, b'windowOpacity')
        self.opacity_ani.setStartValue(0.)
        self.opacity_ani.setEndValue(1.)
        self.opacity_ani.setDuration(100)
        self.opacity_ani.finished.connect(self.check_closed)

        self.corner = Qt.TopLeftCorner
        self.margin = 10

    def check_closed(self):
        # if we have been fading out, we're closing the notification
        if self.opacity_ani.direction() == QPropertyAnimation.Backward:
            self.close()

    def restore(self):
        # this is a "helper function", that can be called from mouseEnterEvent
        # and when the parent widget is resized. We will not close the
        # notification if the mouse is in or the parent is resized
        self.timer.stop()
        # also, stop the animation if it's fading out...
        self.opacity_ani.stop()
        # ...and restore the opacity
        if self.parent():
            self.opacityEffect.setOpacity(1)
        else:
            self.setWindowOpacity(1)

    def hide(self):
        # start hiding
        self.opacity_ani.setDirection(QPropertyAnimation.Backward)
        self.opacity_ani.setDuration(500)
        self.opacity_ani.start()

    def eventFilter(self, source, event):
        if source == self.parent() and event.type() == QEvent.Resize:
            self.opacity_ani.stop()
            parent_rect = self.parent().rect()
            geo = self.geometry()
            if self.corner == Qt.TopLeftCorner:
                geo.moveTopLeft(
                    parent_rect.topLeft() + QtCore.QPoint(self.margin, self.margin))
            elif self.corner == Qt.TopRightCorner:
                geo.moveTopRight(
                    parent_rect.topRight() + QtCore.QPoint(-self.margin, self.margin))
            elif self.corner == Qt.BottomRightCorner:
                geo.moveBottomRight(
                    parent_rect.bottomRight() + QtCore.QPoint(-self.margin, -self.margin))
            else:
                geo.moveBottomLeft(
                    parent_rect.bottomLeft() + QtCore.QPoint(self.margin, -self.margin))
            self.setGeometry(geo)
            self.restore()
            self.timer.start()
        return super(Toaster, self).eventFilter(source, event)

    def enterEvent(self, event):
        self.restore()

    def leaveEvent(self, event):
        self.timer.start()

    def closeEvent(self, event):
        # we don't need the notification anymore, delete it!
        self.deleteLater()

    def resizeEvent(self, event):
        super(Toaster, self).resizeEvent(event)
        # if you don't set a stylesheet, you don't need any of the following!
        if not self.parent():
            # there's no parent, so we need to update the mask
            path = QtGui.QPainterPath()
            path.addRoundedRect(QtCore.QRectF(self.rect()).translated(-.5, -.5), 4, 4)
            self.setMask(QtGui.QRegion(path.toFillPolygon(QtGui.QTransform()).toPolygon()))
        else:
            self.clearMask()


def show_message(parent: QWidget, message: str,
                 icon: Optional[int] = QStyle.SP_MessageBoxInformation,
                 corner: Optional[int] = Qt.BottomRightCorner,
                 margin: Optional[int] = 10,
                 closable: Optional[bool] = True,
                 timeout: Optional[int] = 2000,
                 desktop: Optional[bool] = False,
                 parent_window: Optional[bool] = True,
                 background_color: Optional[str] = '') -> Toaster:
    if parent and parent_window:
        parent = parent.window()

    if not parent or desktop:
        toaster = Toaster(None)
        toaster.setWindowFlags(toaster.windowFlags() | Qt.FramelessWindowHint | Qt.BypassWindowManagerHint)
        # This is a dirty hack!
        # parentless objects are garbage collected, so the widget will be
        # deleted as soon as the function that calls it returns, but if an
        # object is referenced to *any* other object it will not, at least
        # for PyQt (I didn't test it to a deeper level)
        toaster.__self = toaster

        current_screen = QtWidgets.QApplication.primaryScreen()
        if parent and parent.window().geometry().size().isValid():
            # the notification is to be shown on the desktop, but there is a
            # parent that is (theoretically) visible and mapped, we'll try to
            # use its geometry as a reference to guess which desktop shows
            # most of its area; if the parent is not a top level window, use
            # that as a reference
            reference = parent.window().geometry()
        else:
            # the parent has not been mapped yet, let's use the cursor as a
            # reference for the screen
            reference = QtCore.QRect(
                QtGui.QCursor.pos() - QtCore.QPoint(1, 1),
                QtCore.QSize(3, 3))
        max_area = 0
        for screen in QtWidgets.QApplication.screens():
            intersected = screen.geometry().intersected(reference)
            area = intersected.width() * intersected.height()
            if area > max_area:
                max_area = area
                current_screen = screen
        parent_rect = current_screen.availableGeometry()
    else:
        toaster = Toaster(parent)
        parent_rect = parent.rect()

    toaster.timer.setInterval(timeout)

    # use Qt standard icon pix-maps; see:
    # https://doc.qt.io/qt-5/qstyle.html#StandardPixmap-enum
    if isinstance(icon, QtWidgets.QStyle.StandardPixmap):
        label_icon = QtWidgets.QLabel()
        toaster.layout().addWidget(label_icon)
        icon = toaster.style().standardIcon(icon)
        size = toaster.style().pixelMetric(QStyle.PM_SmallIconSize)
        label_icon.setPixmap(icon.pixmap(size))

    toaster.label = QtWidgets.QLabel(message)
    toaster.layout().addWidget(toaster.label)

    if closable:
        toaster.closeButton = QtWidgets.QToolButton()
        toaster.layout().addWidget(toaster.closeButton)
        close_icon = toaster.style().standardIcon(QStyle.SP_DialogCloseButton)
        toaster.closeButton.setIcon(close_icon)
        toaster.closeButton.setAutoRaise(True)
        toaster.closeButton.clicked.connect(toaster.close)

    if background_color:
        toaster.setStyleSheet(f"background-color: {background_color}")

    toaster.timer.start()

    # raise the widget and adjust its size to the minimum
    toaster.raise_()
    toaster.adjustSize()

    toaster.corner = corner
    toaster.margin = margin

    geo = toaster.geometry()
    # now the widget should have the correct size hints, let's move it to the
    # right place
    if corner == Qt.TopLeftCorner:
        geo.moveTopLeft(
            parent_rect.topLeft() + QtCore.QPoint(margin, margin))
    elif corner == Qt.TopRightCorner:
        geo.moveTopRight(
            parent_rect.topRight() + QtCore.QPoint(-margin, margin))
    elif corner == Qt.BottomRightCorner:
        geo.moveBottomRight(
            parent_rect.bottomRight() + QtCore.QPoint(-margin, -margin))
    else:
        geo.moveBottomLeft(
            parent_rect.bottomLeft() + QtCore.QPoint(margin, -margin))

    toaster.setGeometry(geo)
    toaster.show()
    toaster.opacity_ani.start()

    return toaster


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)

    w = QtWidgets.QWidget()
    w.resize(400, 300)
    w.show()

    show_message(w, 'This is a test message', icon=QStyle.SP_MessageBoxQuestion, timeout=2000)

    app.exec_()
