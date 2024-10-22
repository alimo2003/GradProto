import sys
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout, QGridLayout

class Encryptor(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        layout.addWidget(QLabel("Encryptor Scene"))
        self.setLayout(layout)