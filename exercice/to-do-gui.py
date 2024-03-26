import sys
import json
from tasks_manager import tasks_manager
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from ui_main import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        file_path = 'tasks.json'
        self.manager = tasks_manager(file_path)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        for task in self.manager.tasks.values():
            self.ui.listWidget.addItem(QListWidgetItem(task))
        
        self.ui.pushButton.clicked.connect(self.add_task)
        self.ui.pushButton_2.clicked.connect(self.delete_task)
        self.ui.lineEdit.returnPressed.connect(self.add_task)
        
    def add_task(self):
        task_description = self.ui.lineEdit.text()
        if task_description:
            self.ui.listWidget.addItem(QListWidgetItem(task_description))
            self.ui.lineEdit.clear()
            self.manager.add_task(task_description)
        else:
            print("Please enter a task description.")
            
    def delete_task(self):
        key_list = list(self.manager.tasks.keys())
        val_list = list(self.manager.tasks.values())
 
        task_id = val_list.index(self.ui.listWidget.currentItem().text())
        self.ui.listWidget.takeItem(task_id)
        self.manager.delete_task(key_list[task_id])
    
if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())