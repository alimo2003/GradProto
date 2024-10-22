import sys
from PySide6.QtCore import Qt, QPoint
from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QLabel, QHBoxLayout,QStackedWidget
from Sniffer import Snifferscene
from Dashboard import Dashboard
from Encryptor import Encryptor

class CustomMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.dashboardscene=Dashboard()
        self.snifferscened=Snifferscene()
        self.Encryp=Encryptor()

        # Remove the default window frame
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setFixedSize(900, 600)  # Set the size of the window
        self.setStyleSheet("background-color: ffffff; color: white; border: none")
        self.setContentsMargins(0,0,0,0)

        # Create custom title bar
        title_bar = QWidget(self)
        title_bar.setFixedHeight(40)
        title_bar.setStyleSheet("background-color: 000000; color: white; border:none;")
        title_bar.setContentsMargins(0,0,0,0)

        # Create a close button
        close_button = QPushButton("✕")
        close_button.setFixedSize(32, 38)
        close_button.setContentsMargins(0,0,0,0)
        close_button.setStyleSheet("QPushButton{ background-color: #000000; border: none; color: white; margin-top: 0;border:none;}QPushButton:hover{background-color: #262626}")
        close_button.clicked.connect(self.close)
    

        # Create a minimize button
        minimize_button = QPushButton("−")
        minimize_button.setFixedSize(32, 38)
        minimize_button.setStyleSheet("QPushButton{ background-color: #000000; border: none; color: white; margin-top: 0;border:none;}QPushButton:hover{background-color: #262626}")
        minimize_button.clicked.connect(self.showMinimized)

        # Title label
        title_label = QLabel("Cyber Z")
        title_label.setAlignment(Qt.AlignCenter)
        title_label.setStyleSheet("font-size: 25px;margin-left: 15px; margin-top: 2px")

        # Layout for title bar
        title_layout = QHBoxLayout()
        title_layout.addWidget(title_label)
        title_layout.addStretch()
        title_layout.addWidget(minimize_button)
        title_layout.addWidget(close_button)
        title_layout.setContentsMargins(0, 0, 0, 0)
        title_bar.setLayout(title_layout)

        # Side Navigation Bar
        side_nav = QWidget()
        side_nav.setFixedWidth(200)
        side_nav.setStyleSheet("background-color: #0d0d0d;")

        # Buttons of the side navbar 
        nav_layout= QVBoxLayout()
        nav_layout.setContentsMargins(0,0,0,0)
        nav_layout.setSpacing(0)
        nav_layout.addStretch()

        Dashboard_button = QPushButton("Dashboard")
        Dashboard_button.setStyleSheet("QPushButton{ background-color: #0d0d0d; border: none; color: white; padding: 10px;font-size:15;}QPushButton:hover{background-color: #262626}")
        Dashboard_button.clicked.connect(self.generatedashboard)

        MessageEND_button = QPushButton("Encryption and Decryption")
        MessageEND_button.setStyleSheet("QPushButton{ background-color: #0d0d0d; border: none; color: white; padding: 10px;font-size:15;}QPushButton:hover{background-color: #262626}")
        MessageEND_button.clicked.connect(self.generateencryptor)

        Sniffer_button = QPushButton("Packet Sniffer")
        Sniffer_button.setStyleSheet("QPushButton{ background-color: #0d0d0d; border: none; color: white; padding: 10px;font-size:15;}QPushButton:hover{background-color: #262626}")
        Sniffer_button.clicked.connect(self.generatesniffer)
        """
        AntiVirus_button = QPushButton("AntiVirus")
        AntiVirus_button.setStyleSheet("QPushButton{ background-color: #0d0d0d; border: none; color: white; padding: 10px;font-size:15;}QPushButton:hover{background-color: #262626}")
        AntiVirus_button.clicked.connect(self.generateAnti)
        """
       

        nav_layout.addWidget(Dashboard_button)
        nav_layout.addWidget(MessageEND_button)
        nav_layout.addWidget(Sniffer_button)
        #nav_layout.addWidget(AntiVirus_button)

        nav_layout.setContentsMargins(0,0,0,0)
        nav_layout.addStretch()
        side_nav.setLayout(nav_layout)
        side_nav.setContentsMargins(0,0,0,0)

        """    
        # Main Content Area
        main_content= QWidget()   
        main_content_layout= QGridLayout()
        main_content_layout.setContentsMargins(0,0,0,0)
   
        main_content_layout.addWidget(QLabel("PART ONE"),0,0)
        main_content_layout.addWidget(QLabel("PART TWO"),0,1)
        main_content_layout.addWidget(QLabel("PART THREE"),1,0)
        main_content_layout.addWidget(QLabel("PART FOUR"),1,1)
        main_content.setFixedSize(850,600)
        main_content.setStyleSheet("background-color: #ffffff; border: none; color: white;")
        main_content.setLayout(main_content_layout)
        """
        #Main content area 
        self.main_content= QStackedWidget()

        self.main_content.setContentsMargins(0,0,0,0)

        self.main_content.addWidget(self.dashboardscene)
        self.main_content.addWidget(self.snifferscened)
        #self.main_content.addWidget(self.Anti)
        self.main_content.addWidget(self.Encryp)

        # Combining MainContent, SideNav and Title Bar
        main_layout = QVBoxLayout()
        main_layout.addWidget(title_bar)
        main_layout.setContentsMargins(0,0,0,0)
        main_layout.setSpacing(0)
        
        centraLayout= QHBoxLayout()
        centraLayout.addWidget(side_nav)
        centraLayout.addWidget(self.main_content)
        centraLayout.addStretch()
        centraLayout.setContentsMargins(0,0,0,0)
        centraLayout.setSpacing(0)

        main_layout.addLayout(centraLayout)

        # Set central widget
        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

        # Variables for dragging the window
        self.old_pos = None

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.old_pos = event.globalPos()

    def mouseMoveEvent(self, event):
        if event.buttons() == Qt.LeftButton:
            delta = QPoint(event.globalPos() - self.old_pos)
            self.move(self.x() + delta.x(), self.y() + delta.y())
            self.old_pos = event.globalPos()

    def generateencryptor(self):
        self.main_content.setCurrentWidget(self.Encryp)
    """
    def generateAnti(self):
        self.main_content.setCurrentWidget(self.Anti)
    """
    
    
    def generatesniffer(self):
        self.main_content.setCurrentWidget(self.snifferscened)
    
    def generatedashboard(self):
        self.main_content.setCurrentWidget(self.dashboardscene)
        self.setContentsMargins(0,0,0,0)