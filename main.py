import sys
from PyQt5.QtWidgets import QMainWindow, QWidget, QPushButton, QLabel, QApplication, qApp, QHBoxLayout, QVBoxLayout
from PyQt5.QtGui import QPalette, QColor
from MainWindow import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    main_window = MainWindow()
    qApp.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.Window, QColor(25, 50, 50))
    palette.setColor(QPalette.Button, QColor(12, 30, 58))
    palette.setColor(QPalette.Foreground, QColor(255, 0, 0))
    app.setPalette(palette)
    sys.exit(app.exec_())
