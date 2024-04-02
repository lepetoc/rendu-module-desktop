from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtWidgets import QApplication, QTableView, QMainWindow
from PySide6.QtCore import QSortFilterProxyModel
from ui_mainwindow import Ui_MainWindow
from controller import Controller
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
        
        query = QSqlQuery()

        model = QSqlTableModel()
        model.setTable("products")
        model.setEditStrategy(QSqlTableModel.OnFieldChange)  # Or OnRowChange, OnManualSubmit
        model.select()
        proxyModel = QSortFilterProxyModel(self)
        proxyModel.setSourceModel(model)
        
        self.ui.tableView_products.setModel(proxyModel)
        self.ui.tableView_products.setSelectionBehavior(QTableView.SelectRows)
        self.ui.tableView_products.setAlternatingRowColors(True)
        self.ui.tableView_products.resizeColumnsToContents()
        self.ui.tableView_products.setSortingEnabled(True)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    controller = Controller()
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