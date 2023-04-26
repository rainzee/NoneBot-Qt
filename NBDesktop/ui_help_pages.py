# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'help_pages.ui'
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
from PySide6.QtWidgets import (QApplication, QSizePolicy, QTabWidget, QTextBrowser,
    QWidget)

class Ui_help_page(object):
    def setupUi(self, help_page):
        if not help_page.objectName():
            help_page.setObjectName(u"help_page")
        help_page.resize(400, 300)
        self.help_pages = QTabWidget(help_page)
        self.help_pages.setObjectName(u"help_pages")
        self.help_pages.setGeometry(QRect(0, 0, 401, 301))
        self.help_pages.setDocumentMode(True)
        self.welcome = QWidget()
        self.welcome.setObjectName(u"welcome")
        self.text1 = QTextBrowser(self.welcome)
        self.text1.setObjectName(u"text1")
        self.text1.setGeometry(QRect(0, 0, 401, 271))
        self.help_pages.addTab(self.welcome, "")
        self.help_new_project = QWidget()
        self.help_new_project.setObjectName(u"help_new_project")
        self.text2 = QTextBrowser(self.help_new_project)
        self.text2.setObjectName(u"text2")
        self.text2.setGeometry(QRect(0, 0, 401, 271))
        self.help_pages.addTab(self.help_new_project, "")
        self.help_open_project = QWidget()
        self.help_open_project.setObjectName(u"help_open_project")
        self.text3 = QTextBrowser(self.help_open_project)
        self.text3.setObjectName(u"text3")
        self.text3.setGeometry(QRect(0, 0, 411, 271))
        self.help_pages.addTab(self.help_open_project, "")
        self.help_edit_config = QWidget()
        self.help_edit_config.setObjectName(u"help_edit_config")
        self.text4 = QTextBrowser(self.help_edit_config)
        self.text4.setObjectName(u"text4")
        self.text4.setGeometry(QRect(0, 0, 401, 271))
        self.help_pages.addTab(self.help_edit_config, "")

        self.retranslateUi(help_page)

        self.help_pages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(help_page)
    # setupUi

    def retranslateUi(self, help_page):
        help_page.setWindowTitle(QCoreApplication.translate("help_page", u"Form", None))
        self.text1.setHtml(QCoreApplication.translate("help_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#1e1e1e;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:16pt; font-weight:600; text-decoration: underline; color:#55ffff;\">\u6b22\u8fce\u4f7f\u7528 NoneBot Desktop \u5e94\u7528\u7a0b\u5e8f\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#55ffff;\">\u672c\u7a0b\u5e8f\u65e8\u5728\u51cf\u5c11\u4f7f\u7528 NoneBot2 "
                        "\u65f6\u547d\u4ee4\u884c\u7684\u4f7f\u7528\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#55ffff;\">\u8fd9\u91cc\u5305\u542b\u4e86\u672c\u7a0b\u5e8f\u7684\u4e00\u4e9b\u529f\u80fd\u7528\u6cd5\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#55ffff;\">\u8fdb\u5165\u5176\u5b83\u6807\u7b7e\u9875\u67e5\u770b\u66f4\u591a\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#55ffff;\">\u63d0\u793a\uff1a\u65b9\u62ec\u53f7 [] \u5305\u88f9\u7684\u5185\u5bb9\u4e0e\u5b9e\u9645\u754c"
                        "\u9762\u4e2d\u7684\u63a7\u4ef6/\u6587\u672c\u76f8\u5bf9\u5e94\uff1b</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#55ffff;\">\u63d0\u793a\uff1a\u5c16\u62ec\u53f7 &lt;&gt; \u5305\u88f9\u7684\u5185\u5bb9\u8868\u660e\u5176\u4e3a\u5916\u90e8\u5e94\u7528\u7a0b\u5e8f;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#55ffff;\">\u63d0\u793a\uff1a\u53cc\u5de6\u5f15\u53f7 `` \u5305\u88f9\u7684\u5185\u5bb9\u8868\u793a\u4e00\u4e2a\u8def\u5f84\uff08\u7edf\u4e00\u4f7f\u7528 Unix \u683c\u5f0f\uff09\u3002</span></p></body></html>", None))
        self.help_pages.setTabText(self.help_pages.indexOf(self.welcome), QCoreApplication.translate("help_page", u"\u6b22\u8fce", None))
