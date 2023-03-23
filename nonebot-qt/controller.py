import time

from PySide6.QtWidgets import QMainWindow

from ui import UI

class MainWindow(QMainWindow, UI):
    def __init__(self, parent=None):  # type: ignore
        super().__init__(parent)  # type: ignore
        time_start = time.perf_counter()

        # Initialize Main UI
        self.init_UI(self)
        # TODO: Initialize Objects
        # TODO: Initialize Client Information
        # TODO: Initialize default state
        # TODO: Initialize default Assets
        # TODO: Initialize Thread
        # TODO: Initialize Worker
        # TODO: Initalize Widgets Slots Connection
        # TODO: Initalize Threads Slots Connection
        # TODO: Initalize Bootup Checking

        time_end = time.perf_counter()
        print(f"系统初始化耗时{((time_end - time_start) * 1000):.1f}毫秒")
        self.text_log.log(f"系统初始化耗时{((time_end - time_start) * 1000):.1f}毫秒")