import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QLabel, QWidget, QGridLayout, QLineEdit, QPushButton, QComboBox, \
    QMainWindow, QTableWidget
from datetime import datetime
from PyQt6.QtGui import QAction


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

        self.table = QTableWidget()
        self.table.setColumnCount(4)
        self.table.setHorizontalHeaderLabels(("id", "Name", "Course", "Mobile"))
        self.setCentralWidget(self.table)
    def load_data(self):
        pass


app = QApplication(sys.argv)
age_calculator = MainWindow()
age_calculator.show()
sys.exit(app.exec())
