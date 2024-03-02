import sys

from PySide6.QtWidgets import QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget


from untitled_ui import Ui_MainWindow as Ui_MainWindow
import random
# from untitled2_ui import Ui_MainWindow111 as Ui_MainWindow2

class MainWindow1(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.yes.clicked.connect(self.yes_click)
        self.ui.no.clicked.connect(self.no_click)

    def yes_click(self):
        
        print('Yes')

    def no_click(self):
        random_x = random.randint(0, 400)
        random_y = random.randint(0, 200)
        self.ui.yes.setGeometry(0, 0, 1, 1)
        self.ui.no.setGeometry(random_x, random_y, 30, 30)
        print('No')


# class MainWindow2(QMainWindow):
#     def __init__(self):
#         super().__init__()

#         self.ui = Ui_MainWindow2()
#         self.ui.setupUi(self)

#     def yes_click(self):

#         print('Yes')

#     def no_click(self):
#         print('No')

if __name__ == "__main__":
    app = QApplication([])

    window = MainWindow1()
    window.show()

    sys.exit(app.exec_())