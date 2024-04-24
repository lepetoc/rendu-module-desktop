# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sale_dialog.ui'
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

class Ui_SaleDialog(object):
    def setupUi(self, SaleDialog):
        if not SaleDialog.objectName():
            SaleDialog.setObjectName(u"SaleDialog")
        SaleDialog.resize(705, 137)
        self.gridLayout = QGridLayout(SaleDialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.buttonBox = QDialogButtonBox(SaleDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Vertical)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.buttonBox, 0, 1, 1, 1)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(SaleDialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(SaleDialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(SaleDialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.edit_product = QLineEdit(SaleDialog)
        self.edit_product.setObjectName(u"edit_product")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edit_product)

        self.edit_quantity = QLineEdit(SaleDialog)
        self.edit_quantity.setObjectName(u"edit_quantity")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edit_quantity)

        self.edit_date = QDateEdit(SaleDialog)
        self.edit_date.setObjectName(u"edit_date")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.edit_date)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)


        self.retranslateUi(SaleDialog)
        self.buttonBox.accepted.connect(SaleDialog.accept)
        self.buttonBox.rejected.connect(SaleDialog.reject)

        QMetaObject.connectSlotsByName(SaleDialog)
    # setupUi

    def retranslateUi(self, SaleDialog):
        SaleDialog.setWindowTitle(QCoreApplication.translate("SaleDialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("SaleDialog", u"Product id", None))
        self.label_2.setText(QCoreApplication.translate("SaleDialog", u"Quantity", None))
        self.label_3.setText(QCoreApplication.translate("SaleDialog", u"Date", None))
    # retranslateUi

