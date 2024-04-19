from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtWidgets import QApplication, QTableView, QMainWindow, QDialog
from PySide6.QtCore import QSortFilterProxyModel
from ui_mainwindow import Ui_MainWindow
from ui_product_dialog import Ui_Dialog
from model import Model
import sys

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

        self.ui.actionProduct.triggered.connect(self.openProductDialog)

        model_products = QSqlTableModel()
        model_products.setTable("products")
        model_products.setEditStrategy(QSqlTableModel.OnFieldChange)  # Or OnRowChange, OnManualSubmit
        model_products.select()
        proxy_model_products = QSortFilterProxyModel(self)
        proxy_model_products.setSourceModel(model_products)
        
        self.ui.tableView_products.setModel(proxy_model_products)
        self.ui.tableView_products.setSelectionBehavior(QTableView.SelectRows)
        self.ui.tableView_products.setAlternatingRowColors(True)
        self.ui.tableView_products.resizeColumnsToContents()
        self.ui.tableView_products.setSortingEnabled(True)
    
    def openProductDialog(self):
        self.dialog = QDialog()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self.dialog)
        self.dialog.show()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Model()
    window = MainWindow()
    window.show()

    sys.exit(app.exec())

# # Customize model headers (optional)
# # model.setHeaderData(0, Qt.Horizontal, "Column 1 Name")
# # model.setHeaderData(1, Qt.Horizontal, "Column 2 Name")
# # Add more columns as needed

# view = QTableView()
# view.setModel(model)

# # Optional: Adjust settings for better user experience
# view.setSelectionBehavior(QTableView.SelectRows)
# view.setAlternatingRowColors(True)
# view.resizeColumnsToContents()