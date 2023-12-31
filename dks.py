# Form implementation generated from reading ui file 'devkitsetup.ui'
#
# Created by: PyQt6 UI code generator 6.4.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(785, 702)
        MainWindow.setStyleSheet("font: 14pt \"Roboto\";\n"
"background: #282a36;\n"
"color: #f8f8f2;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 771, 51))
        self.label.setStyleSheet("text-align: center;")
        self.label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label.setObjectName("label")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 100, 771, 501))
        self.tabWidget.setStyleSheet("background: #202029;")
        self.tabWidget.setObjectName("tabWidget")
        self.java_tab = QtWidgets.QWidget()
        self.java_tab.setObjectName("java_tab")
        self.gridLayoutWidget = QtWidgets.QWidget(parent=self.java_tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 771, 511))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.jdk17_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.jdk17_btn.setObjectName("jdk17_btn")
        self.gridLayout.addWidget(self.jdk17_btn, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_2.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(parent=self.gridLayoutWidget)
        self.label_3.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.jre17_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget)
        self.jre17_btn.setObjectName("jre17_btn")
        self.gridLayout.addWidget(self.jre17_btn, 1, 1, 1, 1)
        self.tabWidget.addTab(self.java_tab, "")
        self.cpp_tab = QtWidgets.QWidget()
        self.cpp_tab.setObjectName("cpp_tab")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(parent=self.cpp_tab)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 771, 471))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.clang_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        self.clang_btn.setObjectName("clang_btn")
        self.gridLayout_2.addWidget(self.clang_btn, 0, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_5.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.gridLayoutWidget_2)
        self.label_6.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.gcc_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget_2)
        self.gcc_btn.setObjectName("gcc_btn")
        self.gridLayout_2.addWidget(self.gcc_btn, 1, 1, 1, 1)
        self.tabWidget.addTab(self.cpp_tab, "")
        self.python_tab = QtWidgets.QWidget()
        self.python_tab.setObjectName("python_tab")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(parent=self.python_tab)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 771, 471))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.python3_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.python3_btn.setObjectName("python3_btn")
        self.gridLayout_3.addWidget(self.python3_btn, 0, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.label_7.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.gridLayoutWidget_3)
        self.label_8.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.pip3_btn = QtWidgets.QPushButton(parent=self.gridLayoutWidget_3)
        self.pip3_btn.setObjectName("pip3_btn")
        self.gridLayout_3.addWidget(self.pip3_btn, 1, 1, 1, 1)
        self.tabWidget.addTab(self.python_tab, "")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(-1, 60, 771, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_4 = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_4.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout.addWidget(self.label_4)
        self.comboBox = QtWidgets.QComboBox(parent=self.horizontalLayoutWidget)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout.addWidget(self.comboBox)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "DevKit Setup"))
        self.jdk17_btn.setText(_translate("MainWindow", "Установить"))
        self.label_2.setText(_translate("MainWindow", "JDK 17"))
        self.label_3.setText(_translate("MainWindow", "JRE 17"))
        self.jre17_btn.setText(_translate("MainWindow", "Установить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.java_tab), _translate("MainWindow", "Java"))
        self.clang_btn.setText(_translate("MainWindow", "Установить"))
        self.label_5.setText(_translate("MainWindow", "Компилятор CLANG"))
        self.label_6.setText(_translate("MainWindow", "Компилятор GCC"))
        self.gcc_btn.setText(_translate("MainWindow", "Установить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.cpp_tab), _translate("MainWindow", "C/C++"))
        self.python3_btn.setText(_translate("MainWindow", "Установить"))
        self.label_7.setText(_translate("MainWindow", "Python3"))
        self.label_8.setText(_translate("MainWindow", "PIP3"))
        self.pip3_btn.setText(_translate("MainWindow", "Установить"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.python_tab), _translate("MainWindow", "Python"))
        self.label_4.setText(_translate("MainWindow", "Дистрибутив Linux"))
        self.comboBox.setItemText(0, _translate("MainWindow", "Arch/Manjaro"))
        self.comboBox.setItemText(1, _translate("MainWindow", "Debian/Ubuntu"))
