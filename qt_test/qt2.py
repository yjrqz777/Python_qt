from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import QFile
import picture_rc

class Stats:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        file = QFile("./qt_test/untitled.ui")
        self.ui = QUiLoader().load(file)

        # self.ui.yes.clicked.connect(self.handleCalc)

    def handleCalc(self):
        print(self.ui.yes.geometry())
        # self.ui.yes.setGeometry(300, 300, 300, 200)
        # self.ui.yes.geometry().setX(1)

    #     salary_above_20k = ''
    #     salary_below_20k = ''
    #     for line in info.splitlines():
    #         if not line.strip():
    #             continue
    #         parts = line.split(' ')

    #         parts = [p for p in parts if p]
    #         name,salary,age = parts
    #         if int(salary) >= 20000:
    #             salary_above_20k += name + '\n'
    #         else:
    #             salary_below_20k += name + '\n'

        # QMessageBox.about(self.ui,
        #             '统计结果',
        #             f'''薪资20000 以上的有：\n{salary_above_20k}
        #             \n薪资20000 以下的有：\n{salary_below_20k}'''
        #             )

app = QApplication([])
stats = Stats()
stats.ui.show()
app.exec_()