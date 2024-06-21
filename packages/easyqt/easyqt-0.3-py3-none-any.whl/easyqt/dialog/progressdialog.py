from typing import Optional

from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt


class ProgressDialog(QtWidgets.QProgressDialog):

    def __init__(self):
        super(ProgressDialog, self).__init__()

        self.setWindowModality(Qt.WindowModal)
        self.setWindowTitle("Progress..")
        self.setCancelButton(None)  # Disallow canceling
        self.setRange(0, 100)  # Spinner mode (not a progress bar)
        self.setMinimumDuration(3000)
        self.close()  # Start out hidden

    def show(self, title: Optional[str] = None) -> None:
        if title:
            self.setWindowTitle(title)
        super(ProgressDialog, self).show()
