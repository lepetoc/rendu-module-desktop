# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'purchase_dialog.ui'
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
from PySide6.QtWidgets import (QAbstractButton, QApplication, QDateEdit, QDialog,
    QDialogButtonBox, QFormLayout, QGridLayout, QLabel,
    QLineEdit, QSizePolicy, QWidget)

class Ui_PurchaseDialog(object):
    def setupUi(self, PurchaseDialog):
        if not PurchaseDialog.objectName():
            PurchaseDialog.setObjectName(u"PurchaseDialog")
        PurchaseDialog.resize(707, 149)
        self.gridLayout = QGridLayout(PurchaseDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(PurchaseDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 0, 1, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(PurchaseDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(PurchaseDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(PurchaseDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.label_4 = QLabel(PurchaseDialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_4)

        self.edit_date = QDateEdit(PurchaseDialog)
        self.edit_date.setObjectName(u"edit_date")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.edit_date)

        self.edit_product = QLineEdit(PurchaseDialog)
        self.edit_product.setObjectName(u"edit_product")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edit_product)

        self.edit_supplier = QLineEdit(PurchaseDialog)
        self.edit_supplier.setObjectName(u"edit_supplier")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edit_supplier)

        self.edit_quantity = QLineEdit(PurchaseDialog)
        self.edit_quantity.setObjectName(u"edit_quantity")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.edit_quantity)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)


        self.retranslateUi(PurchaseDialog)
        self.buttonBox.accepted.connect(PurchaseDialog.accept)
        self.buttonBox.rejected.connect(PurchaseDialog.reject)

        QMetaObject.connectSlotsByName(PurchaseDialog)
    # setupUi

    def retranslateUi(self, PurchaseDialog):
        PurchaseDialog.setWindowTitle(QCoreApplication.translate("PurchaseDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("PurchaseDialog", u"Product id", None))
        self.label_2.setText(QCoreApplication.translate("PurchaseDialog", u"Supplier id", None))
        self.label_3.setText(QCoreApplication.translate("PurchaseDialog", u"Quantity", None))
        self.label_4.setText(QCoreApplication.translate("PurchaseDialog", u"Date", None))
    # retranslateUi

