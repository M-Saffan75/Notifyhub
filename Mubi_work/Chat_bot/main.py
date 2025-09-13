import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PyQt5.QtGui import QPixmap, QFont, QPalette, QBrush, QLinearGradient, QColor
from PyQt5.QtCore import Qt

class NoticeBoard(QWidget):
    def __init__(self):
        super().__init__()

        # Window Title
        self.setWindowTitle("Smart Notice Board")

        # Default Window Size (Normal Size)
        self.resize(800, 600)
        self.center()

        # Layout
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignCenter)

        # Image
        self.image_label = QLabel()
        pixmap = QPixmap("img1.png")  # Yaha apni image ka naam dalna
        pixmap = pixmap.scaled(400, 300, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.image_label.setPixmap(pixmap)
        self.image_label.setAlignment(Qt.AlignCenter)

        # Text
        self.text_label = QLabel("HELLO WORLD YE LE KARLIYA")
        self.text_label.setAlignment(Qt.AlignCenter)
        self.text_label.setFont(QFont("Arial Black", 20, QFont.Bold))
        self.text_label.setStyleSheet("color: red;")

        # Add to layout
        layout.addWidget(self.image_label)
        layout.addWidget(self.text_label)

        self.setLayout(layout)

        # Background Gradient
        palette = QPalette()
        gradient = QLinearGradient(0, 0, 0, self.height())
        gradient.setColorAt(0.0, QColor("#fceabb"))
        gradient.setColorAt(1.0, QColor("#f8b500"))
        palette.setBrush(QPalette.Window, QBrush(gradient))
        self.setAutoFillBackground(True)
        self.setPalette(palette)

    def center(self):
        """Screen ke beech me window ko center karne ka method"""
        qr = self.frameGeometry()
        cp = QApplication.desktop().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NoticeBoard()
    window.show()
    sys.exit(app.exec_())
