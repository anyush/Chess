from PyQt5.QtWidgets import QMainWindow, QApplication
from PlayWindow import PlayWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setGeometry((QApplication.desktop().width() - 600) // 2, (QApplication.desktop().height() - 640) // 2, 600,
                         640)
        self.setFixedSize(600, 650)
        self.play_window = PlayWindow()
        self.setCentralWidget(self.play_window)
        self.show()
