from PyQt6.QtWidgets import QWidget, QApplication, QLineEdit, QVBoxLayout, QPushButton
from PyQt6.QtGui import QIcon
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()


        self.showMaximized()
        self.setWindowTitle("J.A.R.V.I.S.")
        self.setWindowIcon(QIcon("jarvis_icon.png"))


        text = QLineEdit(self)
        text.setPlaceholderText("enter your message here.......")
        text_area = QVBoxLayout()

        send_button = QPushButton("Send")
        #send_button.clicked.connect(send_text)

        text_area.addWidget(text)
        text_area.addWidget(send_button)
        self.setLayout(text_area)

        def send_text(self):
            pass

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
