# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStackedWidget, QStatusBar, QWidget)

class UI(object):
    def setupUi(self, Root):
        if not Root.objectName():
            Root.setObjectName(u"Root")
        Root.resize(606, 620)
        self.help_us = QAction(Root)
        self.help_us.setObjectName(u"help_us")
        self.help_qt6 = QAction(Root)
        self.help_qt6.setObjectName(u"help_qt6")
        self.new_project = QAction(Root)
        self.new_project.setObjectName(u"new_project")
        self.open_project = QAction(Root)
        self.open_project.setObjectName(u"open_project")
        self.get_project = QAction(Root)
        self.get_project.setObjectName(u"get_project")
        self.config_bot = QAction(Root)
        self.config_bot.setObjectName(u"config_bot")
        self.run_project = QAction(Root)
        self.run_project.setObjectName(u"run_project")
        self.open_dir = QAction(Root)
        self.open_dir.setObjectName(u"open_dir")
        self.config_driver = QAction(Root)
        self.config_driver.setObjectName(u"config_driver")
        self.download_plugin = QAction(Root)
        self.download_plugin.setObjectName(u"download_plugin")
        self.list_plugin = QAction(Root)
        self.list_plugin.setObjectName(u"list_plugin")
        self.upgrade_plugin = QAction(Root)
        self.upgrade_plugin.setObjectName(u"upgrade_plugin")
        self.rm_plugin = QAction(Root)
        self.rm_plugin.setObjectName(u"rm_plugin")
        self.config_adapter = QAction(Root)
        self.config_adapter.setObjectName(u"config_adapter")
        self.config_env = QAction(Root)
        self.config_env.setObjectName(u"config_env")
        self.senior_terminal = QAction(Root)
        self.senior_terminal.setObjectName(u"senior_terminal")
        self.centralwidget = QWidget(Root)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        self.pages.setGeometry(QRect(0, 0, 600, 600))
        self.pages.setMinimumSize(QSize(600, 600))
        self.pages.setMaximumSize(QSize(600, 600))
        '''
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setEnabled(False)
        self.pages.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.pages.addWidget(self.page_2)
        '''
        Root.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Root)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 606, 32))
        self.project = QMenu(self.menubar)
        self.project.setObjectName(u"project")
        self.config = QMenu(self.menubar)
        self.config.setObjectName(u"config")
        self.plugin = QMenu(self.menubar)
        self.plugin.setObjectName(u"plugin")
        self.senior = QMenu(self.menubar)
        self.senior.setObjectName(u"senior")
        self.help = QMenu(self.menubar)
        self.help.setObjectName(u"help")
        self.exit = QMenu(self.menubar)
        self.exit.setObjectName(u"exit")
        Root.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Root)
        self.statusbar.setObjectName(u"statusbar")
        Root.setStatusBar(self.statusbar)

        self.menubar.addAction(self.project.menuAction())
        self.menubar.addAction(self.config.menuAction())
        self.menubar.addAction(self.plugin.menuAction())
        self.menubar.addAction(self.senior.menuAction())
        self.menubar.addAction(self.help.menuAction())
        self.menubar.addAction(self.exit.menuAction())
        self.project.addAction(self.new_project)
        self.project.addAction(self.open_project)
        self.project.addAction(self.get_project)
        self.project.addSeparator()
        self.project.addAction(self.run_project)
        self.project.addSeparator()
        self.project.addAction(self.open_dir)
        self.config.addAction(self.config_bot)
        self.config.addSeparator()
        self.config.addAction(self.config_driver)
        self.config.addAction(self.config_adapter)
        self.config.addSeparator()
        self.config.addAction(self.config_env)
        self.plugin.addAction(self.download_plugin)
        self.plugin.addAction(self.list_plugin)
        self.plugin.addAction(self.upgrade_plugin)
        self.plugin.addSeparator()
        self.plugin.addAction(self.rm_plugin)
        self.senior.addAction(self.senior_terminal)
        self.help.addAction(self.help_us)
        self.help.addAction(self.help_qt6)

        self.retranslateUi(Root)

        self.pages.setCurrentIndex(0)
    




    # setupUi

    def retranslateUi(self, Root):
        Root.setWindowTitle(QCoreApplication.translate("Root", u"NoneBot QDesktop", None))
        self.help_us.setText(QCoreApplication.translate("Root", u"\u5173\u4e8e", None))
        self.help_qt6.setText(QCoreApplication.translate("Root", u"\u5173\u4e8eQt6", None))
        self.new_project.setText(QCoreApplication.translate("Root", u"\u65b0\u5efa", None))
        self.open_project.setText(QCoreApplication.translate("Root", u"\u6253\u5f00", None))
        self.get_project.setText(QCoreApplication.translate("Root", u"\u83b7\u53d6", None))
        self.config_bot.setText(QCoreApplication.translate("Root", u"\u9879\u76ee\u914d\u7f6e", None))
        self.run_project.setText(QCoreApplication.translate("Root", u"\u8fd0\u884c", None))
        self.open_dir.setText(QCoreApplication.translate("Root", u"\u6253\u5f00\u9879\u76ee\u6587\u4ef6\u5939", None))
        self.config_driver.setText(QCoreApplication.translate("Root", u"\u7ba1\u7406\u9a71\u52a8\u5668", None))
        self.download_plugin.setText(QCoreApplication.translate("Root", u"\u4e0b\u8f7d", None))
        self.list_plugin.setText(QCoreApplication.translate("Root", u"\u5217\u8868", None))
        self.upgrade_plugin.setText(QCoreApplication.translate("Root", u"\u66f4\u65b0", None))
        self.rm_plugin.setText(QCoreApplication.translate("Root", u"\u79fb\u9664", None))
        self.config_adapter.setText(QCoreApplication.translate("Root", u"\u7ba1\u7406\u9002\u914d\u5668", None))
        self.config_env.setText(QCoreApplication.translate("Root", u"\u7ba1\u7406\u73af\u5883", None))
        self.senior_terminal.setText(QCoreApplication.translate("Root", u"\u7ec8\u7aef", None))
        self.project.setTitle(QCoreApplication.translate("Root", u"\u9879\u76ee", None))
        self.config.setTitle(QCoreApplication.translate("Root", u"\u914d\u7f6e", None))
        self.plugin.setTitle(QCoreApplication.translate("Root", u"\u63d2\u4ef6", None))
        self.senior.setTitle(QCoreApplication.translate("Root", u"\u9ad8\u7ea7", None))
        self.help.setTitle(QCoreApplication.translate("Root", u"\u5e2e\u52a9", None))
        self.exit.setTitle(QCoreApplication.translate("Root", u"\u9000\u51fa", None))
    # retranslateUi

  
