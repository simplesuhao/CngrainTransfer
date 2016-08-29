
import sys

from PyQt5 import QtWidgets, QtCore

app = QtWidgets.QApplication(sys.argv)

widget = QtWidgets.QWidget()

widget.resize(360, 360)

widget.setWindowTitle("政策性粮传输系统配置帮助")

widget.show()

sys.exit(app.exec_())
