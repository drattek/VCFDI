import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # Set the window title and size
        self.setWindowTitle("PySide6 Sample")
        self.setGeometry(100, 100, 400, 200)

        # Create a label widget
        self.label = QLabel("Hello, PySide6!", self)
        self.label.setGeometry(150, 80, 150, 30)

        # Create a button widget
        self.button = QPushButton("Click Me", self)
        self.button.setGeometry(150, 120, 100, 30)
        self.button.clicked.connect(self.button_clicked)

    def button_clicked(self):
        self.label.setText("Button Clicked!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())