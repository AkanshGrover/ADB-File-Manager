from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QHBoxLayout, QLabel, QLineEdit, QSizePolicy,
    QVBoxLayout, QWidget)
import os

class Ui_Wadb_Dialog(object):
    def setupUi(self, Wadb_Dialog):
        if not Wadb_Dialog.objectName():
            Wadb_Dialog.setObjectName(u"Wadb_Dialog")
        Wadb_Dialog.resize(400, 102)
        basedir = os.path.dirname(__file__)
        icon = QIcon(os.path.join(basedir, 'icons', 'alticon-adb-fm.png'))
        Wadb_Dialog.setWindowIcon(icon)
        Wadb_Dialog.setMaximumSize(QSize(800, 150))
        self.horizontalLayout_2 = QHBoxLayout(Wadb_Dialog)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Wadb_Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.label_2 = QLabel(Wadb_Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.ipa_input = QLineEdit(Wadb_Dialog)
        self.ipa_input.setObjectName(u"ipa_input")

        self.verticalLayout_2.addWidget(self.ipa_input)

        self.pin_input = QLineEdit(Wadb_Dialog)
        self.pin_input.setObjectName(u"pin_input")

        self.verticalLayout_2.addWidget(self.pin_input)


        self.horizontalLayout.addLayout(self.verticalLayout_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout)

        self.buttonBox = QDialogButtonBox(Wadb_Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(True)

        self.verticalLayout_3.addWidget(self.buttonBox)


        self.horizontalLayout_2.addLayout(self.verticalLayout_3)


        self.retranslateUi(Wadb_Dialog)
        self.buttonBox.accepted.connect(Wadb_Dialog.accept)
        self.buttonBox.rejected.connect(Wadb_Dialog.reject)

        QMetaObject.connectSlotsByName(Wadb_Dialog)
    # setupUi

    def retranslateUi(self, Wadb_Dialog):
        Wadb_Dialog.setWindowTitle(QCoreApplication.translate("Wadb_Dialog", u"ADB File Manager", None))
        self.label.setText(QCoreApplication.translate("Wadb_Dialog", u"Enter IP address and port: ", None))
        self.label_2.setText(QCoreApplication.translate("Wadb_Dialog", u"Enter pairing code: ", None))
    # retranslateUi

