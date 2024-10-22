import os
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout
from Antivirus import *

class Dashboard(QWidget):
    def __init__(self):
        super().__init__()

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.setFixedSize(743, 558)

        self.label1info = QLabel("", self)
        self.label1info.setWordWrap(True)

        label1 = QLabel("Number of Files Scanned:")
        trigger = QPushButton("Click to start scanning", self)
        trigger.clicked.connect(self.start_count_files)

        firstline = QHBoxLayout()
        firstline.addWidget(label1)
        firstline.addWidget(self.label1info)
        layout.addLayout(firstline)
        layout.addWidget(trigger)
        self.setLayout(layout)

        self.thread = None

    def start_count_files(self):
        if os.name == 'nt':
            start_path = "C:\\"
        else:
            start_path = "/"

        # Start the file counting thread
        self.thread = FileCounterThread(start_path)
        self.thread.file_count_updated.connect(self.update_file_count)
        self.thread.count_complete.connect(self.display_final_result)
        self.thread.start()

    def update_file_count(self, file_count):
        self.label1info.setText(str(file_count))

    def display_final_result(self, file_count):
        self.label1info.setText(f"Final Count: {file_count}")