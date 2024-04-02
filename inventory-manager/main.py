from PySide6.QtSql import QSqlDatabase, QSqlTableModel, QSqlQuery
from PySide6.QtWidgets import QApplication, QTableView
import sys

app = QApplication(sys.argv)

# Open a database connection
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("inventory-manager.sqlite")
if not db.open():
    print("Unable to open the database")
    sys.exit(-1)

query = QSqlQuery()

model = QSqlTableModel()
model.setTable("products")
model.setEditStrategy(QSqlTableModel.OnFieldChange)  # Or OnRowChange, OnManualSubmit
model.select()

# Customize model headers (optional)
# model.setHeaderData(0, Qt.Horizontal, "Column 1 Name")
# model.setHeaderData(1, Qt.Horizontal, "Column 2 Name")
# Add more columns as needed

view = QTableView()
view.setModel(model)

# Optional: Adjust settings for better user experience
view.setSelectionBehavior(QTableView.SelectRows)
view.setAlternatingRowColors(True)
view.resizeColumnsToContents()

view.show()

sys.exit(app.exec())

