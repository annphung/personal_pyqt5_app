import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import QPropertyAnimation

# Adding path to the ui-folder in order to import the pyuic generated files
sys.path.append("./ui/")

from interface  import Ui_side_menu_interface
from timerthread import timerWidget
from todoList_interface import ToDoList


class SideMenu(QMainWindow, Ui_side_menu_interface):

    def __init__(self):
        super().__init__()
        self.window = Ui_side_menu_interface()
        self.window.setupUi(self)
        style = "stylesheets/main_stylesheet.css"
        with open(style, "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())

        # Handling different widgets in the stack
        self.timer = timerWidget()                                                            # New instance of the TimerThread
        self.window.main_body_stackedWidget.insertWidget(1, self.timer)
        self.todolist = ToDoList()
        self.window.main_body_stackedWidget.insertWidget(2, self.todolist)
        
        # Buttons and design components of main window
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)                                    # Hides the upper window frame 
        self.window.exit_button.clicked.connect(lambda: self.close())                         # Adds method to close button 
        self.window.exit_button_2.clicked.connect(lambda: self.close())                       # Adds method to close button 
        self.window.maximize_button.clicked.connect(self.size_change)
        self.window.minimize_button.clicked.connect(lambda: self.showMinimized())
        self.window.header.mouseMoveEvent = self.moveWindow
        self.window.left_align_Button.clicked.connect(self.toggle_sidebar)

        # Button for choosing widget
        self.window.user_button.clicked.connect(lambda: self.window.main_body_stackedWidget.setCurrentIndex(0))
        self.window.bell_button.clicked.connect(lambda: self.window.main_body_stackedWidget.setCurrentIndex(1))
        self.window.ToDo_list_button.clicked.connect(lambda: self.window.main_body_stackedWidget.setCurrentIndex(2))


    def toggle_sidebar(self):
        width = self.window.side_menu_container.width()
        if width == 0:
            newWidth = 200
            self.window.left_align_Button.setIcon(QtGui.QIcon(":/icons/icons/chevron-left.svg"))
        else: 
            newWidth = 0
            self.window.left_align_Button.setIcon(QtGui.QIcon(":/icons/icons/align-left.svg"))
    
        # Creatting the animation of opening and closing the side meny.
        self.animation = QPropertyAnimation(self.window.side_menu_container, b"maximumWidth")
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setDuration(150)
        self.animation.start()
            
    # Method for changing maximizing/minimizing the app 
    def size_change(self):
        if self.isMaximized():
            self.showNormal()                                                                 # Back to small size if maximized   
            self.window.maximize_button.setIcon(QtGui.QIcon(":/icons/icons/maximize-2.svg"))  # Change icon 
        else:
            self.showMaximized()                                                              # Maximize if window is small
            self.window.maximize_button.setIcon(QtGui.QIcon(":/icons/icons/minimize-2.svg"))


    # Method for moving the window. Uses the mousePressEvent() method
    def moveWindow(self, event):
        if self.isMaximized() == False:
            if event.buttons() == QtCore.Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.clickPosition)                # Using value from mousePressEvent()
                self.clickPosition = event.globalPos()
                event.accept()

    # Overriding method. Using this to get the current position of the mouse
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sidemenu = SideMenu()
    sidemenu.show()
    sys.exit(app.exec_())