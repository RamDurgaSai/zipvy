# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QSize,QMetaObject,QCoreApplication
from PySide2.QtGui import QFont,Qt
from PySide2.QtWidgets import QHBoxLayout,QWidget,QFrame,QVBoxLayout,QSpacerItem,QSizePolicy,\
                                QTextEdit,QCheckBox,QLabel,QComboBox,QLineEdit,QProgressBar,QPushButton,QToolButton


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(787, 415)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.base = QFrame(self.centralwidget)
        self.base.setObjectName(u"base")
        self.base.setStyleSheet(u"QFrame{\n"
"\n"
"	\n"
"	background-color: rgb(97, 101, 157);\n"
"}")
        self.base.setFrameShape(QFrame.StyledPanel)
        self.base.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.base)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.frame_for_widgets = QFrame(self.base)
        self.frame_for_widgets.setObjectName(u"frame_for_widgets")
        self.frame_for_widgets.setStyleSheet(u"QFrame{\n"
"\n"
"border-radius:25px;\n"
"\n"
"\n"
"\n"
"background-color: rgb(24, 25, 39);\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"\n"
"}")
        self.frame_for_widgets.setFrameShape(QFrame.NoFrame)
        self.frame_for_widgets.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_for_widgets)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.frame_for_widgets)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.select_zip_button = QPushButton(self.frame)
        self.select_zip_button.setObjectName(u"select_zip_button")
        self.select_zip_button.setMinimumSize(QSize(75, 75))
        self.select_zip_button.setMaximumSize(QSize(75, 75))
        font = QFont()
        font.setFamily(u"Segoe UI Light")
        font.setPointSize(24)
        self.select_zip_button.setFont(font)
        self.select_zip_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(30, 149, 198);\n"
"	 border: 2px solid black;\n"
"\n"
"	border-color:rgb(240, 123, 255);\n"
"	\n"
"	background-color: rgb(42, 44, 68);\n"
"	\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"border-color:rgb(255, 37, 255);\n"
"\n"
"\n"
"}")

        self.horizontalLayout_2.addWidget(self.select_zip_button)

        self.horizontalSpacer = QSpacerItem(331, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addWidget(self.frame)

        self.frame_left_middle = QFrame(self.frame_for_widgets)
        self.frame_left_middle.setObjectName(u"frame_left_middle")
        self.frame_left_middle.setFrameShape(QFrame.StyledPanel)
        self.frame_left_middle.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_left_middle)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_left_middle_up = QFrame(self.frame_left_middle)
        self.frame_left_middle_up.setObjectName(u"frame_left_middle_up")
        self.frame_left_middle_up.setFrameShape(QFrame.StyledPanel)
        self.frame_left_middle_up.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_left_middle_up)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.frame_left_middle_up)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Arial Rounded MT Bold")
        font1.setPointSize(11)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel{\n"
" color:rgb(30, 149, 198);\n"
"\n"
"	\n"
"\n"
"	}")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)

        self.lineEdit = QLineEdit(self.frame_left_middle_up)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"color:rgb(30, 149, 198);\n"