#if QT_CONFIG(tooltip)
        self.help_pages.setTabToolTip(self.help_pages.indexOf(self.welcome), QCoreApplication.translate("help_page", u"\u6b22\u8fce\uff01", None))
#endif // QT_CONFIG(tooltip)
        self.text2.setHtml(QCoreApplication.translate("help_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#1e1e1e;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:16pt; font-weight:600; text-decoration: underline; color:#ffaaff;\">\u672c\u9875\u4ecb\u7ecd\u4e86\u5982\u4f55\u4f7f\u7528\u672c\u7a0b\u5e8f\u521b\u5efa\u65b0\u9879\u76ee\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#ffaaff;\">\u5728\u4e3b\u754c\u9762\u70b9"
                        "\u51fb [\u9879\u76ee]\u83dc\u5355 -&gt; [\u65b0\u5efa\u9879\u76ee] \u8fdb\u5165\u521b\u5efa\u9879\u76ee\u9875\u9762\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#ffaaff;\">\u5728[\u9879\u76ee\u76ee\u5f55]\u4e00\u680f \u901a\u8fc7[\u6d4f\u89c8]\u9009\u62e9\u4e00\u4e2a\u76ee\u5f55 \u6216 \u76f4\u63a5\u5c06\u8def\u5f84\u7c98\u8d34\u81f3[\u8f93\u5165\u6846] \u7528\u4e8e\u521b\u5efa\u9879\u76ee\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#ffaaff;\">\u6ce8\u610f\uff1a\u9879\u76ee\u76ee\u5f55*\u5fc5\u987b*\u662f\u4e00\u4e2a\u7a7a\u76ee\u5f55\uff08\u53ef\u4ee5\u4e0d\u5b58\u5728\uff09\uff0c\u4e14\u907f\u514d\u4f7f\u7528\u4fdd\u7559\u540d\uff08\u5982"
                        "</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">\\u00a0nonebot\\u00a0</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#ffaaff;\">\u7b49\uff09\u4f5c\u4e3a\u9879\u76ee\u76ee\u5f55\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#ffaaff;\">\u5728[\u9a71\u52a8\u5668]\u4e00\u680f\u9009\u62e9\u4f60\u9700\u8981\u7684\u9a71\u52a8\u5668\uff08\u901a\u5e38\u662f [FastAPI]\uff09\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#ffaaff;\"> {DRIVERS_NOTICE}</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0p"
                        "x; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#ffaaff;\">\u9002\u914d\u5668\u7528\u4e8e\u4e0e\u5916\u754c\u8fdb\u884c\u7279\u5b9a\u534f\u8bae\u7684\u6570\u636e\u4ea4\u6362\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#ffaaff;\">\u5728[\u9002\u914d\u5668]\u4e00\u680f\u9009\u62e9\u4f60\u9700\u8981\u7684\u9002\u914d\u5668\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#ffaaff;\"> {ADAPTERS_NOTICE}</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:"
                        "'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#ffaaff;\">\u5982\u679c\u9700\u8981\u4f7f\u7528\u65e0\u6cd5\u4ece\u63d2\u4ef6\u5546\u5e97\u83b7\u53d6\u7684\u63d2\u4ef6\uff08\u5982\u81ea\u7f16\u63d2\u4ef6\u3001\u4ece\u6e90\u7801\u4e0b\u8f7d\u7684\u63d2\u4ef6\u7b49\uff09\uff0c\u8bf7\u52fe\u9009</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#ffaaff;\">[\u9884\u7559\u914d\u7f6e\u7528\u4e8e\u5f00\u53d1\u63d2\u4ef6]\u9009\u9879\uff0c\u7136\u540e\u5c06\u8fd9\u4e9b\u63d2\u4ef6\u6b63\u786e\u653e\u5165 `src/plugins` \u4e0b\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#ffaaff;\">[\u521b\u5efa\u865a\u62df\u73af\u5883]\u53ef\u4ee5\u6709\u6548"
                        "\u907f\u514d\u56e0\u7cfb\u7edf Python \u73af\u5883\u6df7\u4e71\u9020\u6210\u7684\u4e00\u7cfb\u5217\u95ee\u9898\uff0c\u5efa\u8bae\u5f00\u542f\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#ffaaff;\"> {PYPI_INDEX_NOTICE}</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:12pt; color:#ffaaff;\">\u521b\u5efa\u5b8c\u6210\u540e\u4f1a\u81ea\u52a8\u8fdb\u5165\u65b0\u521b\u5efa\u7684\u9879\u76ee\u76ee\u5f55\u3002</span></p></body></html>", None))
        self.help_pages.setTabText(self.help_pages.indexOf(self.help_new_project), QCoreApplication.translate("help_page", u"\u65b0\u5efa\u9879\u76ee", None))
