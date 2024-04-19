# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'product_dialog.ui'
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
    QSizePolicy, QTextEdit, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(667, 407)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.edit_product_name = QLineEdit(Dialog)
        self.edit_product_name.setObjectName(u"edit_product_name")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.edit_product_name)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.edit_product_price = QLineEdit(Dialog)
        self.edit_product_price.setObjectName(u"edit_product_price")

        self.formLayout.setWidget(3, QFormLayout.FieldRole, self.edit_product_price)

        self.edit_product_desc = QTextEdit(Dialog)
        self.edit_product_desc.setObjectName(u"edit_product_desc")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.edit_product_desc)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_4)

        self.edit_product_category = QLineEdit(Dialog)
        self.edit_product_category.setObjectName(u"edit_product_category")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.edit_product_category)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.validateButton = QDialogButtonBox(Dialog)
        self.validateButton.setObjectName(u"validateButton")
        self.validateButton.setOrientation(Qt.Vertical)
        self.validateButton.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.validateButton, 0, 1, 1, 1)


        self.retranslateUi(Dialog)
        self.validateButton.accepted.connect(Dialog.accept)
        self.validateButton.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Nom du produit", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Description du produit", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Prix du produit", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Cat\u00e9gorie(s) du produit", None))
    # retranslateUi

