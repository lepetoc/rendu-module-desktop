# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.6.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QMainWindow,
    QMenu, QMenuBar, QSizePolicy, QStatusBar,
    QTabWidget, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(646, 484)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionProduct = QAction(MainWindow)
        self.actionProduct.setObjectName(u"actionProduct")
        self.actionSupplier = QAction(MainWindow)
        self.actionSupplier.setObjectName(u"actionSupplier")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tab_products = QWidget()
        self.tab_products.setObjectName(u"tab_products")
        self.gridLayout_2 = QGridLayout(self.tab_products)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.tableView_products = QTableView(self.tab_products)
        self.tableView_products.setObjectName(u"tableView_products")

        self.gridLayout_2.addWidget(self.tableView_products, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_products, "")
        self.tab_stock = QWidget()
        self.tab_stock.setObjectName(u"tab_stock")
        self.gridLayout_3 = QGridLayout(self.tab_stock)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableView_stock = QTableView(self.tab_stock)
        self.tableView_stock.setObjectName(u"tableView_stock")

        self.gridLayout_3.addWidget(self.tableView_stock, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_stock, "")
        self.tab_suppliers = QWidget()
        self.tab_suppliers.setObjectName(u"tab_suppliers")
        self.gridLayout_4 = QGridLayout(self.tab_suppliers)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableView_suppliers = QTableView(self.tab_suppliers)
        self.tableView_suppliers.setObjectName(u"tableView_suppliers")

        self.gridLayout_4.addWidget(self.tableView_suppliers, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_suppliers, "")
        self.tab_sales = QWidget()
        self.tab_sales.setObjectName(u"tab_sales")
        self.gridLayout_5 = QGridLayout(self.tab_sales)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tabWidget.addTab(self.tab_sales, "")
        self.tab_purchases = QWidget()
        self.tab_purchases.setObjectName(u"tab_purchases")
        self.gridLayout_6 = QGridLayout(self.tab_purchases)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tabWidget.addTab(self.tab_purchases, "")
        self.tab_history = QWidget()
        self.tab_history.setObjectName(u"tab_history")
        self.tabWidget.addTab(self.tab_history, "")

        self.gridLayout.addWidget(self.tabWidget, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 646, 22))
        self.menuFichier = QMenu(self.menubar)
        self.menuFichier.setObjectName(u"menuFichier")
        self.menuAdd = QMenu(self.menuFichier)
        self.menuAdd.setObjectName(u"menuAdd")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menuFichier.addAction(self.menuAdd.menuAction())
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuit)
        self.menuAdd.addAction(self.actionProduct)
        self.menuAdd.addAction(self.actionSupplier)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionProduct.setText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.actionSupplier.setText(QCoreApplication.translate("MainWindow", u"Supplier", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_products), QCoreApplication.translate("MainWindow", u"Products", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stock), QCoreApplication.translate("MainWindow", u"Stock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_suppliers), QCoreApplication.translate("MainWindow", u"Suppliers", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sales), QCoreApplication.translate("MainWindow", u"Sales", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_purchases), QCoreApplication.translate("MainWindow", u"Purchases", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_history), QCoreApplication.translate("MainWindow", u"History", None))
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"Fichier", None))
        self.menuAdd.setTitle(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

