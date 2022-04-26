# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1440, 900)
        MainWindow.setStyleSheet("background-color: rgb(17, 29, 38);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWelcome = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWelcome.setGeometry(QtCore.QRect(0, 0, 1440, 900))
        self.stackedWelcome.setObjectName("stackedWelcome")
        self.welcome = QtWidgets.QWidget()
        self.welcome.setObjectName("welcome")
        self.welcome_win = QtWidgets.QFrame(self.welcome)
        self.welcome_win.setGeometry(QtCore.QRect(495, 161, 451, 578))
        self.welcome_win.setStyleSheet("\n"
"background: rgba(58, 86, 111, 0.6);\n"
"border-radius: 40px;\n"
"")
        self.welcome_win.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.welcome_win.setFrameShadow(QtWidgets.QFrame.Raised)
        self.welcome_win.setObjectName("welcome_win")
        self.welcome_bold = QtWidgets.QLabel(self.welcome_win)
        self.welcome_bold.setGeometry(QtCore.QRect(180, 150, 91, 20))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.welcome_bold.setFont(font)
        self.welcome_bold.setStyleSheet("color: white;\n"
"font: 57 20pt \"Roboto\";\n"
"background-color: none;\n"
"font-weight: bold")
        self.welcome_bold.setObjectName("welcome_bold")
        self.welcome_desc = QtWidgets.QLabel(self.welcome_win)
        self.welcome_desc.setGeometry(QtCore.QRect(72, 170, 321, 151))
        self.welcome_desc.setStyleSheet("color: white;\n"
"font: 12pt \"Roboto\";\n"
"background-color: none;")
        self.welcome_desc.setWordWrap(True)
        self.welcome_desc.setObjectName("welcome_desc")
        self.btn_upload = QtWidgets.QPushButton(self.welcome_win)
        self.btn_upload.setGeometry(QtCore.QRect(100, 330, 246, 47))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_upload.setFont(font)
        self.btn_upload.setStyleSheet("color: white;\n"
"font: 57 16pt \"Roboto\";\n"
"font-weight: bold;\n"
"background-color: #45AA9E;\n"
"border-radius: 12px;")
        self.btn_upload.setObjectName("btn_upload")
        self.note = QtWidgets.QLabel(self.welcome_win)
        self.note.setGeometry(QtCore.QRect(100, 390, 261, 20))
        self.note.setStyleSheet("color: white;\n"
"background-color: none;\n"
"font: 57 10pt \"Roboto\";")
        self.note.setObjectName("note")
        self.label_2 = QtWidgets.QLabel(self.welcome_win)
        self.label_2.setGeometry(QtCore.QRect(217, 430, 21, 20))
        self.label_2.setStyleSheet("color: white;\n"
"background-color: none;\n"
"font: 57 16pt \"Roboto\";")
        self.label_2.setObjectName("label_2")
        self.combo_box = QtWidgets.QComboBox(self.welcome_win)
        self.combo_box.setGeometry(QtCore.QRect(101, 470, 141, 31))
        self.combo_box.setStyleSheet("border-radius: 6px;\n"
"color: white;\n"
"border: 1px solid white;")
        self.combo_box.setObjectName("combo_box")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.combo_box.addItem("")
        self.btn_sample = QtWidgets.QPushButton(self.welcome_win)
        self.btn_sample.setGeometry(QtCore.QRect(253, 470, 91, 31))
        self.btn_sample.setStyleSheet("color: white;\n"
"font: 57 16pt \"Roboto\";\n"
"font-weight: bold;\n"
"background-color: #45AA9E;\n"
"border-radius: 6px;")
        self.btn_sample.setObjectName("btn_sample")
        self.logo = QtWidgets.QLabel(self.welcome_win)
        self.logo.setGeometry(QtCore.QRect(90, 60, 271, 71))
        self.logo.setStyleSheet("background-color: none;")
        self.logo.setText("")
        self.logo.setPixmap(QtGui.QPixmap("visual_comp/dataanal-logo.png"))
        self.logo.setObjectName("logo")
        self.stackedWelcome.addWidget(self.welcome)
        self.main = QtWidgets.QWidget()
        self.main.setObjectName("main")
        self.stackedMain = QtWidgets.QStackedWidget(self.main)
        self.stackedMain.setGeometry(QtCore.QRect(470, 0, 971, 801))
        self.stackedMain.setStyleSheet("")
        self.stackedMain.setObjectName("stackedMain")
        self.raw = QtWidgets.QWidget()
        self.raw.setObjectName("raw")
        self.description = QtWidgets.QLabel(self.raw)
        self.description.setGeometry(QtCore.QRect(0, 145, 847, 80))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.description.setFont(font)
        self.description.setStyleSheet("color: rgb(255, 255, 255);")
        self.description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description.setObjectName("description")
        self.step = QtWidgets.QLabel(self.raw)
        self.step.setGeometry(QtCore.QRect(0, 72, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.step.setFont(font)
        self.step.setStyleSheet("color: rgb(255, 255, 255);")
        self.step.setObjectName("step")
        self.label_12 = QtWidgets.QLabel(self.raw)
        self.label_12.setGeometry(QtCore.QRect(825, 253, 21, 16))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("visual_comp/arrow.png"))
        self.label_12.setObjectName("label_12")
        self.btn_text_info = QtWidgets.QPushButton(self.raw)
        self.btn_text_info.setGeometry(QtCore.QRect(0, 236, 165, 47))
        self.btn_text_info.setStyleSheet("border: none")
        self.btn_text_info.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("visual_comp/raw_text_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_text_info.setIcon(icon)
        self.btn_text_info.setIconSize(QtCore.QSize(165, 47))
        self.btn_text_info.setObjectName("btn_text_info")
        self.btn_visualize = QtWidgets.QPushButton(self.raw)
        self.btn_visualize.setGeometry(QtCore.QRect(200, 236, 165, 47))
        self.btn_visualize.setStyleSheet("border: none")
        self.btn_visualize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("visual_comp/raw_visualize_button.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_visualize.setIcon(icon1)
        self.btn_visualize.setIconSize(QtCore.QSize(165, 47))
        self.btn_visualize.setObjectName("btn_visualize")
        self.btn_preprocess = QtWidgets.QPushButton(self.raw)
        self.btn_preprocess.setGeometry(QtCore.QRect(705, 250, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_preprocess.setFont(font)
        self.btn_preprocess.setStyleSheet("color: rgb(0, 230, 204);\n"
"border: none;\n"
"text-align: right")
        self.btn_preprocess.setObjectName("btn_preprocess")
        self.out_raw = QtWidgets.QFrame(self.raw)
        self.out_raw.setGeometry(QtCore.QRect(0, 348, 874, 433))
        self.out_raw.setStyleSheet("background-color: rgb(29, 52, 70);\n"
"border-radius: 40;")
        self.out_raw.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.out_raw.setFrameShadow(QtWidgets.QFrame.Raised)
        self.out_raw.setObjectName("out_raw")
        self.out_console = QtWidgets.QLabel(self.out_raw)
        self.out_console.setGeometry(QtCore.QRect(40, 30, 711, 381))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(14)
        self.out_console.setFont(font)
        self.out_console.setStyleSheet("color: rgb(255, 255, 255);")
        self.out_console.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.out_console.setWordWrap(True)
        self.out_console.setObjectName("out_console")
        self.stackedMain.addWidget(self.raw)
        self.preprocess = QtWidgets.QWidget()
        self.preprocess.setObjectName("preprocess")
        self.menu_8 = QtWidgets.QLabel(self.preprocess)
        self.menu_8.setGeometry(QtCore.QRect(0, 72, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.menu_8.setFont(font)
        self.menu_8.setStyleSheet("color: rgb(255, 255, 255);")
        self.menu_8.setObjectName("menu_8")
        self.label_6 = QtWidgets.QLabel(self.preprocess)
        self.label_6.setGeometry(QtCore.QRect(0, 145, 847, 80))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_6.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_6.setWordWrap(True)
        self.label_6.setObjectName("label_6")
        self.label_8 = QtWidgets.QLabel(self.preprocess)
        self.label_8.setGeometry(QtCore.QRect(825, 252, 21, 16))
        self.label_8.setText("")
        self.label_8.setPixmap(QtGui.QPixmap("visual_comp/arrow.png"))
        self.label_8.setObjectName("label_8")
        self.btn_preprocess_plot = QtWidgets.QPushButton(self.preprocess)
        self.btn_preprocess_plot.setGeometry(QtCore.QRect(0, 236, 165, 47))
        self.btn_preprocess_plot.setStyleSheet("border: none")
        self.btn_preprocess_plot.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("visual_comp/button_preprocess1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_preprocess_plot.setIcon(icon2)
        self.btn_preprocess_plot.setIconSize(QtCore.QSize(165, 47))
        self.btn_preprocess_plot.setObjectName("btn_preprocess_plot")
        self.btn_comparesignals = QtWidgets.QPushButton(self.preprocess)
        self.btn_comparesignals.setGeometry(QtCore.QRect(210, 236, 201, 47))
        self.btn_comparesignals.setStyleSheet("border: none")
        self.btn_comparesignals.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("visual_comp/button_preprocess2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_comparesignals.setIcon(icon3)
        self.btn_comparesignals.setIconSize(QtCore.QSize(201, 47))
        self.btn_comparesignals.setObjectName("btn_comparesignals")
        self.btn_detectevents = QtWidgets.QPushButton(self.preprocess)
        self.btn_detectevents.setGeometry(QtCore.QRect(718, 250, 101, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_detectevents.setFont(font)
        self.btn_detectevents.setStyleSheet("color: rgb(0, 230, 204);\n"
"border: none;\n"
"text-align: right")
        self.btn_detectevents.setObjectName("btn_detectevents")
        self.out_preprocess = QtWidgets.QFrame(self.preprocess)
        self.out_preprocess.setGeometry(QtCore.QRect(0, 348, 874, 433))
        self.out_preprocess.setStyleSheet("background-color: rgb(29, 52, 70);\n"
"border-radius: 40;")
        self.out_preprocess.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.out_preprocess.setFrameShadow(QtWidgets.QFrame.Raised)
        self.out_preprocess.setObjectName("out_preprocess")
        self.stackedMain.addWidget(self.preprocess)
        self.events = QtWidgets.QWidget()
        self.events.setObjectName("events")
        self.label_9 = QtWidgets.QLabel(self.events)
        self.label_9.setGeometry(QtCore.QRect(830, 252, 16, 16))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("visual_comp/arrow.png"))
        self.label_9.setObjectName("label_9")
        self.menu_9 = QtWidgets.QLabel(self.events)
        self.menu_9.setGeometry(QtCore.QRect(0, 72, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.menu_9.setFont(font)
        self.menu_9.setStyleSheet("color: rgb(255, 255, 255);")
        self.menu_9.setObjectName("menu_9")
        self.label_7 = QtWidgets.QLabel(self.events)
        self.label_7.setGeometry(QtCore.QRect(0, 145, 847, 80))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_7.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_7.setWordWrap(True)
        self.label_7.setObjectName("label_7")
        self.btn_findevents = QtWidgets.QPushButton(self.events)
        self.btn_findevents.setGeometry(QtCore.QRect(0, 236, 165, 47))
        self.btn_findevents.setStyleSheet("border: none")
        self.btn_findevents.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("visual_comp/button_findevents.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_findevents.setIcon(icon4)
        self.btn_findevents.setIconSize(QtCore.QSize(165, 47))
        self.btn_findevents.setObjectName("btn_findevents")
        self.btn_plotevents = QtWidgets.QPushButton(self.events)
        self.btn_plotevents.setGeometry(QtCore.QRect(210, 236, 201, 47))
        self.btn_plotevents.setStyleSheet("border: none")
        self.btn_plotevents.setText("")
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("visual_comp/button_plotevents.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_plotevents.setIcon(icon5)
        self.btn_plotevents.setIconSize(QtCore.QSize(201, 47))
        self.btn_plotevents.setObjectName("btn_plotevents")
        self.btn_epoch = QtWidgets.QPushButton(self.events)
        self.btn_epoch.setGeometry(QtCore.QRect(770, 250, 51, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_epoch.setFont(font)
        self.btn_epoch.setStyleSheet("color: rgb(0, 230, 204);\n"
"border: none;\n"
"text-align: right")
        self.btn_epoch.setObjectName("btn_epoch")
        self.out_events = QtWidgets.QFrame(self.events)
        self.out_events.setGeometry(QtCore.QRect(0, 348, 874, 433))
        self.out_events.setStyleSheet("background-color: rgb(29, 52, 70);\n"
"border-radius: 40;")
        self.out_events.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.out_events.setFrameShadow(QtWidgets.QFrame.Raised)
        self.out_events.setObjectName("out_events")
        self.stackedMain.addWidget(self.events)
        self.epoch = QtWidgets.QWidget()
        self.epoch.setObjectName("epoch")
        self.label_10 = QtWidgets.QLabel(self.epoch)
        self.label_10.setGeometry(QtCore.QRect(830, 260, 60, 16))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("visual_comp/arrow.png"))
        self.label_10.setObjectName("label_10")
        self.menu_10 = QtWidgets.QLabel(self.epoch)
        self.menu_10.setGeometry(QtCore.QRect(0, 72, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.menu_10.setFont(font)
        self.menu_10.setStyleSheet("color: rgb(255, 255, 255);")
        self.menu_10.setObjectName("menu_10")
        self.label_11 = QtWidgets.QLabel(self.epoch)
        self.label_11.setGeometry(QtCore.QRect(0, 145, 847, 80))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_11.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.label_11.setWordWrap(True)
        self.label_11.setObjectName("label_11")
        self.btn_dropepochs = QtWidgets.QPushButton(self.epoch)
        self.btn_dropepochs.setGeometry(QtCore.QRect(0, 246, 165, 47))
        self.btn_dropepochs.setStyleSheet("border: none")
        self.btn_dropepochs.setText("")
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("visual_comp/button_drop_epochs.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_dropepochs.setIcon(icon6)
        self.btn_dropepochs.setIconSize(QtCore.QSize(165, 47))
        self.btn_dropepochs.setObjectName("btn_dropepochs")
        self.btn_imagemap = QtWidgets.QPushButton(self.epoch)
        self.btn_imagemap.setGeometry(QtCore.QRect(210, 246, 201, 47))
        self.btn_imagemap.setStyleSheet("border: none")
        self.btn_imagemap.setText("")
        icon7 = QtGui.QIcon()
        icon7.addPixmap(QtGui.QPixmap("visual_comp/button_imagemap.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_imagemap.setIcon(icon7)
        self.btn_imagemap.setIconSize(QtCore.QSize(201, 47))
        self.btn_imagemap.setObjectName("btn_imagemap")
        self.btn_tfa = QtWidgets.QPushButton(self.epoch)
        self.btn_tfa.setGeometry(QtCore.QRect(640, 258, 181, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_tfa.setFont(font)
        self.btn_tfa.setStyleSheet("color: rgb(0, 230, 204);\n"
"border: none;")
        self.btn_tfa.setObjectName("btn_tfa")
        self.out_epoch = QtWidgets.QFrame(self.epoch)
        self.out_epoch.setGeometry(QtCore.QRect(0, 348, 874, 433))
        self.out_epoch.setStyleSheet("background-color: rgb(29, 52, 70);\n"
"border-radius: 40;")
        self.out_epoch.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.out_epoch.setFrameShadow(QtWidgets.QFrame.Raised)
        self.out_epoch.setObjectName("out_epoch")
        self.stackedMain.addWidget(self.epoch)
        self.tfa = QtWidgets.QWidget()
        self.tfa.setObjectName("tfa")
        self.description_tfa = QtWidgets.QLabel(self.tfa)
        self.description_tfa.setGeometry(QtCore.QRect(0, 145, 847, 80))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.description_tfa.setFont(font)
        self.description_tfa.setStyleSheet("color: rgb(255, 255, 255);")
        self.description_tfa.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description_tfa.setWordWrap(True)
        self.description_tfa.setObjectName("description_tfa")
        self.label_tfa = QtWidgets.QLabel(self.tfa)
        self.label_tfa.setGeometry(QtCore.QRect(0, 72, 461, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_tfa.setFont(font)
        self.label_tfa.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_tfa.setObjectName("label_tfa")
        self.label_13 = QtWidgets.QLabel(self.tfa)
        self.label_13.setGeometry(QtCore.QRect(830, 252, 60, 16))
        self.label_13.setText("")
        self.label_13.setPixmap(QtGui.QPixmap("visual_comp/arrow.png"))
        self.label_13.setObjectName("label_13")
        self.btn_evoked = QtWidgets.QPushButton(self.tfa)
        self.btn_evoked.setGeometry(QtCore.QRect(620, 250, 201, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_evoked.setFont(font)
        self.btn_evoked.setStyleSheet("color: rgb(0, 230, 204);\n"
"border: none;")
        self.btn_evoked.setObjectName("btn_evoked")
        self.btn_tfa1 = QtWidgets.QPushButton(self.tfa)
        self.btn_tfa1.setGeometry(QtCore.QRect(0, 236, 268, 47))
        self.btn_tfa1.setStyleSheet("border: none")
        self.btn_tfa1.setText("")
        icon8 = QtGui.QIcon()
        icon8.addPixmap(QtGui.QPixmap("visual_comp/button_tfa_1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_tfa1.setIcon(icon8)
        self.btn_tfa1.setIconSize(QtCore.QSize(281, 47))
        self.btn_tfa1.setObjectName("btn_tfa1")
        self.out_tfa = QtWidgets.QFrame(self.tfa)
        self.out_tfa.setGeometry(QtCore.QRect(0, 348, 874, 433))
        self.out_tfa.setStyleSheet("background-color: rgb(29, 52, 70);\n"
"border-radius: 40;")
        self.out_tfa.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.out_tfa.setFrameShadow(QtWidgets.QFrame.Raised)
        self.out_tfa.setObjectName("out_tfa")
        self.stackedMain.addWidget(self.tfa)
        self.evoked = QtWidgets.QWidget()
        self.evoked.setObjectName("evoked")
        self.description_evoked = QtWidgets.QLabel(self.evoked)
        self.description_evoked.setGeometry(QtCore.QRect(0, 145, 847, 80))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        self.description_evoked.setFont(font)
        self.description_evoked.setStyleSheet("color: rgb(255, 255, 255);")
        self.description_evoked.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.description_evoked.setWordWrap(True)
        self.description_evoked.setObjectName("description_evoked")
        self.label_evoked = QtWidgets.QLabel(self.evoked)
        self.label_evoked.setGeometry(QtCore.QRect(0, 72, 401, 21))
        font = QtGui.QFont()
        font.setFamily("Helvetica Neue")
        font.setPointSize(25)
        font.setBold(True)
        font.setWeight(75)
        self.label_evoked.setFont(font)
        self.label_evoked.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_evoked.setObjectName("label_evoked")
        self.arrow_6 = QtWidgets.QLabel(self.evoked)
        self.arrow_6.setGeometry(QtCore.QRect(830, 260, 60, 16))
        self.arrow_6.setText("")
        self.arrow_6.setPixmap(QtGui.QPixmap("visual_comp/arrow.png"))
        self.arrow_6.setObjectName("arrow_6")
        self.btn_evoked1 = QtWidgets.QPushButton(self.evoked)
        self.btn_evoked1.setGeometry(QtCore.QRect(0, 246, 268, 47))
        self.btn_evoked1.setStyleSheet("border: none")
        self.btn_evoked1.setText("")
        icon9 = QtGui.QIcon()
        icon9.addPixmap(QtGui.QPixmap("visual_comp/button_evoked1.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_evoked1.setIcon(icon9)
        self.btn_evoked1.setIconSize(QtCore.QSize(281, 47))
        self.btn_evoked1.setObjectName("btn_evoked1")
        self.btn_evoked2 = QtWidgets.QPushButton(self.evoked)
        self.btn_evoked2.setGeometry(QtCore.QRect(300, 246, 141, 47))
        self.btn_evoked2.setStyleSheet("border: none")
        self.btn_evoked2.setText("")
        icon10 = QtGui.QIcon()
        icon10.addPixmap(QtGui.QPixmap("visual_comp/button_evoked2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_evoked2.setIcon(icon10)
        self.btn_evoked2.setIconSize(QtCore.QSize(165, 47))
        self.btn_evoked2.setObjectName("btn_evoked2")
        self.btn_tevoked3 = QtWidgets.QPushButton(self.evoked)
        self.btn_tevoked3.setGeometry(QtCore.QRect(470, 246, 141, 47))
        self.btn_tevoked3.setStyleSheet("border: none")
        self.btn_tevoked3.setText("")
        icon11 = QtGui.QIcon()
        icon11.addPixmap(QtGui.QPixmap("visual_comp/button_evoked3.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_tevoked3.setIcon(icon11)
        self.btn_tevoked3.setIconSize(QtCore.QSize(165, 47))
        self.btn_tevoked3.setObjectName("btn_tevoked3")
        self.btn_traindata = QtWidgets.QPushButton(self.evoked)
        self.btn_traindata.setGeometry(QtCore.QRect(738, 257, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_traindata.setFont(font)
        self.btn_traindata.setStyleSheet("color: rgb(0, 230, 204);\n"
"border: none;")
        self.btn_traindata.setObjectName("btn_traindata")
        self.out_evoked = QtWidgets.QFrame(self.evoked)
        self.out_evoked.setGeometry(QtCore.QRect(0, 348, 874, 433))
        self.out_evoked.setStyleSheet("background-color: rgb(29, 52, 70);\n"
"border-radius: 40;")
        self.out_evoked.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.out_evoked.setFrameShadow(QtWidgets.QFrame.Raised)
        self.out_evoked.setObjectName("out_evoked")
        self.stackedMain.addWidget(self.evoked)
        self.side_menu = QtWidgets.QFrame(self.main)
        self.side_menu.setGeometry(QtCore.QRect(0, 0, 461, 891))
        self.side_menu.setStyleSheet("border: none;")
        self.side_menu.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.side_menu.setFrameShadow(QtWidgets.QFrame.Raised)
        self.side_menu.setObjectName("side_menu")
        self.circle_1 = QtWidgets.QLabel(self.side_menu)
        self.circle_1.setGeometry(QtCore.QRect(57, 211, 9, 9))
        self.circle_1.setText("")
        self.circle_1.setPixmap(QtGui.QPixmap("visual_comp/filled_circle.png"))
        self.circle_1.setObjectName("circle_1")
        self.logo_2 = QtWidgets.QLabel(self.side_menu)
        self.logo_2.setGeometry(QtCore.QRect(56, 60, 256, 42))
        self.logo_2.setText("")
        self.logo_2.setPixmap(QtGui.QPixmap("visual_comp/dataanal-logo.png"))
        self.logo_2.setObjectName("logo_2")
        self.circle_4 = QtWidgets.QLabel(self.side_menu)
        self.circle_4.setGeometry(QtCore.QRect(57, 417, 15, 15))
        self.circle_4.setText("")
        self.circle_4.setPixmap(QtGui.QPixmap("visual_comp/blank_circle.png"))
        self.circle_4.setObjectName("circle_4")
        self.circle_2 = QtWidgets.QLabel(self.side_menu)
        self.circle_2.setGeometry(QtCore.QRect(57, 264, 9, 9))
        self.circle_2.setText("")
        self.circle_2.setPixmap(QtGui.QPixmap("visual_comp/blank_circle.png"))
        self.circle_2.setObjectName("circle_2")
        self.circle_5 = QtWidgets.QLabel(self.side_menu)
        self.circle_5.setGeometry(QtCore.QRect(57, 364, 16, 16))
        self.circle_5.setText("")
        self.circle_5.setPixmap(QtGui.QPixmap("visual_comp/blank_circle.png"))
        self.circle_5.setObjectName("circle_5")
        self.circle_3 = QtWidgets.QLabel(self.side_menu)
        self.circle_3.setGeometry(QtCore.QRect(57, 313, 15, 15))
        self.circle_3.setText("")
        self.circle_3.setPixmap(QtGui.QPixmap("visual_comp/blank_circle.png"))
        self.circle_3.setObjectName("circle_3")
        self.circle_6 = QtWidgets.QLabel(self.side_menu)
        self.circle_6.setGeometry(QtCore.QRect(57, 469, 15, 15))
        self.circle_6.setText("")
        self.circle_6.setPixmap(QtGui.QPixmap("visual_comp/blank_circle.png"))
        self.circle_6.setObjectName("circle_6")
        self.circle_7 = QtWidgets.QLabel(self.side_menu)
        self.circle_7.setGeometry(QtCore.QRect(57, 520, 15, 15))
        self.circle_7.setText("")
        self.circle_7.setPixmap(QtGui.QPixmap("visual_comp/blank_circle.png"))
        self.circle_7.setObjectName("circle_7")
        self.btn_choosedataset = QtWidgets.QPushButton(self.side_menu)
        self.btn_choosedataset.setGeometry(QtCore.QRect(60, 670, 241, 47))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_choosedataset.setFont(font)
        self.btn_choosedataset.setStyleSheet("QPushButton {\n"
"border: 2px solid ;\n"
"border-color: white;\n"
"color: white;\n"
"border-radius: 10px;\n"
"transition: 0.3s;\n"
"}\n"
"QPushButton:hover {\n"
"border: none;\n"
"background-color: white;\n"
"border-color: white;\n"
"color: rgb(12, 22, 29);\n"
"border-radius: 10px;\n"
"}")
        self.btn_choosedataset.setIconSize(QtCore.QSize(281, 47))
        self.btn_choosedataset.setObjectName("btn_choosedataset")
        self.btn_menu1 = QtWidgets.QPushButton(self.side_menu)
        self.btn_menu1.setGeometry(QtCore.QRect(70, 205, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.btn_menu1.setFont(font)
        self.btn_menu1.setStyleSheet("QPushButton {color: rgb(255, 255, 255);\n"
"border: none;\n"
"text-align: right;\n"
"cursor: pointer; \n"
"}\n"
"\n"
"QPushButton:hover { \n"
"cursor: pointer; \n"
"}")
        self.btn_menu1.setCheckable(False)
        self.btn_menu1.setObjectName("btn_menu1")
        self.btn_menu2 = QtWidgets.QPushButton(self.side_menu)
        self.btn_menu2.setGeometry(QtCore.QRect(80, 258, 111, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_menu2.setFont(font)
        self.btn_menu2.setStyleSheet("color: rgb(125, 135, 141);\n"
"border: none;\n"
"text-align: left")
        self.btn_menu2.setCheckable(False)
        self.btn_menu2.setObjectName("btn_menu2")
        self.btn_menu3 = QtWidgets.QPushButton(self.side_menu)
        self.btn_menu3.setGeometry(QtCore.QRect(80, 309, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_menu3.setFont(font)
        self.btn_menu3.setStyleSheet("color: rgb(125, 135, 141);\n"
"border: none;\n"
"text-align: left")
        self.btn_menu3.setCheckable(False)
        self.btn_menu3.setObjectName("btn_menu3")
        self.btn_menu4 = QtWidgets.QPushButton(self.side_menu)
        self.btn_menu4.setGeometry(QtCore.QRect(80, 361, 121, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_menu4.setFont(font)
        self.btn_menu4.setStyleSheet("color: rgb(125, 135, 141);\n"
"border: none;\n"
"text-align: left")
        self.btn_menu4.setCheckable(False)
        self.btn_menu4.setObjectName("btn_menu4")
        self.btn_menu5 = QtWidgets.QPushButton(self.side_menu)
        self.btn_menu5.setGeometry(QtCore.QRect(80, 413, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_menu5.setFont(font)
        self.btn_menu5.setStyleSheet("color: rgb(125, 135, 141);\n"
"border: none;\n"
"text-align: left")
        self.btn_menu5.setCheckable(False)
        self.btn_menu5.setObjectName("btn_menu5")
        self.btn_menu6 = QtWidgets.QPushButton(self.side_menu)
        self.btn_menu6.setGeometry(QtCore.QRect(80, 465, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_menu6.setFont(font)
        self.btn_menu6.setStyleSheet("color: rgb(125, 135, 141);\n"
"border: none;\n"
"text-align: left")
        self.btn_menu6.setCheckable(False)
        self.btn_menu6.setObjectName("btn_menu6")
        self.btn_menu7 = QtWidgets.QPushButton(self.side_menu)
        self.btn_menu7.setGeometry(QtCore.QRect(80, 517, 221, 21))
        font = QtGui.QFont()
        font.setFamily("Roboto")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.btn_menu7.setFont(font)
        self.btn_menu7.setStyleSheet("color: rgb(125, 135, 141);\n"
"border: none;\n"
"text-align: left")
        self.btn_menu7.setCheckable(False)
        self.btn_menu7.setObjectName("btn_menu7")
        self.stackedWelcome.addWidget(self.main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWelcome.setCurrentIndex(0)
        self.stackedMain.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.welcome_bold.setText(_translate("MainWindow", "Welcome!"))
        self.welcome_desc.setText(_translate("MainWindow", "The brain data analyzer is a UI for MNE Python framework for analyzing brain signal datasets. It uses an interactive interface to reduce the complexity of working with BCI data\n"
"Start with uploading your own dataset or choose a sample dataset from MNE library. "))
        self.btn_upload.setText(_translate("MainWindow", "Upload a dataset"))
        self.note.setText(_translate("MainWindow", "Supported types: .vhdr, .edf, .bdf, .gdf, .cnt, .egi, .mff, .mat"))
        self.label_2.setText(_translate("MainWindow", "or"))
        self.combo_box.setItemText(0, _translate("MainWindow", "Sample (.fif)"))
        self.combo_box.setItemText(1, _translate("MainWindow", "Brainstorm (.ds)"))
        self.combo_box.setItemText(2, _translate("MainWindow", "SSVEP (.vhdr)"))
        self.btn_sample.setText(_translate("MainWindow", "Select"))
        self.description.setText(_translate("MainWindow", "The first step allows to view the information about the raw data in textual and visual format."))
        self.step.setText(_translate("MainWindow", "RAW DATA"))
        self.btn_preprocess.setText(_translate("MainWindow", "Preprocessing"))
        self.out_console.setText(_translate("MainWindow", "Helloo darkness"))
        self.menu_8.setText(_translate("MainWindow", "PREPROCESSING"))
        self.label_6.setText(_translate("MainWindow", "We preprocess our data to make it more suitable for training and obtaining the best results. Here we clean up our data by performing independent components analysis (ICA). We exclude unneeded parameters and apply the ICA. "))
        self.btn_detectevents.setText(_translate("MainWindow", "Detect events"))
        self.menu_9.setText(_translate("MainWindow", "EVENTS"))
        self.label_7.setText(_translate("MainWindow", "We detect events in order to take relevant segments from the data to reduce learning time. The resulting events array is an ordinary 3-column NumPy array, with sample number in the first column and integer event ID in the last column; the middle column is usually ignored. Press “Plot events” to visualize the distribution of events across the duration of the recording (to make sure event detection worked as expected)"))
        self.btn_epoch.setText(_translate("MainWindow", "Epoch"))
        self.menu_10.setText(_translate("MainWindow", "EPOCH DATA"))
        self.label_11.setText(_translate("MainWindow", "An epoch indicates the number of passes of the entire training dataset the machine learning algorithm has completed. In this step, we reject any epoch where peak-to-peak signal amplitude is beyond reasonable limits for that channel type. “Image map” shows each epoch as one row of an image map, with color representing signal magnitude; the average evoked response and the sensor location.\n"
""))
        self.btn_tfa.setText(_translate("MainWindow", "Time-frequency analysis"))
        self.description_tfa.setText(_translate("MainWindow", "Here we compute for the auditory epochs the induced power at different frequencies and times, using Morlet wavelets"))
        self.label_tfa.setText(_translate("MainWindow", "TIME-FREQUENCY ANALYSIS"))
        self.btn_evoked.setText(_translate("MainWindow", "Estimate evoked responses"))
        self.description_evoked.setText(_translate("MainWindow", "Evoked potentials (EPs) are neural responses time-locked to some stimulus. We can get an estimate of evoked responses to auditory versus visual stimuli by averaging together the epochs in each condition. We can plot scalp topographies at  arbitrary times. Evoked objects can also be combined to show contrasts between conditions. A simple difference can be generated by passing weights=[1, -1].\n"
""))
        self.label_evoked.setText(_translate("MainWindow", "ESTIMATE EVOKED RESPONSES"))
        self.btn_traindata.setText(_translate("MainWindow", "Train data"))
        self.btn_choosedataset.setText(_translate("MainWindow", "Choose another dataset"))
        self.btn_menu1.setText(_translate("MainWindow", "Raw data"))
        self.btn_menu2.setText(_translate("MainWindow", "Preprocess"))
        self.btn_menu3.setText(_translate("MainWindow", "Detect events"))
        self.btn_menu4.setText(_translate("MainWindow", "Epoch"))
        self.btn_menu5.setText(_translate("MainWindow", "Time-frequency analysis"))
        self.btn_menu6.setText(_translate("MainWindow", "Estimate evoked"))
        self.btn_menu7.setText(_translate("MainWindow", "Train data"))
