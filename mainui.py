from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLineEdit, QListWidget,
    QListWidgetItem, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTabWidget, QVBoxLayout, QWidget)
import os

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(794, 501)
        basedir = os.path.dirname(__file__)
        icon = QIcon(os.path.join(basedir, 'icons', 'alticon-adb-fm.png'))
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.back_btn = QPushButton(self.centralwidget)
        self.back_btn.setObjectName(u"back_btn")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.back_btn.sizePolicy().hasHeightForWidth())
        self.back_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.back_btn)

        self.forward_btn = QPushButton(self.centralwidget)
        self.forward_btn.setObjectName(u"forward_btn")
        sizePolicy.setHeightForWidth(self.forward_btn.sizePolicy().hasHeightForWidth())
        self.forward_btn.setSizePolicy(sizePolicy)

        self.horizontalLayout.addWidget(self.forward_btn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.currentloc_lineedit = QLineEdit(self.centralwidget)
        self.currentloc_lineedit.setObjectName(u"currentloc_lineedit")

        self.horizontalLayout.addWidget(self.currentloc_lineedit)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.newfolder_btn = QPushButton(self.centralwidget)
        self.newfolder_btn.setObjectName(u"newfolder_btn")

        self.horizontalLayout.addWidget(self.newfolder_btn)

        self.copy_btn = QPushButton(self.centralwidget)
        self.copy_btn.setObjectName(u"copy_btn")

        self.horizontalLayout.addWidget(self.copy_btn)

        self.cut_btn = QPushButton(self.centralwidget)
        self.cut_btn.setObjectName(u"cut_btn")

        self.horizontalLayout.addWidget(self.cut_btn)

        self.delete_btn = QPushButton(self.centralwidget)
        self.delete_btn.setObjectName(u"delete_btn")

        self.horizontalLayout.addWidget(self.delete_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setTabPosition(QTabWidget.West)
        self.computer_tab = QWidget()
        self.computer_tab.setObjectName(u"computer_tab")
        self.horizontalLayout_2 = QHBoxLayout(self.computer_tab)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.computer_list = QListWidget(self.computer_tab)
        self.computer_list.setObjectName(u"computer_list")

        self.horizontalLayout_2.addWidget(self.computer_list)

        self.tabWidget.addTab(self.computer_tab, "")
        self.adbdevice_tab = QWidget()
        self.adbdevice_tab.setObjectName(u"adbdevice_tab")
        self.horizontalLayout_3 = QHBoxLayout(self.adbdevice_tab)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.adb_list = QListWidget(self.adbdevice_tab)
        self.adb_list.setObjectName(u"adb_list")

        self.horizontalLayout_3.addWidget(self.adb_list)

        self.tabWidget.addTab(self.adbdevice_tab, "")

        self.verticalLayout.addWidget(self.tabWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ADB File Manager", None))
        self.back_btn.setText(QCoreApplication.translate("MainWindow", u"<", None))
        self.forward_btn.setText(QCoreApplication.translate("MainWindow", u">", None))
        self.newfolder_btn.setText(QCoreApplication.translate("MainWindow", u"New Folder", None))
        self.copy_btn.setText(QCoreApplication.translate("MainWindow", u"Copy", None))
        self.cut_btn.setText(QCoreApplication.translate("MainWindow", u"Cut", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.computer_tab), QCoreApplication.translate("MainWindow", u"Computer", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.adbdevice_tab), QCoreApplication.translate("MainWindow", u"ADB Device", None))
    # retranslateUi

