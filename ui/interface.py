# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_side_menu_interface(object):
    def setupUi(self, side_menu_interface):
        side_menu_interface.setObjectName("side_menu_interface")
        side_menu_interface.resize(1110, 637)
        side_menu_interface.setStyleSheet("*{border:none;}")
        self.centralwidget = QtWidgets.QWidget(side_menu_interface)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.side_menu_container = QtWidgets.QFrame(self.centralwidget)
        self.side_menu_container.setMinimumSize(QtCore.QSize(0, 0))
        self.side_menu_container.setMaximumSize(QtCore.QSize(200, 16777215))
        self.side_menu_container.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu_container.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu_container.setObjectName("side_menu_container")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.side_menu_container)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.slide_menu = QtWidgets.QFrame(self.side_menu_container)
        self.slide_menu.setMinimumSize(QtCore.QSize(180, 0))
        self.slide_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slide_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slide_menu.setObjectName("slide_menu")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.slide_menu)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.frame_7 = QtWidgets.QFrame(self.slide_menu)
        self.frame_7.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_7.setObjectName("frame_7")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.frame_7)
        self.horizontalLayout_8.setContentsMargins(0, 3, 0, 0)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.anns_app_navn = QtWidgets.QLabel(self.frame_7)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.anns_app_navn.setFont(font)
        self.anns_app_navn.setObjectName("anns_app_navn")
        self.horizontalLayout_8.addWidget(self.anns_app_navn, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.heart_logo = QtWidgets.QLabel(self.frame_7)
        self.heart_logo.setText("")
        self.heart_logo.setPixmap(QtGui.QPixmap(":/icons/icons/heart.svg"))
        self.heart_logo.setObjectName("heart_logo")
        self.horizontalLayout_8.addWidget(self.heart_logo, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.verticalLayout_5.addWidget(self.frame_7)
        self.slide_menu_frame = QtWidgets.QFrame(self.slide_menu)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.slide_menu_frame.sizePolicy().hasHeightForWidth())
        self.slide_menu_frame.setSizePolicy(sizePolicy)
        self.slide_menu_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.slide_menu_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.slide_menu_frame.setObjectName("slide_menu_frame")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.slide_menu_frame)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.toolBox = QtWidgets.QToolBox(self.slide_menu_frame)
        self.toolBox.setObjectName("toolBox")
        self.page = QtWidgets.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 200, 524))
        self.page.setObjectName("page")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.page)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.frame_10 = QtWidgets.QFrame(self.page)
        self.frame_10.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_10.setObjectName("frame_10")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.frame_10)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.ToDo_list_button = QtWidgets.QPushButton(self.frame_10)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/icons/check-square.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.ToDo_list_button.setIcon(icon)
        self.ToDo_list_button.setObjectName("ToDo_list_button")
        self.verticalLayout_8.addWidget(self.ToDo_list_button)
        self.rain = QtWidgets.QPushButton(self.frame_10)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/icons/divide.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.rain.setIcon(icon1)
        self.rain.setObjectName("rain")
        self.verticalLayout_8.addWidget(self.rain)
        self.wind = QtWidgets.QPushButton(self.frame_10)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/icons/calendar.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.wind.setIcon(icon2)
        self.wind.setObjectName("wind")
        self.verticalLayout_8.addWidget(self.wind)
        self.verticalLayout_7.addWidget(self.frame_10, 0, QtCore.Qt.AlignTop)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/icons/chevron-down.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolBox.addItem(self.page, icon3, "")
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 200, 752))
        self.page_2.setObjectName("page_2")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.page_2)
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.frame_11 = QtWidgets.QFrame(self.page_2)
        self.frame_11.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_11.setObjectName("frame_11")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.frame_11)
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.thunder = QtWidgets.QPushButton(self.frame_11)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/icons/icons/coffee.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.thunder.setIcon(icon4)
        self.thunder.setObjectName("thunder")
        self.verticalLayout_10.addWidget(self.thunder)
        self.snow = QtWidgets.QPushButton(self.frame_11)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(":/icons/icons/cloud-snow.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.snow.setIcon(icon5)
        self.snow.setObjectName("snow")
        self.verticalLayout_10.addWidget(self.snow)
        self.verticalLayout_9.addWidget(self.frame_11, 0, QtCore.Qt.AlignTop)
        self.additional_text = QtWidgets.QLabel(self.page_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.additional_text.setFont(font)
        self.additional_text.setWordWrap(True)
        self.additional_text.setObjectName("additional_text")
        self.verticalLayout_9.addWidget(self.additional_text, 0, QtCore.Qt.AlignTop)
        self.toolBox.addItem(self.page_2, icon3, "")
        self.verticalLayout_6.addWidget(self.toolBox)
        self.verticalLayout_5.addWidget(self.slide_menu_frame)
        self.frame_9 = QtWidgets.QFrame(self.slide_menu)
        self.frame_9.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_9.setObjectName("frame_9")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.frame_9)
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.exit_button_2 = QtWidgets.QPushButton(self.frame_9)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap(":/icons/icons/external-link.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_button_2.setIcon(icon6)
        self.exit_button_2.setIconSize(QtCore.QSize(16, 16))
        self.exit_button_2.setObjectName("exit_button_2")
        self.horizontalLayout_9.addWidget(self.exit_button_2, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignBottom)
        self.verticalLayout_5.addWidget(self.frame_9)
        self.verticalLayout_2.addWidget(self.slide_menu)
        self.horizontalLayout.addWidget(self.side_menu_container)
        self.main_body = QtWidgets.QFrame(self.centralwidget)
        self.main_body.setStyleSheet("")
        self.main_body.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body.setObjectName("main_body")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.main_body)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.header = QtWidgets.QFrame(self.main_body)
        self.header.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.header.setFrameShadow(QtWidgets.QFrame.Raised)
        self.header.setObjectName("header")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.header)
        self.horizontalLayout_2.setContentsMargins(0, 6, 0, 0)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame_6 = QtWidgets.QFrame(self.header)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.frame_6)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.left_align_Button = QtWidgets.QPushButton(self.frame_6)
        self.left_align_Button.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap(":/icons/icons/align-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.left_align_Button.setIcon(icon7)
        self.left_align_Button.setIconSize(QtCore.QSize(25, 25))
        self.left_align_Button.setObjectName("left_align_Button")
        self.horizontalLayout_7.addWidget(self.left_align_Button, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.horizontalLayout_2.addWidget(self.frame_6, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame = QtWidgets.QFrame(self.header)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.search_bar = QtWidgets.QLineEdit(self.frame)
        self.search_bar.setMinimumSize(QtCore.QSize(250, 0))
        self.search_bar.setMaximumSize(QtCore.QSize(250, 16777215))
        self.search_bar.setStyleSheet("")
        self.search_bar.setObjectName("search_bar")
        self.horizontalLayout_6.addWidget(self.search_bar, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.search_button = QtWidgets.QPushButton(self.frame)
        self.search_button.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap(":/icons/icons/search.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.search_button.setIcon(icon8)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout_6.addWidget(self.search_button, 0, QtCore.Qt.AlignLeft)
        self.horizontalLayout_2.addWidget(self.frame, 0, QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.frame_2 = QtWidgets.QFrame(self.header)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.user_button = QtWidgets.QPushButton(self.frame_2)
        self.user_button.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap(":/icons/icons/home.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.user_button.setIcon(icon9)
        self.user_button.setObjectName("user_button")
        self.horizontalLayout_5.addWidget(self.user_button)
        self.bell_button = QtWidgets.QPushButton(self.frame_2)
        self.bell_button.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap(":/icons/icons/clock.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bell_button.setIcon(icon10)
        self.bell_button.setObjectName("bell_button")
        self.horizontalLayout_5.addWidget(self.bell_button)
        self.horizontalLayout_2.addWidget(self.frame_2, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.frame_3 = QtWidgets.QFrame(self.header)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.minimize_button = QtWidgets.QPushButton(self.frame_3)
        self.minimize_button.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap(":/icons/icons/arrow-down-left.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize_button.setIcon(icon11)
        self.minimize_button.setObjectName("minimize_button")
        self.horizontalLayout_4.addWidget(self.minimize_button)
        self.maximize_button = QtWidgets.QPushButton(self.frame_3)
        self.maximize_button.setText("")
        icon12 = QtGui.QIcon()
        icon12.addPixmap(QtGui.QPixmap(":/icons/icons/maximize-2.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.maximize_button.setIcon(icon12)
        self.maximize_button.setObjectName("maximize_button")
        self.horizontalLayout_4.addWidget(self.maximize_button)
        self.exit_button = QtWidgets.QPushButton(self.frame_3)
        self.exit_button.setText("")
        icon13 = QtGui.QIcon()
        icon13.addPixmap(QtGui.QPixmap(":/icons/icons/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.exit_button.setIcon(icon13)
        self.exit_button.setObjectName("exit_button")
        self.horizontalLayout_4.addWidget(self.exit_button)
        self.horizontalLayout_2.addWidget(self.frame_3, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignTop)
        self.verticalLayout.addWidget(self.header, 0, QtCore.Qt.AlignTop)
        self.main_body_2 = QtWidgets.QFrame(self.main_body)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_2.sizePolicy().hasHeightForWidth())
        self.main_body_2.setSizePolicy(sizePolicy)
        self.main_body_2.setStyleSheet("")
        self.main_body_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.main_body_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.main_body_2.setObjectName("main_body_2")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.main_body_2)
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.main_body_stackedWidget = QtWidgets.QStackedWidget(self.main_body_2)
        self.main_body_stackedWidget.setStyleSheet("")
        self.main_body_stackedWidget.setObjectName("main_body_stackedWidget")
        self.main_widget = QtWidgets.QWidget()
        self.main_widget.setStyleSheet("")
        self.main_widget.setObjectName("main_widget")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.main_widget)
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout()
        self.verticalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.coffee_logo = QtWidgets.QLabel(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.coffee_logo.sizePolicy().hasHeightForWidth())
        self.coffee_logo.setSizePolicy(sizePolicy)
        self.coffee_logo.setMinimumSize(QtCore.QSize(50, 50))
        self.coffee_logo.setMaximumSize(QtCore.QSize(50, 50))
        self.coffee_logo.setText("")
        self.coffee_logo.setPixmap(QtGui.QPixmap(":/icons/icons/layers.svg"))
        self.coffee_logo.setAlignment(QtCore.Qt.AlignCenter)
        self.coffee_logo.setObjectName("coffee_logo")
        self.verticalLayout_12.addWidget(self.coffee_logo, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignBottom)
        self.center_label = QtWidgets.QLabel(self.main_widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.center_label.sizePolicy().hasHeightForWidth())
        self.center_label.setSizePolicy(sizePolicy)
        self.center_label.setMaximumSize(QtCore.QSize(200, 50))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.center_label.setFont(font)
        self.center_label.setAlignment(QtCore.Qt.AlignCenter)
        self.center_label.setObjectName("center_label")
        self.verticalLayout_12.addWidget(self.center_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.horizontalLayout_10.addLayout(self.verticalLayout_12)
        self.main_body_stackedWidget.addWidget(self.main_widget)
        self.timer_page = QtWidgets.QWidget()
        self.timer_page.setStyleSheet("")
        self.timer_page.setObjectName("timer_page")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.timer_page)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(-1, -1, 1002, 1002))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.timer_widget_layout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.timer_widget_layout.setContentsMargins(0, 0, 0, 0)
        self.timer_widget_layout.setSpacing(0)
        self.timer_widget_layout.setObjectName("timer_widget_layout")
        self.main_body_stackedWidget.addWidget(self.timer_page)
        self.verticalLayout_11.addWidget(self.main_body_stackedWidget)
        self.verticalLayout.addWidget(self.main_body_2)
        self.footer = QtWidgets.QFrame(self.main_body)
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.footer)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.footer)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.bottom_label = QtWidgets.QLabel(self.frame_4)
        self.bottom_label.setObjectName("bottom_label")
        self.verticalLayout_4.addWidget(self.bottom_label, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_3.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.footer)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.pushButton = QtWidgets.QPushButton(self.frame_5)
        self.pushButton.setText("")
        icon14 = QtGui.QIcon()
        icon14.addPixmap(QtGui.QPixmap(":/icons/icons/box.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon14)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_3.addWidget(self.pushButton, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout_3.addWidget(self.frame_5)
        self.size_grip = QtWidgets.QFrame(self.footer)
        self.size_grip.setMinimumSize(QtCore.QSize(10, 10))
        self.size_grip.setMaximumSize(QtCore.QSize(10, 10))
        self.size_grip.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QtWidgets.QFrame.Raised)
        self.size_grip.setObjectName("size_grip")
        self.horizontalLayout_3.addWidget(self.size_grip, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.footer, 0, QtCore.Qt.AlignBottom)
        self.horizontalLayout.addWidget(self.main_body)
        side_menu_interface.setCentralWidget(self.centralwidget)

        self.retranslateUi(side_menu_interface)
        self.toolBox.setCurrentIndex(0)
        self.main_body_stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(side_menu_interface)

    def retranslateUi(self, side_menu_interface):
        _translate = QtCore.QCoreApplication.translate
        side_menu_interface.setWindowTitle(_translate("side_menu_interface", "MainWindow"))
        self.anns_app_navn.setText(_translate("side_menu_interface", "ANNS APP"))
        self.ToDo_list_button.setText(_translate("side_menu_interface", "TO DO LIST"))
        self.rain.setText(_translate("side_menu_interface", "Time calculator"))
        self.wind.setText(_translate("side_menu_interface", "Fagkvelder overtid"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("side_menu_interface", "Praktisk"))
        self.thunder.setText(_translate("side_menu_interface", "Spisesteder"))
        self.snow.setText(_translate("side_menu_interface", "snow"))
        self.additional_text.setText(_translate("side_menu_interface", "Placeholder for a message. This could be a very long, or just a short message."))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("side_menu_interface", "Personlig"))
        self.exit_button_2.setText(_translate("side_menu_interface", "EXIT"))
        self.search_bar.setPlaceholderText(_translate("side_menu_interface", "Search"))
        self.center_label.setText(_translate("side_menu_interface", "STARTPAGE"))
        self.bottom_label.setText(_translate("side_menu_interface", "Anns desktop GUI 03.22"))
import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    side_menu_interface = QtWidgets.QMainWindow()
    ui = Ui_side_menu_interface()
    ui.setupUi(side_menu_interface)
    side_menu_interface.show()
    sys.exit(app.exec_())
