# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.5.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QListView, QMainWindow,
    QPushButton, QSizePolicy, QWidget)
import picture_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(400, 200)
        MainWindow.setMaximumSize(QSize(400, 200))
        icon = QIcon()
        icon.addFile(u":/pic/Christmas Star.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.yes = QPushButton(self.centralwidget)
        self.yes.setObjectName(u"yes")
        self.yes.setGeometry(QRect(30, 80, 75, 23))
        self.listView = QListView(self.centralwidget)
        self.listView.setObjectName(u"listView")
        self.listView.setGeometry(QRect(0, 0, 400, 200))
        self.listView.setMaximumSize(QSize(400, 200))
        self.listView.setStyleSheet(u"border-image: url(:/pic/Snipaste_2020-12-01_17-49-55.png);")
        self.no = QPushButton(self.centralwidget)
        self.no.setObjectName(u"no")
        self.no.setGeometry(QRect(280, 20, 75, 23))
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 141, 71))
        font = QFont()
        font.setFamilies([u"\u4eff\u5b8b"])
        font.setPointSize(20)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setCursor(QCursor(Qt.PointingHandCursor))
        self.label.setMouseTracking(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.listView.raise_()
        self.label.raise_()
        self.no.raise_()
        self.yes.raise_()

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u563f\u563f", None))
        self.yes.setText(QCoreApplication.translate("MainWindow", u"yes", None))
        self.no.setText(QCoreApplication.translate("MainWindow", u"no", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u4f60\u662f\u732a\u5417?", None))
    # retranslateUi

