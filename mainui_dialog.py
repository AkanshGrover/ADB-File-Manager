from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QHBoxLayout, QLabel,
    QListWidget, QListWidgetItem, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(311, 436)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ndevices_label = QLabel(Dialog)
        self.ndevices_label.setObjectName(u"ndevices_label")
        font = QFont()
        font.setBold(True)
        self.ndevices_label.setFont(font)
        self.ndevices_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.ndevices_label)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label1 = QLabel(Dialog)
        self.label1.setObjectName(u"label1")

        self.horizontalLayout.addWidget(self.label1)

        self.refresh_btn = QPushButton(Dialog)
        self.refresh_btn.setObjectName(u"refresh_btn")

        self.horizontalLayout.addWidget(self.refresh_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.devices_list = QListWidget(Dialog)
        self.devices_list.setObjectName(u"devices_list")

        self.verticalLayout.addWidget(self.devices_list)

        self.exit_app_btn = QPushButton(Dialog)
        self.exit_app_btn.setObjectName(u"exit_app_btn")

        self.verticalLayout.addWidget(self.exit_app_btn)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"ADB File Manager", None))
        self.ndevices_label.setText(QCoreApplication.translate("Dialog", u"devices connected", None))
        self.label1.setText(QCoreApplication.translate("Dialog", u"Please select one device from the list below:", None))
        self.refresh_btn.setText(QCoreApplication.translate("Dialog", u"Refresh", None))
        self.exit_app_btn.setText(QCoreApplication.translate("Dialog", u"Exit app", None))
    # retranslateUi

