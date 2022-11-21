from PyQt5 import QtWidgets
import sys
import Content

app = QtWidgets.QApplication(sys.argv)
cnt = Content.MyWindow()
cnt.show()
sys.exit(app.exec_())