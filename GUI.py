from PySide6.QtWidgets import QApplication, QWidget, QPushButton,QMainWindow
import sys
from Generator import *

if __name__ == "__main__":
    app = QApplication([])
    window = CustomMainWindow()
    window.show()
    sys.exit(app.exec())
