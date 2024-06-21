from PyQt5 import QtWidgets


class QHSeparator(QtWidgets.QFrame):
    def __init__(self):
        super(QHSeparator, self).__init__()
        self.setFrameShape(QtWidgets.QFrame.HLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)


class QVSeparator(QtWidgets.QFrame):
    def __init__(self):
        super(QVSeparator, self).__init__()
        self.setFrameShape(QtWidgets.QFrame.VLine)
        self.setFrameShadow(QtWidgets.QFrame.Sunken)


if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)

    h = QHSeparator()
    h.show()

    v = QVSeparator()
    v.show()

    sys.exit(app.exec_())