# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'create_project.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QListWidget,
    QListWidgetItem, QPlainTextEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_NewProject(QWidget):
    def setupUi(self, NewProject):
        if not NewProject.objectName():
            NewProject.setObjectName(u"NewProject")
        #NewProject.resize(600, 600)
        #NewProject.setMinimumSize(QSize(600, 600))
        #NewProject.setMaximumSize(QSize(600, 600))
        self.adapter_list = QListWidget(NewProject)
        self.adapter_list.setObjectName(u"adapter_list")
        self.adapter_list.setGeometry(QRect(10, 30, 281, 481))
        self.drivertext = QLabel(NewProject)
        self.drivertext.setObjectName(u"drivertext")
        self.drivertext.setGeometry(QRect(90, 10, 71, 16))
        self.listWidget_2 = QListWidget(NewProject)
        self.listWidget_2.setObjectName(u"listWidget_2")
        self.listWidget_2.setGeometry(QRect(300, 30, 281, 481))
        self.adaptertext = QLabel(NewProject)
        self.adaptertext.setObjectName(u"adaptertext")
        self.adaptertext.setGeometry(QRect(420, 10, 71, 16))
        self.venv = QCheckBox(NewProject)
        self.venv.setObjectName(u"venv")
        self.venv.setGeometry(QRect(10, 530, 111, 21))
        self.dev = QCheckBox(NewProject)
        self.dev.setObjectName(u"dev")
        self.dev.setGeometry(QRect(10, 570, 101, 21))
        self.projects_entry = QPlainTextEdit(NewProject)
        self.projects_entry.setObjectName(u"projects_entry")
        self.projects_entry.setGeometry(QRect(230, 520, 191, 31))
        self.projectdir = QLabel(NewProject)
        self.projectdir.setObjectName(u"projectdir")
        self.projectdir.setGeometry(QRect(170, 520, 61, 31))
        self.sources = QLabel(NewProject)
        self.sources.setObjectName(u"sources")
        self.sources.setGeometry(QRect(170, 570, 58, 18))
        self.sources_entry = QPlainTextEdit(NewProject)
        self.sources_entry.setObjectName(u"sources_entry")
        self.sources_entry.setGeometry(QRect(230, 560, 191, 31))
        self.project_ok = QPushButton(NewProject)
        self.project_ok.setObjectName(u"project_ok")
        self.project_ok.setGeometry(QRect(460, 520, 121, 71))
        QWidget.setTabOrder(self.adapter_list, self.projects_entry)
        QWidget.setTabOrder(self.projects_entry, self.sources_entry)
        QWidget.setTabOrder(self.sources_entry, self.project_ok)
        QWidget.setTabOrder(self.project_ok, self.dev)
        QWidget.setTabOrder(self.dev, self.venv)
        QWidget.setTabOrder(self.venv, self.listWidget_2)

        self.retranslateUi(NewProject)

        
    # setupUi

    def retranslateUi(self, NewProject):
        NewProject.setWindowTitle(QCoreApplication.translate("NewProject", u"Form", None))
        self.drivertext.setText(QCoreApplication.translate("NewProject", u"\u9009\u62e9\u9a71\u52a8\u5668", None))
        self.adaptertext.setText(QCoreApplication.translate("NewProject", u"\u9009\u62e9\u9002\u914d\u5668", None))
        self.venv.setText(QCoreApplication.translate("NewProject", u"\u521b\u5efa\u865a\u62df\u73af\u5883", None))
        self.dev.setText(QCoreApplication.translate("NewProject", u"\u9884\u7559\u5f00\u53d1\u914d\u7f6e", None))
        self.projectdir.setText(QCoreApplication.translate("NewProject", u"\u9879\u76ee\u76ee\u5f55", None))
        self.sources.setText(QCoreApplication.translate("NewProject", u"\u4e0b\u8f7d\u6e90", None))
        self.project_ok.setText(QCoreApplication.translate("NewProject", u"\u521b\u5efa\u9879\u76ee", None))
    # retranslateUi

    

