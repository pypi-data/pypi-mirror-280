from pathlib import Path
from PyQt5 import QtGui, QtWidgets


class ToolBarWidget(QtWidgets.QToolBar):

    def __init__(self, *args):
        super(ToolBarWidget, self).__init__(*args)

    def add_action_tool_button(self, name: str, icon_path: Path = None) -> QtWidgets.QAction:
        """
        Add an action to the toolbar with a nice name and icon. Sets the objectName of the action to the name passed
        :param name:        *(str)* name of the action
        :param icon_path:   *(Path)* absolute filepath to icon
        :return:            *(QAction)* returns the action created
        """
        if icon_path and icon_path.is_file():
            action = QtWidgets.QAction(QtGui.QIcon(str(icon_path)), '&{}'.format(name.title()), self)
        else:
            action = QtWidgets.QAction('&{}'.format(name.title()), self)

        action.setObjectName(name)
        self.addAction(action)

        return action


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    win = QtWidgets.QMainWindow()

    tbw = ToolBarWidget()
    tbw.add_action_tool_button('open', Path('open.png'))

    win.addToolBar(tbw)
    win.show()
    sys.exit(app.exec_())
