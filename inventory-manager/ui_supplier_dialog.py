# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'supplier_dialog.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDialog, QDialogButtonBox,
    QFormLayout, QGridLayout, QLabel, QLineEdit,
    QSizePolicy, QWidget)

class Ui_SupplierDialog(object):
    def setupUi(self, SupplierDialog):
        if not SupplierDialog.objectName():
            SupplierDialog.setObjectName(u"SupplierDialog")
        SupplierDialog.resize(678, 96)
        self.gridLayout = QGridLayout(SupplierDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(SupplierDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 0, 1, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(SupplierDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(SupplierDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.edit_supplier_name = QLineEdit(SupplierDialog)
        self.edit_supplier_name.setObjectName(u"edit_supplier_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edit_supplier_name)

        self.edit_contact = QLineEdit(SupplierDialog)
        self.edit_contact.setObjectName(u"edit_contact")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edit_contact)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)


        self.retranslateUi(SupplierDialog)
        self.buttonBox.accepted.connect(SupplierDialog.accept)
        self.buttonBox.rejected.connect(SupplierDialog.reject)

        QMetaObject.connectSlotsByName(SupplierDialog)
    # setupUi

    def retranslateUi(self, SupplierDialog):
        SupplierDialog.setWindowTitle(QCoreApplication.translate("SupplierDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("SupplierDialog", u"Supplier name", None))
        self.label_2.setText(QCoreApplication.translate("SupplierDialog", u"Contact info", None))
    # retranslateUi

