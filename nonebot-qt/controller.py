# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QMainWindow,QWidget
import time
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui import UI
from create_project import Ui_NewProject as CP
from terminal_page import Ui_terminal_page as TP
from help_pages import Ui_help_page as HP
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = UI()
        self.ui.setupUi(self)
        
        self.hp = HP()
        self.hp.setupUi(self.hp)
        self.cp = CP()
        self.cp.setupUi(self.cp)
        self.tp = TP()
        self.tp.setupUi(self.tp)
        
        self.ui.pages.addWidget(self.hp)
        self.ui.pages.addWidget(self.tp)
        self.ui.pages.addWidget(self.cp)
        '''
        self.tp.output("test!!!\n")
        self.tp.output("test2!!!\n")
        '''
        '''
        print(self.ui.pages.currentIndex())
        self.ui.pages.setCurrentIndex(1)
        print(self.ui.pages.currentIndex())
        '''
        
       # TODO: Initialize Objects
        # TODO: Initialize Client Information
        # TODO: Initialize default state
        # TODO: Initialize default Assets
        # TODO: Initialize Thread
        # TODO: Initialize Worker
        # TODO: Initalize Widgets Slots Connection
        # TODO: Initalize Threads Slots Connection
        # TODO: Initalize Bootup Checking

        #time_end = time.perf_counter()
        #print(f"系统初始化耗时{((time_end - time_start) * 1000):.1f}毫秒")
        #self.text_log.log(f"系统初始化耗时{((time_end - time_start) * 1000):.1f}毫秒")

        #set singal and slot
        self.ui.help_us.triggered.connect(lambda:self.set_pages_index(0))
        self.ui.senior_terminal.triggered.connect(lambda:self.set_pages_index(1))
        self.ui.new_project.triggered.connect(lambda:self.set_pages_index(2))
        


    def set_pages_index(self,page_num : int) :
        self.ui.pages.setCurrentIndex(page_num)


