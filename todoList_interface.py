from datetime import date
from PyQt5.QtWidgets import QWidget, QListWidgetItem
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui

from todolist import Ui_To_Do_List_widget
from custom_list_item import Ui_custom_list_item

class ToDoList(QWidget, Ui_To_Do_List_widget):
    check = pyqtSignal()
    uncheck = pyqtSignal()
    all_elements = list()
    completed_tasks = list()

    def __init__(self):
        super().__init__()
        self.widget = Ui_To_Do_List_widget()
        self.widget.setupUi(self)
        style = "stylesheets/todo_list_stylesheet.css"
        with open(style, "r") as stylesheet:
            self.setStyleSheet(stylesheet.read())
        self.list_count = 0
        
        self.date = date.today()
        self.date_formatted = self.date.strftime("%d. %B %Y")
        self.widget.date_label.setText(self.date_formatted)

        self.widget.add_task_must.setPlaceholderText("Add new task")
        self.widget.add_task_should.setPlaceholderText("Add new task")
        self.widget.add_task_nice.setPlaceholderText("Add new task")

        self.widget.add_button_nice.clicked.connect(self.add_new_item)
        self.widget.add_button_should.clicked.connect(self.add_new_item)
        self.widget.add_button_must.clicked.connect(self.add_new_item)
        self.widget.add_task_nice.returnPressed.connect(lambda: self.widget.add_button_nice.clicked.emit())
        self.widget.add_task_should.returnPressed.connect(lambda: self.widget.add_button_should.clicked.emit())
        self.widget.add_task_must.returnPressed.connect(lambda: self.widget.add_button_must.clicked.emit())

        self.widget.clear_all_button.clicked.connect(self.clear_all)
        self.widget.clear_completed_button.clicked.connect(self.clear_completed)
        
    def delete_item(self, *parent):
        selected = None 
        if parent[0] == False:                            # Hvis vi ikke sender inn parent selv, må den bruke sender 
            pointer_to_parent = self.sender().parent()
        else: 
            pointer_to_parent = parent[0].parent     # QListWidgetItem
        for item in self.all_elements:
            if item.parent == pointer_to_parent:
                selected = item.sender
                if item.category == "nice":
                    row = self.widget.nice_to_do_list.row(selected)
                    self.widget.nice_to_do_list.takeItem(row)
                elif item.category == "should":
                    row = self.widget.should_do_list.row(selected)
                    self.widget.should_do_list.takeItem(row)
                elif item.category == "must":
                    row = self.widget.must_do_list.row(selected)
                    self.widget.must_do_list.takeItem(row)
        

    def add_new_item(self):
        objectName = self.sender().objectName()
        self.list_item = QListWidgetItem()
        category = None
        match objectName:
            case "add_button_nice":
                category = "nice"
                self.item = Custom_list_item(self.widget.add_task_nice.text())
                self.widget.nice_to_do_list.addItem(self.list_item)
                self.widget.nice_to_do_list.setItemWidget(self.list_item, self.item)
                self.widget.add_task_nice.clear()
            case "add_button_should":
                category = "should"
                self.item = Custom_list_item(self.widget.add_task_should.text())
                self.widget.should_do_list.addItem(self.list_item)
                self.widget.should_do_list.setItemWidget(self.list_item, self.item)
                self.widget.add_task_should.clear()
            case "add_button_must":
                category = "must"
                self.item = Custom_list_item(self.widget.add_task_must.text())
                self.widget.must_do_list.addItem(self.list_item)
                self.widget.must_do_list.setItemWidget(self.list_item, self.item)
                self.widget.add_task_must.clear()
        self.item.trash_button.clicked.connect(self.delete_item)
        self.item.check_button.clicked.connect(self.toggle_check)
        self.all_elements.append(self.List_element(self.list_item, self.item, category))

    def clear_completed(self):
        for tasks in self.all_elements:
            for completed in self.completed_tasks:
                if tasks.parent == completed.parent:
                    self.delete_item(completed)

    def clear_all(self):
        self.widget.nice_to_do_list.clear()
        self.widget.should_do_list.clear()
        self.widget.must_do_list.clear()

    def toggle_check(self):
        pointer_to_sender = self.sender().parent()
        # Add tasks to completed list
        if self.sender().isChecked():
            for item in self.all_elements:
                if item.parent == pointer_to_sender:
                    self.completed_tasks.append(item)
        # Remove tasks to completed list
        elif self.sender().isChecked() == False:
            for item in self.completed_tasks:
                if item.parent == pointer_to_sender:
                    self.completed_tasks.remove(item)
                    print("removed item")


    # Inner class for saving item-components 
    class List_element:
        def __init__(self,sender, parent, category):
            self.sender = sender 
            self.parent = parent 
            self.category = category


class Custom_list_item(QWidget, Ui_custom_list_item):
    def __init__(self, text):
         super().__init__()
         self.setupUi(self)
        
         self.text = text
         self.task_field.setText(text)
         self.check_button.clicked.connect(self.checkbox_tick)

    def setItemText(self, text):
        self.task_field.setText(text)

    def checkbox_tick(self):
        font = QtGui.QFont()
        if self.check_button.isChecked():
            self.check_button.setIcon(QtGui.QIcon(":/icons/icons/checked.svg"))
            font.setStrikeOut(True)
            self.task_field.setFont(font)
        else:
            self.check_button.setIcon(QtGui.QIcon(":/icons/icons/unchecked.svg"))
            font.setStrikeOut(False)
            self.task_field.setFont(font)

        



