from datetime import datetime

from PySide6.QtGui import QFont, QAction
from PySide6.QtCore import QSize, QCoreApplication
from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QTextEdit,
    QMenu,
    QMenuBar,
)


class Log_Widgets(QTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)

    def _log(self, text: str, color: str = "black") -> None:
        self.append(
            f"{datetime.now().strftime('%H:%M:%S')} - <font color={color}>{text}</font>"
        )

    def log(self, text: str):
        self._log(text)

    def success(self, text: str) -> None:
        self._log(text, "green")

    def error(self, text: str) -> None:
        self._log(text, "brown")

    def warning(self, text: str) -> None:
        self._log(text, "orange")

    def code(self, text: str) -> None:
        self._log(text, "red")


class UI:
    def init_UI(self, MainWindow):
        # MainWindow Size
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(320, 420)
        MainWindow.setMinimumSize(QSize(420, 520))
        MainWindow.setMaximumSize(QSize(720, 820))

        # MainWindow Font
        font = QFont()
        font.setPointSize(9)
        font.setFamily("Microsoft YaHei")
        font.setStyleStrategy(QFont.PreferAntialias)  # type: ignore
        MainWindow.setFont(font)

        # Layout Init
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        # Widgets Init
        self.text_log = Log_Widgets(self.centralwidget)
        self.text_log.setObjectName("text_log")

        # Widgets Setup
        self.verticalLayout.addWidget(self.text_log)

        MainWindow.setCentralWidget(self.centralwidget)

        # Menu Bar Init
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")

        # Menu Bar Init
        self.menu_project = QMenu(self.menubar)
        self.menu_project.setObjectName("menu_project")

        self.menu_config = QMenu(self.menubar)
        self.menu_config.setObjectName("menu_config")

        self.menu_plugins = QMenu(self.menubar)
        self.menu_plugins.setObjectName("menu_plugins")

        self.menu_menu = QMenu(self.menubar)
        self.menu_menu.setObjectName("menu_menu")

        self.menu_help = QMenu(self.menubar)
        self.menu_help.setObjectName("menu_help")

        # Menu Actions Init
        self.action_about = QAction(MainWindow)
        self.action_about.setObjectName("action_about")

        self.action_about_qt = QAction(MainWindow)
        self.action_about_qt.setObjectName("action_about_qt")

        # Menu Bar Setup
        MainWindow.setMenuBar(self.menubar)

        # Menu setup
        self.menubar.addMenu(self.menu_project)
        self.menubar.addMenu(self.menu_config)
        self.menubar.addMenu(self.menu_plugins)
        self.menubar.addMenu(self.menu_menu)
        self.menubar.addMenu(self.menu_help)

        # Menu Actions setup
        self.menu_help.addAction(self.action_about)
        self.menu_help.addAction(self.action_about_qt)

        self.retranslateUi(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "NoneBot Qt"))

        self.menu_project.setTitle(_translate("MainWindow", self.tr("项目")))
        self.menu_config.setTitle(_translate("MainWindow", self.tr("配置")))
        self.menu_plugins.setTitle(_translate("MainWindow", self.tr("插件")))
        self.menu_menu.setTitle(_translate("MainWindow", self.tr("高级")))
        self.menu_help.setTitle(_translate("MainWindow", self.tr("帮助")))

        self.action_about.setText(_translate("MainWindow", self.tr("关于")))
        self.action_about_qt.setText(_translate("MainWindow", self.tr("关于Qt")))