"	background-color: rgb(65, 69, 106);\n"
"\n"
"border:2px solid black;\n"
"\n"
"border-radius:3px;\n"
"border-color:rgb(240, 123, 255);\n"
"\n"
"}")

        self.horizontalLayout_3.addWidget(self.lineEdit)

        self.same_as_zip_name_checkbox = QCheckBox(self.frame_left_middle_up)
        self.same_as_zip_name_checkbox.setObjectName(u"same_as_zip_name_checkbox")
        font2 = QFont()
        font2.setFamily(u"Arial Rounded MT Bold")
        font2.setPointSize(10)
        self.same_as_zip_name_checkbox.setFont(font2)
        self.same_as_zip_name_checkbox.setStyleSheet(u"QCheckBox{\n"
"color:rgb(30, 149, 198);\n"
"\n"
"}\n"
"QCheckBox:unchecked {\n"
"   \n"
"	 color:rgb(30, 149, 198);\n"
"}\n"
"QCheckBox::indicator {\n"
"    width: 13px;\n"
"    height: 13px;\n"
"	\n"
"	color: rgb(30, 149, 198);\n"
"	background-color: rgb(42, 44, 68);\n"
"}\n"
"QCheckBox::indicator:checked {\n"
"   \n"
"	\n"
"	background-color: rgb(192, 98, 204);\n"
"}\n"
"QCheckBox:checked {\n"
"\n"
"color: rgb(38, 194, 255);\n"
" \n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"color: rgb(253, 111, 54);\n"
"    \n"
"}\n"
"")

        self.horizontalLayout_3.addWidget(self.same_as_zip_name_checkbox)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)

        self.horizontalSpacer_2 = QSpacerItem(85, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_2)


        self.verticalLayout_5.addWidget(self.frame_left_middle_up)

        self.frame_3 = QFrame(self.frame_left_middle)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(100, 0))
        font3 = QFont()
        font3.setFamily(u"Segoe UI")
        font3.setPointSize(12)
        self.label_2.setFont(font3)
        self.label_2.setStyleSheet(u"QLabel{\n"
"\n"
"	\n"
"	\n"
" color:rgb(30, 149, 198);\n"
"\n"
"	\n"
"\n"
"	}")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_5.addWidget(self.label_2)

        self.algorithm_combobox = QComboBox(self.frame_3)
        self.algorithm_combobox.addItem("")
        self.algorithm_combobox.addItem("")
        self.algorithm_combobox.addItem("")
        self.algorithm_combobox.addItem("")
        self.algorithm_combobox.setObjectName(u"algorithm_combobox")
        self.algorithm_combobox.setMinimumSize(QSize(150, 0))
        font4 = QFont()
        font4.setFamily(u"Segoe UI")
        font4.setPointSize(10)
        font4.setBold(True)
        font4.setWeight(75)
        self.algorithm_combobox.setFont(font4)
        self.algorithm_combobox.setStyleSheet(u"QComboBox{\n"
"\n"
"	\n"
"	color:rgb(30, 149, 198);\n"
"\n"
"	border:2px solid black;\n"
"	border-color:rgb(240, 123, 255);\n"
"	background-color: rgb(42, 44, 68);\n"
"	\n"
"\n"
"}\n"
"QComboBox::down-arrow {\n"
"  border:1px solid black;\n"
"border-color:rgb(30, 149, 198);\n"
"}\n"
"\n"
"ComboBox::drop-down {\n"
"   \n"
"	color: rgb(30, 149, 198);\n"
"	background-color: rgb(56, 58, 91);\n"
"}\n"
"\n"
"\n"
"QComboBox::down-arrow:on { /* shift the arrow when popup is open */\n"
"    top: 1px;\n"
"    left: 1px;\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.algorithm_combobox)


        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)

        self.horizontalSpacer_3 = QSpacerItem(146, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_3)


        self.verticalLayout_5.addWidget(self.frame_3)


        self.verticalLayout_4.addWidget(self.frame_left_middle)

        self.frame_left_bottom = QFrame(self.frame_for_widgets)
        self.frame_left_bottom.setObjectName(u"frame_left_bottom")
        self.frame_left_bottom.setFrameShape(QFrame.StyledPanel)
        self.frame_left_bottom.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_left_bottom)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.frame_for_start_button = QFrame(self.frame_left_bottom)
        self.frame_for_start_button.setObjectName(u"frame_for_start_button")
        self.frame_for_start_button.setFrameShape(QFrame.StyledPanel)
        self.frame_for_start_button.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.frame_for_start_button)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_3 = QLabel(self.frame_for_start_button)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(100, 0))
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"QLabel{\n"
"\n"
"	\n"
" color:rgb(30, 149, 198);\n"
"\n"
"	\n"
"\n"
"	}")
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_7.addWidget(self.label_3)

        self.toolButton = QToolButton(self.frame_for_start_button)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setStyleSheet(u"QToolButton{\n"
"	color:rgb(30, 149, 198);\n"
"	 border: 2px solid black;\n"
"\n"
"	border-color:rgb(240, 123, 255);\n"
"	\n"
"	background-color: rgb(42, 44, 68);\n"
"	\n"
"	border-radius:1px;\n"
"}\n"
"QToolButton:hover{\n"
"\n"
"\n"
"border-color:rgb(255, 37, 255);\n"
"\n"
"\n"
"}")

        self.horizontalLayout_7.addWidget(self.toolButton)


        self.horizontalLayout_8.addLayout(self.horizontalLayout_7)

        self.horizontalSpacer_4 = QSpacerItem(190, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_4)

        self.start_button = QPushButton(self.frame_for_start_button)
        self.start_button.setObjectName(u"start_button")
        self.start_button.setMinimumSize(QSize(75, 75))
        font5 = QFont()
        font5.setFamily(u"Segoe UI Light")
        font5.setPointSize(28)
        self.start_button.setFont(font5)
        self.start_button.setStyleSheet(u"QPushButton{\n"
"	color:rgb(30, 149, 198);\n"
"	 border: 2px solid black;\n"
"\n"
"	border-color:rgb(240, 123, 255);\n"
"	\n"
"	background-color: rgb(42, 44, 68);\n"
"	\n"
"	border-radius:10px;\n"
"}\n"
"QPushButton:hover{\n"
"\n"
"\n"
"border-color:rgb(255, 37, 255);\n"
"\n"
"\n"
"}")

        self.horizontalLayout_8.addWidget(self.start_button)


        self.verticalLayout_6.addWidget(self.frame_for_start_button)

        self.frame_for_progressbar = QFrame(self.frame_left_bottom)
        self.frame_for_progressbar.setObjectName(u"frame_for_progressbar")
        self.frame_for_progressbar.setFrameShape(QFrame.StyledPanel)
        self.frame_for_progressbar.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_for_progressbar)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalSpacer_5 = QSpacerItem(13, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_progress = QLabel(self.frame_for_progressbar)
        self.label_progress.setObjectName(u"label_progress")
        self.label_progress.setFont(font2)
        self.label_progress.setStyleSheet(u"QLabel{\n"
"\n"
" color:rgb(30, 149, 198);\n"
"	\n"
"\n"
"	}")
        self.label_progress.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_progress)

        self.progressBar = QProgressBar(self.frame_for_progressbar)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(350, 20))
        self.progressBar.setMaximumSize(QSize(450, 20))
        font6 = QFont()
        font6.setFamily(u"Segoe UI")
        font6.setPointSize(9)
        self.progressBar.setFont(font6)
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"\n"
"	\n"
"	color:rgb(30, 149, 198);\n"
"\n"
"	 border: 1px solid black;\n"
"\n"
"	border-color:rgb(240, 123, 255);\n"
"	\n"
"	background-color: rgb(42, 44, 68);\n"
"	\n"
"	border-radius:2px;\n"
"}\n"
"QProgressBar::chunk{\n"
"\n"
"border-radius:2px;\n"
"\n"
"	background-color:rgb(30, 149, 198);\n"
"}\n"
"QProgressBar:hover{\n"
"border-color:rgb(255, 37, 255);\n"
"}")
        self.progressBar.setMaximum(100)
        self.progressBar.setValue(56)
        self.progressBar.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.progressBar.setTextVisible(True)
        self.progressBar.setInvertedAppearance(False)

        self.horizontalLayout_9.addWidget(self.progressBar)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_9)


        self.verticalLayout_6.addWidget(self.frame_for_progressbar)


        self.verticalLayout_4.addWidget(self.frame_left_bottom)


        self.horizontalLayout.addWidget(self.frame_for_widgets)

        self.frame_for_textedit = QFrame(self.base)
        self.frame_for_textedit.setObjectName(u"frame_for_textedit")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame_for_textedit.sizePolicy().hasHeightForWidth())
        self.frame_for_textedit.setSizePolicy(sizePolicy1)
        self.frame_for_textedit.setMinimumSize(QSize(30, 0))
        self.frame_for_textedit.setMaximumSize(QSize(350, 16777215))
        self.frame_for_textedit.setFrameShape(QFrame.StyledPanel)
        self.frame_for_textedit.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame_for_textedit)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 0, 0, 0)
        self.terminal_output = QTextEdit(self.frame_for_textedit)
        self.terminal_output.setObjectName(u"terminal_output")
        self.terminal_output.setFont(font2)
        self.terminal_output.setStyleSheet(u"\n"
"QTextEdit, QListView {\n"
"   color:rgb(255, 37, 255);\n"
"    background-color:rgb(40, 41, 65);\n"
"	border:3px solid black;\n"
"	border-radius:10px;\n"
"	border-color:rgb(30, 149, 198);\n"
"    background-attachment: scroll;\n"
"}")

        self.verticalLayout_2.addWidget(self.terminal_output)


        self.horizontalLayout.addWidget(self.frame_for_textedit)


        self.verticalLayout.addWidget(self.base)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.select_zip_button.setText(QCoreApplication.translate("MainWindow", u"Zip", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Video Name :", None))
        self.same_as_zip_name_checkbox.setText(QCoreApplication.translate("MainWindow", u"Same as Zip name", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Algorithm", None))
        self.algorithm_combobox.setItemText(0, QCoreApplication.translate("MainWindow", u"Select", None))
        self.algorithm_combobox.setItemText(1, QCoreApplication.translate("MainWindow", u"Very Fast - Good", None))
        self.algorithm_combobox.setItemText(2, QCoreApplication.translate("MainWindow", u"Fast - Better", None))
        self.algorithm_combobox.setItemText(3, QCoreApplication.translate("MainWindow", u"Slow - Best", None))

        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Video Location", None))
        self.toolButton.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.start_button.setText(QCoreApplication.translate("MainWindow", u"Start", None))
        self.label_progress.setText(QCoreApplication.translate("MainWindow", u"Progress :", None))
        self.terminal_output.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Arial Rounded MT Bold'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Segoe UI Light'; color:#f07bff;\">Zipvy Ready...</span></p></body></html>", None))
    # retranslateUi

