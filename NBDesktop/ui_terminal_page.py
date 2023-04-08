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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTextBrowser, QWidget)

class Ui_terminal_page(object):
    def setupUi(self, terminal_page):
        if not terminal_page.objectName():
            terminal_page.setObjectName(u"terminal_page")
        terminal_page.resize(400, 300)
        self.terminal = QTextBrowser(terminal_page)
        self.terminal.setObjectName(u"terminal")
        self.terminal.setGeometry(QRect(0, 0, 401, 301))

        self.retranslateUi(terminal_page)

        QMetaObject.connectSlotsByName(terminal_page)
    # setupUi

    def retranslateUi(self, terminal_page):
        terminal_page.setWindowTitle(QCoreApplication.translate("terminal_page", u"Form", None))
    # retranslateUi

