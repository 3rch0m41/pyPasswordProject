# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.11.2
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QStatusBar, QTabWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(744, 420)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabEvaluate = QWidget()
        self.tabEvaluate.setObjectName(u"tabEvaluate")
        self.vlayEvaluate = QVBoxLayout(self.tabEvaluate)
        self.vlayEvaluate.setObjectName(u"vlayEvaluate")
        self.hlayPasswordInput = QHBoxLayout()
        self.hlayPasswordInput.setObjectName(u"hlayPasswordInput")
        self.lblEvaluatePassword = QLabel(self.tabEvaluate)
        self.lblEvaluatePassword.setObjectName(u"lblEvaluatePassword")

        self.hlayPasswordInput.addWidget(self.lblEvaluatePassword)

        self.txtPasswordEvaluate = QLineEdit(self.tabEvaluate)
        self.txtPasswordEvaluate.setObjectName(u"txtPasswordEvaluate")
        self.txtPasswordEvaluate.setEchoMode(QLineEdit.EchoMode.Password)

        self.hlayPasswordInput.addWidget(self.txtPasswordEvaluate)


        self.vlayEvaluate.addLayout(self.hlayPasswordInput)

        self.hlayEvaluateButton = QHBoxLayout()
        self.hlayEvaluateButton.setObjectName(u"hlayEvaluateButton")
        self.spcEvaluateLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hlayEvaluateButton.addItem(self.spcEvaluateLeft)

        self.btnEvaluate = QPushButton(self.tabEvaluate)
        self.btnEvaluate.setObjectName(u"btnEvaluate")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnEvaluate.sizePolicy().hasHeightForWidth())
        self.btnEvaluate.setSizePolicy(sizePolicy)

        self.hlayEvaluateButton.addWidget(self.btnEvaluate)

        self.spcEvaluateRight = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hlayEvaluateButton.addItem(self.spcEvaluateRight)


        self.vlayEvaluate.addLayout(self.hlayEvaluateButton)

        self.pbarEvaluationBar = QProgressBar(self.tabEvaluate)
        self.pbarEvaluationBar.setObjectName(u"pbarEvaluationBar")
        self.pbarEvaluationBar.setMaximum(8)
        self.pbarEvaluationBar.setValue(0)
        self.pbarEvaluationBar.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.vlayEvaluate.addWidget(self.pbarEvaluationBar)

        self.lblEvaluationResult = QLabel(self.tabEvaluate)
        self.lblEvaluationResult.setObjectName(u"lblEvaluationResult")
        self.lblEvaluationResult.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lblEvaluationResult.setWordWrap(True)

        self.vlayEvaluate.addWidget(self.lblEvaluationResult)

        self.spcEvaluateBottom = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.vlayEvaluate.addItem(self.spcEvaluateBottom)

        self.tabWidget.addTab(self.tabEvaluate, "")
        self.tabGenerate = QWidget()
        self.tabGenerate.setObjectName(u"tabGenerate")
        self.vlayGenerate = QVBoxLayout(self.tabGenerate)
        self.vlayGenerate.setObjectName(u"vlayGenerate")
        self.hlayLengths = QHBoxLayout()
        self.hlayLengths.setObjectName(u"hlayLengths")
        self.lblMinLen = QLabel(self.tabGenerate)
        self.lblMinLen.setObjectName(u"lblMinLen")

        self.hlayLengths.addWidget(self.lblMinLen)

        self.spbMinLen = QSpinBox(self.tabGenerate)
        self.spbMinLen.setObjectName(u"spbMinLen")
        self.spbMinLen.setMinimum(4)
        self.spbMinLen.setMaximum(128)
        self.spbMinLen.setValue(12)

        self.hlayLengths.addWidget(self.spbMinLen)

        self.lblMaxLen = QLabel(self.tabGenerate)
        self.lblMaxLen.setObjectName(u"lblMaxLen")

        self.hlayLengths.addWidget(self.lblMaxLen)

        self.spbMaxLen = QSpinBox(self.tabGenerate)
        self.spbMaxLen.setObjectName(u"spbMaxLen")
        self.spbMaxLen.setMinimum(4)
        self.spbMaxLen.setMaximum(128)
        self.spbMaxLen.setValue(20)

        self.hlayLengths.addWidget(self.spbMaxLen)

        self.lblQty = QLabel(self.tabGenerate)
        self.lblQty.setObjectName(u"lblQty")

        self.hlayLengths.addWidget(self.lblQty)

        self.spbQty = QSpinBox(self.tabGenerate)
        self.spbQty.setObjectName(u"spbQty")
        self.spbQty.setMinimum(1)
        self.spbQty.setMaximum(100)
        self.spbQty.setValue(5)

        self.hlayLengths.addWidget(self.spbQty)

        self.spcLengthsRight = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hlayLengths.addItem(self.spcLengthsRight)


        self.vlayGenerate.addLayout(self.hlayLengths)

        self.hlayCharTypes = QHBoxLayout()
        self.hlayCharTypes.setObjectName(u"hlayCharTypes")
        self.chkUpper = QCheckBox(self.tabGenerate)
        self.chkUpper.setObjectName(u"chkUpper")
        self.chkUpper.setChecked(True)

        self.hlayCharTypes.addWidget(self.chkUpper)

        self.chkLower = QCheckBox(self.tabGenerate)
        self.chkLower.setObjectName(u"chkLower")
        self.chkLower.setChecked(True)

        self.hlayCharTypes.addWidget(self.chkLower)

        self.chkDigit = QCheckBox(self.tabGenerate)
        self.chkDigit.setObjectName(u"chkDigit")
        self.chkDigit.setChecked(True)

        self.hlayCharTypes.addWidget(self.chkDigit)

        self.chkSpecial = QCheckBox(self.tabGenerate)
        self.chkSpecial.setObjectName(u"chkSpecial")
        self.chkSpecial.setChecked(True)

        self.hlayCharTypes.addWidget(self.chkSpecial)

        self.spcCharTypesRight = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hlayCharTypes.addItem(self.spcCharTypesRight)


        self.vlayGenerate.addLayout(self.hlayCharTypes)

        self.hlayGenerateButton = QHBoxLayout()
        self.hlayGenerateButton.setObjectName(u"hlayGenerateButton")
        self.spcGenerateLeft = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hlayGenerateButton.addItem(self.spcGenerateLeft)

        self.btnGenerate = QPushButton(self.tabGenerate)
        self.btnGenerate.setObjectName(u"btnGenerate")
        sizePolicy.setHeightForWidth(self.btnGenerate.sizePolicy().hasHeightForWidth())
        self.btnGenerate.setSizePolicy(sizePolicy)

        self.hlayGenerateButton.addWidget(self.btnGenerate)

        self.spcGenerateRight = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.hlayGenerateButton.addItem(self.spcGenerateRight)


        self.vlayGenerate.addLayout(self.hlayGenerateButton)

        self.tblResults = QTableWidget(self.tabGenerate)
        if (self.tblResults.columnCount() < 3):
            self.tblResults.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tblResults.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tblResults.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tblResults.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tblResults.setObjectName(u"tblResults")
        self.tblResults.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tblResults.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.tblResults.horizontalHeader().setStretchLastSection(True)
        self.tblResults.verticalHeader().setVisible(False)

        self.vlayGenerate.addWidget(self.tblResults)

        self.tabWidget.addTab(self.tabGenerate, "")

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Password Toolkit", None))
        self.lblEvaluatePassword.setText(QCoreApplication.translate("MainWindow", u"Insert here the password:", None))
        self.btnEvaluate.setText(QCoreApplication.translate("MainWindow", u"Evaluate", None))
        self.pbarEvaluationBar.setFormat(QCoreApplication.translate("MainWindow", u"%v / %m", None))
        self.lblEvaluationResult.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabEvaluate), QCoreApplication.translate("MainWindow", u"Valuta", None))
        self.lblMinLen.setText(QCoreApplication.translate("MainWindow", u"Min Length:", None))
        self.lblMaxLen.setText(QCoreApplication.translate("MainWindow", u"Max Length:", None))
        self.lblQty.setText(QCoreApplication.translate("MainWindow", u"Quantity:", None))
        self.chkUpper.setText(QCoreApplication.translate("MainWindow", u"Uppercase", None))
        self.chkLower.setText(QCoreApplication.translate("MainWindow", u"Lowercase", None))
        self.chkDigit.setText(QCoreApplication.translate("MainWindow", u"Digits", None))
        self.chkSpecial.setText(QCoreApplication.translate("MainWindow", u"Special characters", None))
        self.btnGenerate.setText(QCoreApplication.translate("MainWindow", u"Generate", None))
        ___qtablewidgetitem = self.tblResults.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        ___qtablewidgetitem1 = self.tblResults.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Score", None))
        ___qtablewidgetitem2 = self.tblResults.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Strength", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabGenerate), QCoreApplication.translate("MainWindow", u"Genera", None))
    # retranslateUi

