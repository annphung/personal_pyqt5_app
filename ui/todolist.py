# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/todolist.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_To_Do_List_widget(object):
    def setupUi(self, To_Do_List_widget):
        To_Do_List_widget.setObjectName("To_Do_List_widget")
        To_Do_List_widget.resize(945, 677)
        self.verticalLayout = QtWidgets.QVBoxLayout(To_Do_List_widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.outer_frame = QtWidgets.QFrame(To_Do_List_widget)
        self.outer_frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.outer_frame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.outer_frame.setObjectName("outer_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.outer_frame)
        self.verticalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.inner_frame = QtWidgets.QFrame(self.outer_frame)
        self.inner_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.inner_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.inner_frame.setObjectName("inner_frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.inner_frame)
        self.verticalLayout_3.setContentsMargins(20, 20, 20, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.header_layout = QtWidgets.QVBoxLayout()
        self.header_layout.setObjectName("header_layout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.clear_completed_button = QtWidgets.QPushButton(self.inner_frame)
        self.clear_completed_button.setObjectName("clear_completed_button")
        self.horizontalLayout_2.addWidget(self.clear_completed_button)
        self.title = QtWidgets.QLabel(self.inner_frame)
        font = QtGui.QFont()
        font.setPointSize(23)
        self.title.setFont(font)
        self.title.setScaledContents(True)
        self.title.setObjectName("title")
        self.horizontalLayout_2.addWidget(self.title, 0, QtCore.Qt.AlignHCenter)
        self.clear_all_button = QtWidgets.QPushButton(self.inner_frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.clear_all_button.setFont(font)
        self.clear_all_button.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.clear_all_button.setObjectName("clear_all_button")
        self.horizontalLayout_2.addWidget(self.clear_all_button)
        self.header_layout.addLayout(self.horizontalLayout_2)
        self.date_label = QtWidgets.QLabel(self.inner_frame)
        font = QtGui.QFont()
        font.setPointSize(8)
        self.date_label.setFont(font)
        self.date_label.setObjectName("date_label")
        self.header_layout.addWidget(self.date_label, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout_3.addLayout(self.header_layout)
        self.task_list_layout = QtWidgets.QHBoxLayout()
        self.task_list_layout.setObjectName("task_list_layout")
        self.nice_to_do_layout = QtWidgets.QVBoxLayout()
        self.nice_to_do_layout.setSpacing(0)
        self.nice_to_do_layout.setObjectName("nice_to_do_layout")
        self.nice_to_label = QtWidgets.QLabel(self.inner_frame)
        self.nice_to_label.setAlignment(QtCore.Qt.AlignCenter)
        self.nice_to_label.setObjectName("nice_to_label")
        self.nice_to_do_layout.addWidget(self.nice_to_label)
        self.nice_to_do_list = QtWidgets.QListWidget(self.inner_frame)
        self.nice_to_do_list.setBaseSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.nice_to_do_list.setFont(font)
        self.nice_to_do_list.setFocusPolicy(QtCore.Qt.NoFocus)
        self.nice_to_do_list.setLineWidth(50)
        self.nice_to_do_list.setProperty("showDropIndicator", False)
        self.nice_to_do_list.setDragEnabled(True)
        self.nice_to_do_list.setDragDropMode(QtWidgets.QAbstractItemView.DragDrop)
        self.nice_to_do_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.nice_to_do_list.setObjectName("nice_to_do_list")
        self.nice_to_do_layout.addWidget(self.nice_to_do_list)
        self.enter_task_frame_nice = QtWidgets.QFrame(self.inner_frame)
        self.enter_task_frame_nice.setObjectName("enter_task_frame_nice")
        self.enter_task_layout_nice = QtWidgets.QHBoxLayout(self.enter_task_frame_nice)
        self.enter_task_layout_nice.setContentsMargins(0, 0, 0, 0)
        self.enter_task_layout_nice.setSpacing(0)
        self.enter_task_layout_nice.setObjectName("enter_task_layout_nice")
        self.add_task_nice = QtWidgets.QLineEdit(self.enter_task_frame_nice)
        self.add_task_nice.setMinimumSize(QtCore.QSize(0, 30))
        self.add_task_nice.setObjectName("add_task_nice")
        self.enter_task_layout_nice.addWidget(self.add_task_nice)
        self.add_button_nice = QtWidgets.QPushButton(self.enter_task_frame_nice)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button_nice.sizePolicy().hasHeightForWidth())
        self.add_button_nice.setSizePolicy(sizePolicy)
        self.add_button_nice.setMinimumSize(QtCore.QSize(25, 25))
        self.add_button_nice.setMaximumSize(QtCore.QSize(25, 25))
        self.add_button_nice.setObjectName("add_button_nice")
        self.enter_task_layout_nice.addWidget(self.add_button_nice)
        self.nice_to_do_layout.addWidget(self.enter_task_frame_nice)
        self.task_list_layout.addLayout(self.nice_to_do_layout)
        self.should_do_layout = QtWidgets.QVBoxLayout()
        self.should_do_layout.setSpacing(0)
        self.should_do_layout.setObjectName("should_do_layout")
        self.should_do_label = QtWidgets.QLabel(self.inner_frame)
        self.should_do_label.setAlignment(QtCore.Qt.AlignCenter)
        self.should_do_label.setObjectName("should_do_label")
        self.should_do_layout.addWidget(self.should_do_label)
        self.should_do_list = QtWidgets.QListWidget(self.inner_frame)
        self.should_do_list.setObjectName("should_do_list")
        self.should_do_layout.addWidget(self.should_do_list)
        self.enter_task_frame_should = QtWidgets.QFrame(self.inner_frame)
        self.enter_task_frame_should.setObjectName("enter_task_frame_should")
        self.enter_task_layout_should = QtWidgets.QHBoxLayout(self.enter_task_frame_should)
        self.enter_task_layout_should.setContentsMargins(0, 0, 0, 0)
        self.enter_task_layout_should.setSpacing(0)
        self.enter_task_layout_should.setObjectName("enter_task_layout_should")
        self.add_task_should = QtWidgets.QLineEdit(self.enter_task_frame_should)
        self.add_task_should.setMinimumSize(QtCore.QSize(0, 30))
        self.add_task_should.setObjectName("add_task_should")
        self.enter_task_layout_should.addWidget(self.add_task_should)
        self.add_button_should = QtWidgets.QPushButton(self.enter_task_frame_should)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button_should.sizePolicy().hasHeightForWidth())
        self.add_button_should.setSizePolicy(sizePolicy)
        self.add_button_should.setMinimumSize(QtCore.QSize(40, 30))
        self.add_button_should.setMaximumSize(QtCore.QSize(40, 30))
        self.add_button_should.setObjectName("add_button_should")
        self.enter_task_layout_should.addWidget(self.add_button_should)
        self.should_do_layout.addWidget(self.enter_task_frame_should)
        self.task_list_layout.addLayout(self.should_do_layout)
        self.must_do_layout = QtWidgets.QVBoxLayout()
        self.must_do_layout.setSpacing(0)
        self.must_do_layout.setObjectName("must_do_layout")
        self.must_do_label = QtWidgets.QLabel(self.inner_frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.must_do_label.sizePolicy().hasHeightForWidth())
        self.must_do_label.setSizePolicy(sizePolicy)
        self.must_do_label.setAlignment(QtCore.Qt.AlignCenter)
        self.must_do_label.setObjectName("must_do_label")
        self.must_do_layout.addWidget(self.must_do_label)
        self.must_do_list = QtWidgets.QListWidget(self.inner_frame)
        self.must_do_list.setResizeMode(QtWidgets.QListView.Adjust)
        self.must_do_list.setViewMode(QtWidgets.QListView.ListMode)
        self.must_do_list.setObjectName("must_do_list")
        self.must_do_layout.addWidget(self.must_do_list)
        self.enter_task_frame_must = QtWidgets.QFrame(self.inner_frame)
        self.enter_task_frame_must.setObjectName("enter_task_frame_must")
        self.enter_task_layout_must = QtWidgets.QHBoxLayout(self.enter_task_frame_must)
        self.enter_task_layout_must.setContentsMargins(0, 0, 0, 0)
        self.enter_task_layout_must.setSpacing(0)
        self.enter_task_layout_must.setObjectName("enter_task_layout_must")
        self.add_task_must = QtWidgets.QLineEdit(self.enter_task_frame_must)
        self.add_task_must.setMinimumSize(QtCore.QSize(0, 30))
        self.add_task_must.setToolTipDuration(-1)
        self.add_task_must.setFrame(True)
        self.add_task_must.setObjectName("add_task_must")
        self.enter_task_layout_must.addWidget(self.add_task_must)
        self.add_button_must = QtWidgets.QPushButton(self.enter_task_frame_must)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.add_button_must.sizePolicy().hasHeightForWidth())
        self.add_button_must.setSizePolicy(sizePolicy)
        self.add_button_must.setMinimumSize(QtCore.QSize(40, 30))
        self.add_button_must.setMaximumSize(QtCore.QSize(40, 30))
        self.add_button_must.setObjectName("add_button_must")
        self.enter_task_layout_must.addWidget(self.add_button_must)
        self.must_do_layout.addWidget(self.enter_task_frame_must)
        self.task_list_layout.addLayout(self.must_do_layout)
        self.verticalLayout_3.addLayout(self.task_list_layout)
        self.verticalLayout_2.addWidget(self.inner_frame)
        self.verticalLayout.addWidget(self.outer_frame)

        self.retranslateUi(To_Do_List_widget)
        QtCore.QMetaObject.connectSlotsByName(To_Do_List_widget)

    def retranslateUi(self, To_Do_List_widget):
        _translate = QtCore.QCoreApplication.translate
        To_Do_List_widget.setWindowTitle(_translate("To_Do_List_widget", "Form"))
        self.clear_completed_button.setText(_translate("To_Do_List_widget", "Clear completed"))
        self.title.setText(_translate("To_Do_List_widget", "YOUR TASKS"))
        self.clear_all_button.setText(_translate("To_Do_List_widget", "Clear all"))
        self.date_label.setText(_translate("To_Do_List_widget", "TextLabel"))
        self.nice_to_label.setText(_translate("To_Do_List_widget", "Nice to do"))
        self.add_button_nice.setText(_translate("To_Do_List_widget", "+"))
        self.should_do_label.setText(_translate("To_Do_List_widget", "Should do"))
        self.add_button_should.setText(_translate("To_Do_List_widget", "+"))
        self.must_do_label.setText(_translate("To_Do_List_widget", "Must do"))
        self.add_task_must.setToolTip(_translate("To_Do_List_widget", "Enter new task here"))
        self.add_task_must.setStatusTip(_translate("To_Do_List_widget", "Enter new task here"))
        self.add_task_must.setWhatsThis(_translate("To_Do_List_widget", "Enter new task here"))
        self.add_button_must.setText(_translate("To_Do_List_widget", "+"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    To_Do_List_widget = QtWidgets.QWidget()
    ui = Ui_To_Do_List_widget()
    ui.setupUi(To_Do_List_widget)
    To_Do_List_widget.show()
    sys.exit(app.exec_())
