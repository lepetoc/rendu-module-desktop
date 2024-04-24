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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QSizePolicy,
    QStatusBar, QTabWidget, QTableView, QTableWidget,
    QTableWidgetItem, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(838, 651)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actionProduct = QAction(MainWindow)
        self.actionProduct.setObjectName(u"actionProduct")
        self.actionSupplier = QAction(MainWindow)
        self.actionSupplier.setObjectName(u"actionSupplier")
        self.actionSale = QAction(MainWindow)
        self.actionSale.setObjectName(u"actionSale")
        self.actionPurchase = QAction(MainWindow)
        self.actionPurchase.setObjectName(u"actionPurchase")
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

        self.gridLayout_2.addWidget(self.tableView_products, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_products, "")
        self.tab_stock = QWidget()
        self.tab_stock.setObjectName(u"tab_stock")
        self.gridLayout_3 = QGridLayout(self.tab_stock)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.tableWidget_stock = QTableWidget(self.tab_stock)
        self.tableWidget_stock.setObjectName(u"tableWidget_stock")

        self.gridLayout_3.addWidget(self.tableWidget_stock, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_stock, "")
        self.tab_suppliers = QWidget()
        self.tab_suppliers.setObjectName(u"tab_suppliers")
        self.gridLayout_4 = QGridLayout(self.tab_suppliers)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tableView_suppliers = QTableView(self.tab_suppliers)
        self.tableView_suppliers.setObjectName(u"tableView_suppliers")

        self.gridLayout_4.addWidget(self.tableView_suppliers, 1, 0, 1, 1)

        self.tabWidget.addTab(self.tab_suppliers, "")
        self.tab_sales = QWidget()
        self.tab_sales.setObjectName(u"tab_sales")
        self.gridLayout_5 = QGridLayout(self.tab_sales)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.tableView_sales = QTableView(self.tab_sales)
        self.tableView_sales.setObjectName(u"tableView_sales")

        self.gridLayout_5.addWidget(self.tableView_sales, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_sales, "")
        self.tab_purchases = QWidget()
        self.tab_purchases.setObjectName(u"tab_purchases")
        self.gridLayout_6 = QGridLayout(self.tab_purchases)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.tableView_purchases = QTableView(self.tab_purchases)
        self.tableView_purchases.setObjectName(u"tableView_purchases")

        self.gridLayout_6.addWidget(self.tableView_purchases, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_purchases, "")
        self.tab_history = QWidget()
        self.tab_history.setObjectName(u"tab_history")
        self.gridLayout_7 = QGridLayout(self.tab_history)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.tableWidget_history = QTableWidget(self.tab_history)
        self.tableWidget_history.setObjectName(u"tableWidget_history")

        self.gridLayout_7.addWidget(self.tableWidget_history, 0, 0, 1, 1)

        self.tabWidget.addTab(self.tab_history, "")

        self.gridLayout.addWidget(self.tabWidget, 1, 0, 1, 1)

        self.edit_filter = QLineEdit(self.centralwidget)
        self.edit_filter.setObjectName(u"edit_filter")

        self.gridLayout.addWidget(self.edit_filter, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 838, 22))
        self.menuFichier = QMenu(self.menubar)
        self.menuFichier.setObjectName(u"menuFichier")
        self.menuAdd = QMenu(self.menuFichier)
        self.menuAdd.setObjectName(u"menuAdd")
        self.menuNew = QMenu(self.menuFichier)
        self.menuNew.setObjectName(u"menuNew")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuFichier.menuAction())
        self.menuFichier.addAction(self.menuAdd.menuAction())
        self.menuFichier.addAction(self.menuNew.menuAction())
        self.menuFichier.addAction(self.actionQuit)
        self.menuAdd.addAction(self.actionProduct)
        self.menuAdd.addAction(self.actionSupplier)
        self.menuNew.addAction(self.actionSale)
        self.menuNew.addAction(self.actionPurchase)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(5)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.actionProduct.setText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.actionSupplier.setText(QCoreApplication.translate("MainWindow", u"Supplier", None))
        self.actionSale.setText(QCoreApplication.translate("MainWindow", u"Sale", None))
        self.actionPurchase.setText(QCoreApplication.translate("MainWindow", u"Purchase", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_products), QCoreApplication.translate("MainWindow", u"Products", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_stock), QCoreApplication.translate("MainWindow", u"Stock", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_suppliers), QCoreApplication.translate("MainWindow", u"Suppliers", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_sales), QCoreApplication.translate("MainWindow", u"Sales", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_purchases), QCoreApplication.translate("MainWindow", u"Purchases", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_history), QCoreApplication.translate("MainWindow", u"History", None))
        self.menuFichier.setTitle(QCoreApplication.translate("MainWindow", u"Files", None))
        self.menuAdd.setTitle(QCoreApplication.translate("MainWindow", u"Add", None))
        self.menuNew.setTitle(QCoreApplication.translate("MainWindow", u"New", None))
    # retranslateUi

