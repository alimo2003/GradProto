import os
from PySide6.QtCore import Qt, QThread, Signal
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout

class FileCounterThread(QThread):
    file_count_updated = Signal(int)  # Signal to update file count in real-time
    count_complete = Signal(int)      # Signal to emit the final count

    def __init__(self, start_path):
        super().__init__()
        self.start_path = start_path

    def run(self):
        file_count = 0
        try:
            for dirpath, dirnames, filenames in os.walk(self.start_path):
                file_count += len(filenames)
                self.file_count_updated.emit(file_count)  # Emit updated count
        except Exception as e:
            print(f"Error occurred: {e}")
        self.count_complete.emit(file_count)  # Emit the final count