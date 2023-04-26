# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'terminal_page.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
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
from PySide6.QtWidgets import (QApplication, QLineEdit, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_terminal_page(object):
    def setupUi(self, terminal_page):
        if not terminal_page.objectName():
            terminal_page.setObjectName(u"terminal_page")
        terminal_page.resize(400, 300)
        self.terminal = QTextBrowser(terminal_page)
        self.terminal.setObjectName(u"terminal")
        self.terminal.setGeometry(QRect(0, 0, 401, 261))
        self.pushButton = QPushButton(terminal_page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 270, 80, 25))
        self.pushButton_2 = QPushButton(terminal_page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 270, 80, 25))
        self.pushButton_3 = QPushButton(terminal_page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(310, 270, 80, 25))
        self.lineEdit = QLineEdit(terminal_page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(190, 270, 101, 25))

        self.retranslateUi(terminal_page)

        QMetaObject.connectSlotsByName(terminal_page)
    # setupUi

    def retranslateUi(self, terminal_page):
        terminal_page.setWindowTitle(QCoreApplication.translate("terminal_page", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("terminal_page", u"\u6e05\u9664\u8bb0\u5f55", None))
        self.pushButton_2.setText(QCoreApplication.translate("terminal_page", u"\u505c\u6b62\u8fd0\u884c", None))
        self.pushButton_3.setText(QCoreApplication.translate("terminal_page", u"\u53d1\u9001", None))
    # retranslateUi