#if QT_CONFIG(tooltip)
        self.help_pages.setTabToolTip(self.help_pages.indexOf(self.help_new_project), QCoreApplication.translate("help_page", u"\u5982\u4f55\u65b0\u5efa\u9879\u76ee\uff1f", None))
#endif // QT_CONFIG(tooltip)
        self.text3.setHtml(QCoreApplication.translate("help_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#1e1e1e;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u672c\u9875\u4ecb\u7ecd\u4e86\u5982\u4f55\u4f7f\u7528\u672c\u7a0b\u5e8f\u6253\u5f00\u5e76\u8fd0\u884c\u5df2\u6709\u7684\u9879\u76ee\u3002</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d7ba7d;\">\\n\\n</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; "
                        "margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u5728\u4e3b\u754c\u9762\u70b9\u51fb [\u9879\u76ee]\u83dc\u5355 -&gt; [\u6253\u5f00\u9879\u76ee] \u9009\u62e9\u4f60\u7684\u9879\u76ee\u76ee\u5f55 \u6216 \u76f4\u63a5\u5c06\u8def\u5f84\u7c98\u8d34\u81f3\u4e3b\u754c\u9762\u7684[\u8f93\u5165\u6846]\u3002</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d7ba7d;\">\\n</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; co"
                        "lor:#d4d4d4;\">        </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u5982\u679c\u9879\u76ee\u76ee\u5f55\u6b63\u786e\uff0c\u4e3b\u754c\u9762\u7684[\u542f\u52a8]\u6309\u94ae\u7b49\u529f\u80fd\u5c06\u5168\u90e8\u53ef\u7528\u3002</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d7ba7d;\">\\n</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u63d0\u793a\uff1a\u672c\u7a0b\u5e8f\u53ea\u652f\u6301\u8bc6\u522b\u6709 `pyproject.toml` \u6216 `bot.py` \u7684\u76ee\u5f55\u4f5c\u4e3a"
                        "\u9879\u76ee\u76ee\u5f55\u3002</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d7ba7d;\">\\n\\n</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u6b63\u786e\u6253\u5f00\u9879\u76ee\u76ee\u5f55\u540e\uff0c\u70b9\u51fb \u4e3b\u754c\u9762\u4e0a\u7684[\u542f\u52a8] \u6216 [\u9879\u76ee]\u83dc\u5355 -&gt; [\u542f\u52a8\u9879\u76ee] \u6765\u8fd0\u884c\u9879\u76ee\u3002</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d7ba7d;\">\\n</span><span style=\" font-family:'Droid Sans Mono','monospace','"
                        "monospace'; font-size:14px; color:#ce9178;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u63d0\u793a\uff1a\u9879\u76ee\u4f1a\u5728\u4e00\u4e2a\u65b0\u7684\u547d\u4ee4\u884c\u7a97\u53e3\u4e2d\u8fd0\u884c\uff0cWindows \u4e0a\u4ec5\u652f\u6301\u4f7f\u7528 &lt;cmd.exe&gt;\uff0cLinux \u4e0a\u4f1a\u81ea\u52a8\u4ece &quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;&lt;gnome-termina"
                        "l&gt;, &lt;konsole&gt;, &lt;xfce4-terminal&gt;, &lt;xterm&gt;, &lt;st&gt; \u4e2d\u67e5\u627e\u53ef\u7528\u7684\u7ec8\u7aef\u6a21\u62df\u5668\u3002</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d7ba7d;\">\\n</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u63d0\u793a\uff1a\u8fd0\u884c\u7ed3\u675f\u540e\u7a97\u53e3\u4e0d\u4f1a\u76f4\u63a5\u5173\u95ed\uff0c\u56e0\u6b64\u4e0d\u5fc5\u62c5\u5fc3\u65e0\u6cd5\u67e5\u770b\u7a0b\u5e8f\u8f93\u51fa\u3002&quot;</span></p></body></html>", None))
        self.help_pages.setTabText(self.help_pages.indexOf(self.help_open_project), QCoreApplication.translate("help_page", u"\u6253\u5f00\u4e0e\u542f\u52a8\u9879\u76ee", None))
