import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox, \
    QMainWindow, QTableWidget,QTableWidgetItem
from datetime import datetime
from PyQt6.QtGui import QAction
import sqlite3


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Student Management System")

        # Add dropdown windows
        file_menu_item = self.menuBar().addMenu("&File")
        help_menu_item = self.menuBar().addMenu("&Help")

        # Add file dropdown options
        add_student_action = QAction("Add Student", self)
        file_menu_item.addAction(add_student_action)

        # Add help dropdown and options
        about_action = QAction("About", self)
        help_menu_item.addAction(about_action)
        # only for mac if help does not show
        # about_action.setMenuRole(QAction.MenuRole.NoRole)

        # insert table with SQL data
        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("id", "Name", "Course", "Mobile"))
        self.table.verticalHeader().setVisible(False)
        self.setCentralWidget(self.table)

    def load_data(self):
        connection = sqlite3.connect("database.db")
        result = list(connection.execute("SELECT * FROM students"))
        self.table.setRowCount(0)
        for index , student in enumerate(result):
            self.table.insertRow(index)
            for column, data in enumerate(student):
                self.table.setItem(index, column, QTableWidgetItem(str(data)))
        connection.close()


app = QApplication(sys.argv)
age_calculator = MainWindow()
age_calculator.show()
age_calculator.load_data()
sys.exit(app.exec())
