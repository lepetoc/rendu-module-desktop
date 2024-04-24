from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtWidgets import QApplication, QTableView, QMainWindow, QDialog, QTableWidgetItem
from PySide6.QtCore import QSortFilterProxyModel
from ui_mainwindow import Ui_MainWindow
from ui_product_dialog import Ui_Dialog
from ui_supplier_dialog import Ui_SupplierDialog
from ui_purchase_dialog import Ui_PurchaseDialog
from ui_sale_dialog import Ui_SaleDialog
from model import Model
import sys

class ProductDialog(QDialog, Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.validateButton.accepted.connect(self.submit_form)
    
    def submit_form(self):
        controller.add_product((self.edit_product_name.text(),
            self.edit_product_desc.toPlainText(),
            self.edit_product_price.text(),
            self.edit_product_category.text()))
        window.model_products.select()

class SupplierDialog(QDialog, Ui_SupplierDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.submit_form)
    
    def submit_form(self):
        controller.add_supplier((
            self.edit_supplier_name.text(),
            self.edit_contact.text()
        ))
        window.model_supplier.select()

class SaleDialog(QDialog, Ui_SaleDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.submit_form)
    
    def submit_form(self):
        controller.add_sale((
            self.edit_product.text(),
            self.edit_quantity.text(),
            self.edit_date.date().toString("yyyy-MM-dd")
        ))
        window.model_sales.select()
        # window.refreshHistory()
        # window.refreshStock()

class PurchaseDialog(QDialog, Ui_PurchaseDialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.buttonBox.accepted.connect(self.submit_form)
    
    def submit_form(self):
        controller.add_purchase((
            self.edit_supplier.text(),
            self.edit_product.text(),
            self.edit_quantity.text(),
            self.edit_date.date().toString("yyyy-MM-dd"),
        ))
        window.model_purchases.select()
        # window.refreshHistory()
        # window.refreshStock()

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # Open a database connection
        db = QSqlDatabase.addDatabase("QSQLITE")
        db.setDatabaseName("inventory-manager.sqlite")
        if not db.open():
            print("Unable to open the database")
            sys.exit(-1)

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #region Set product model
        self.model_products = QSqlTableModel()
        self.model_products.setTable("products")
        self.model_products.setEditStrategy(QSqlTableModel.OnFieldChange)  # Or OnRowChange, OnManualSubmit
        self.model_products.select()
        proxy_model_products = QSortFilterProxyModel(self)
        proxy_model_products.setSourceModel(self.model_products)
        
        self.ui.tableView_products.setModel(proxy_model_products)
        self.ui.tableView_products.setSelectionBehavior(QTableView.SelectRows)
        self.ui.tableView_products.setAlternatingRowColors(True)
        self.ui.tableView_products.resizeColumnsToContents()
        self.ui.tableView_products.setSortingEnabled(True)
        #endregion

        #region Set stock model
        stock_headers = ["Product Name", "Quantity", "Stock Threshold"]
        self.ui.tableWidget_stock.setColumnCount(len(stock_headers))
        self.ui.tableWidget_stock.setHorizontalHeaderLabels(stock_headers)
        stock = controller.get_stock()
        self.ui.tableWidget_stock.setRowCount(len(stock))
        for row_index, row_data in enumerate(stock):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.ui.tableWidget_stock.setItem(row_index, col_index, item)
        #endregion
        
        #region Set supplier model
        self.model_supplier = QSqlTableModel()
        self.model_supplier.setTable("suppliers")
        self.model_supplier.setEditStrategy(QSqlTableModel.OnFieldChange)  # Or OnRowChange, OnManualSubmit
        self.model_supplier.select()
        proxy_model_supplier = QSortFilterProxyModel(self)
        proxy_model_supplier.setSourceModel(self.model_supplier)
        
        self.ui.tableView_suppliers.setModel(proxy_model_supplier)
        self.ui.tableView_suppliers.setSelectionBehavior(QTableView.SelectRows)
        self.ui.tableView_suppliers.setAlternatingRowColors(True)
        self.ui.tableView_suppliers.resizeColumnsToContents()
        self.ui.tableView_suppliers.setSortingEnabled(True)
        #endregion
        
        #region Set sales model
        self.model_sales = QSqlTableModel()
        self.model_sales.setTable("sales")
        self.model_sales.setEditStrategy(QSqlTableModel.OnFieldChange)  # Or OnRowChange, OnManualSubmit
        self.model_sales.select()
        proxy_model_sales = QSortFilterProxyModel(self)
        proxy_model_sales.setSourceModel(self.model_sales)
        
        self.ui.tableView_sales.setModel(proxy_model_sales)
        self.ui.tableView_sales.setSelectionBehavior(QTableView.SelectRows)
        self.ui.tableView_sales.setAlternatingRowColors(True)
        self.ui.tableView_sales.resizeColumnsToContents()
        self.ui.tableView_sales.setSortingEnabled(True)
        #endregion

        #region Set purchases model
        self.model_purchases = QSqlTableModel()
        self.model_purchases.setTable("purchases")
        self.model_purchases.setEditStrategy(QSqlTableModel.OnFieldChange)  # Or OnRowChange, OnManualSubmit
        self.model_purchases.select()
        proxy_model_purchases = QSortFilterProxyModel(self)
        proxy_model_purchases.setSourceModel(self.model_purchases)
        
        self.ui.tableView_purchases.setModel(proxy_model_purchases)
        self.ui.tableView_purchases.setSelectionBehavior(QTableView.SelectRows)
        self.ui.tableView_purchases.setAlternatingRowColors(True)
        self.ui.tableView_purchases.resizeColumnsToContents()
        self.ui.tableView_purchases.setSortingEnabled(True)
        #endregion

        #region Set history model
        history_headers = ["Type", "Supplier", "Product", "Quantity", "Date"]
        self.ui.tableWidget_history.setColumnCount(len(history_headers))
        self.ui.tableWidget_history.setHorizontalHeaderLabels(history_headers)
        history = controller.get_history()
        self.ui.tableWidget_history.setRowCount(len(history))
        for row_index, row_data in enumerate(history):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.ui.tableWidget_history.setItem(row_index, col_index, item)
        #endregion

        self.ui.actionProduct.triggered.connect(self.openProductDialog)
        self.ui.actionSupplier.triggered.connect(self.openSupplierDialog)
        self.ui.actionPurchase.triggered.connect(self.openPurchaseDialog)
        self.ui.actionSale.triggered.connect(self.openSaleDialog)
    
    def openProductDialog(self):
        dialog = ProductDialog()
        dialog.exec()

    def openSupplierDialog(self):
        dialog = SupplierDialog()
        dialog.exec()
    
    def openPurchaseDialog(self):
        dialog = PurchaseDialog()
        dialog.exec()

    def openSaleDialog(self):
        dialog = SaleDialog()
        dialog.exec()
    
    def refreshStock(self):
        stock_headers = ["Product Name", "Quantity", "Stock Threshold"]
        self.ui.tableWidget_stock.setColumnCount(len(stock_headers))
        self.ui.tableWidget_stock.setHorizontalHeaderLabels(stock_headers)
        stock = controller.get_stock()
        self.ui.tableWidget_stock.setRowCount(len(stock))
        for row_index, row_data in enumerate(stock):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
        self.ui.tableWidget_stock.setItem(row_index, col_index, item)
        self.ui.tableWidget_stock.clearSelection()
        self.ui.tableWidget_stock.setCurrentCell(-1, -1)
        self.ui.tableWidget_stock.setFocus()
    
    def refreshHistory(self):
        history_headers = ["Type", "Supplier", "Product", "Quantity", "Date"]
        self.ui.tableWidget_history.setColumnCount(len(history_headers))
        self.ui.tableWidget_history.setHorizontalHeaderLabels(history_headers)
        history = controller.get_history()
        self.ui.tableWidget_history.setRowCount(len(history))
        for row_index, row_data in enumerate(history):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
        self.ui.tableWidget_history.setItem(row_index, col_index, item)
        self.ui.tableWidget_history.clearSelection()
        self.ui.tableWidget_history.setCurrentCell(-1, -1)
        self.ui.tableWidget_history.setFocus()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Model()
    window = MainWindow()
    window.show()

    sys.exit(app.exec())