#if QT_CONFIG(tooltip)
        self.help_pages.setTabToolTip(self.help_pages.indexOf(self.help_open_project), QCoreApplication.translate("help_page", u"\u5982\u4f55\u6253\u5f00/\u542f\u52a8\u9879\u76ee\uff1f", None))
#endif // QT_CONFIG(tooltip)
        self.text4.setHtml(QCoreApplication.translate("help_page", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Noto Sans'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:19px; background-color:#1e1e1e;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u672c\u9875\u4ecb\u7ecd\u4e86\u5982\u4f55\u4f7f\u7528\u672c\u7a0b\u5e8f\u7f16\u8f91\u9879\u76ee\u7684\u914d\u7f6e\u6587\u4ef6\u3002</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d7ba7d;\">\\n\\n</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin"
                        "-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u6ce8\u610f\uff1a\u672c\u9875\u4e2d\u7684\u914d\u7f6e\u6587\u4ef6\u5747\u6307\u9879\u76ee\u6587\u4ef6\u5939\u4e2d\u7684 DotEnv \u6587\u4ef6\uff08\u6240\u6709\u4ee5 `.env` \u5f00\u5934\u7684\u914d\u7f6e\u6587\u4ef6\uff09\u3002</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d7ba7d;\">\\n</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4;\">        </span><"
                        "span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u6ce8\u610f\uff1a\u90e8\u5206\u63d2\u4ef6\u5e76\u4e0d\u4f7f\u7528\u8fd9\u4e9b\u914d\u7f6e\u6587\u4ef6\uff0c\u5b9e\u9645\u4f7f\u7528\u65f6\u8bf7\u5148\u67e5\u770b\u76f8\u5173\u63d2\u4ef6\u6587\u6863\u3002</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d7ba7d;\">\\n\\n</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u5728\u4e3b\u754c\u9762\u70b9\u51fb [\u914d\u7f6e]\u83dc\u5355 -&gt; [\u914d\u7f6e\u6587\u4ef6\u7f16\u8f91\u5668] \u8fdb"
                        "\u5165\u914d\u7f6e\u6587\u4ef6\u7f16\u8f91\u9875\u9762\u3002</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d7ba7d;\">\\n\\n</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u5728[\u53ef\u7528\u914d\u7f6e\u6587\u4ef6]\u4e00\u680f\u7684[\u4e0b\u62c9\u6846]\u4e2d\u9009\u62e9\u9700\u8981\u7f16\u8f91\u7684\u914d\u7f6e\u6587\u4ef6\uff0c\u9009\u62e9\u540e\u5c06\u81ea\u52a8\u6253\u5f00\u8be5\u6587\u4ef6\u3002</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d7ba7d;\">\\n\\n</span><span style=\""
                        " font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;[\u914d\u7f6e\u9879]\u4e00\u680f\u5217\u51fa\u4e86\u5f53\u524d\u9009\u4e2d\u7684\u914d\u7f6e\u6587\u4ef6\u4e2d\u6240\u6709\u7684\u914d\u7f6e\u9879\uff08\u6ce8\u91ca\u5728\u8bfb\u53d6\u548c\u4fdd\u5b58\u65f6\u4f1a\u88ab\u5ffd\u7565\uff09\u3002</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d7ba7d;\">\\n</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0p"
                        "x; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u6bcf\u4e2a\u914d\u7f6e\u9879\u7b49\u53f7\u5de6\u4fa7\u662f\u8be5\u914d\u7f6e\u9879\u7684\u540d\u79f0\uff08\u4e0d\u533a\u5206\u5927\u5c0f\u5199\uff09\uff0c\u7b49\u53f7\u53f3\u4fa7\u662f\u8be5\u914d\u7f6e\u9879\u7684\u5b57\u9762\u503c\u3002</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d7ba7d;\">\\n</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Droi"
                        "d Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u5982\u679c\u8981\u6dfb\u52a0\u4e00\u4e2a\u65b0\u7684\u914d\u7f6e\u9879\uff0c\u70b9\u51fb\u4e0b\u65b9\u7684[\u65b0\u5efa\u914d\u7f6e\u9879]\u6309\u94ae\uff0c\u7136\u540e\u81ea\u884c\u586b\u5199\u65b0\u914d\u7f6e\u9879\u7684\u540d\u79f0\u548c\u503c\u5373\u53ef\u3002</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d7ba7d;\">\\n</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u672c\u7a0b\u5e8f\u5728\u4fdd\u5b58\u65f6\u4f1a\u81ea\u52a8\u79fb\u9664\u7a7a\u7684\u914d"
                        "\u7f6e\u9879\uff0c\u56e0\u6b64\u5982\u679c\u8981\u5220\u9664\u67d0\u4e2a\u914d\u7f6e\u9879\uff0c\u53ea\u9700\u8981\u5c06\u5176\u540d\u79f0\u6216\u5b57\u9762\u503c\u6e05\u7a7a\u5373\u53ef\u3002</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d7ba7d;\">\\n</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u7f16\u8f91\u5b8c\u6210\u540e\uff0c\u70b9\u51fb[\u4fdd\u5b58]\u6309\u94ae\u5c06\u65b0\u7684\u914d\u7f6e\u5199\u5165\u6587\u4ef6\u3002</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d7ba7d"
                        ";\">\\n</span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4;\">        </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u6ce8\u610f\uff1a\u53ea\u6709\u5728\u70b9\u51fb[\u4fdd\u5b58]\u6309\u94ae\u65f6\u66f4\u6539\u624d\u4f1a\u88ab\u5199\u5165\u5230\u6587\u4ef6\uff0c\u76f4\u63a5\u5173\u95ed\u7a97\u53e3\u6216\u5207\u6362\u81f3\u5176\u4ed6\u914d\u7f6e\u6587\u4ef6\u5747\u4f1a\u4e22\u5931\u5f53\u524d\u66f4\u6539\uff0c&quot;</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#d4d4d4"
                        ";\">        </span><span style=\" font-family:'Droid Sans Mono','monospace','monospace'; font-size:14px; color:#ce9178;\">&quot;\u672c\u7a0b\u5e8f*\u4e0d\u4f1a*\u8bd5\u56fe\u901a\u8fc7\u4efb\u4f55\u63d0\u793a\u963b\u6b62\u8fd9\u79cd\u884c\u4e3a\u3002&quot;</span></p></body></html>", None))
        self.help_pages.setTabText(self.help_pages.indexOf(self.help_edit_config), QCoreApplication.translate("help_page", u"\u7f16\u8f91\u914d\u7f6e\u6587\u4ef6", None))
#if QT_CONFIG(tooltip)
        self.help_pages.setTabToolTip(self.help_pages.indexOf(self.help_edit_config), QCoreApplication.translate("help_page", u"\u5982\u4f55\u7f16\u8f91\u914d\u7f6e\u6587\u4ef6\uff1f", None))
#endif // QT_CONFIG(tooltip)
    # retranslateUi

