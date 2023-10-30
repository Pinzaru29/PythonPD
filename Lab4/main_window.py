import os
import sys
import pandas as pd
from PyQt6 import QtWidgets
from data_processing import get_dataFiles_ymd, get_data_yw, get_data_ymd

# Get the directory where the current script is located
script_directory = os.path.dirname(os.path.abspath(__file__))

# Set the working directory to the script's directory
os.chdir(script_directory)


class MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Data Processing Application")
        self.setGeometry(100, 100, 800, 600)

        # Create widgets
        self.date_input = QtWidgets.QLineEdit()
        self.date_input.setPlaceholderText("Enter date (YYYY-MM-DD)")
        self.date_input.setStyleSheet("font-size: 16px;")
        
        self.button_dataFiles_ymd = QtWidgets.QPushButton("Get Data Files (ymd)")
        self.button_data_yw = QtWidgets.QPushButton("Get Data Year-Week (yw)")
        self.button_data_ymd = QtWidgets.QPushButton("Get Data Year-Month-Day (ymd)")
        self.button_select_file = QtWidgets.QPushButton("Select File")

        self.button_select_file.setStyleSheet("border-radius: 16px;"
                                            "background-color: #acc7d5;"
                                            "padding: 8px;"
                                            "font-size: 14px;"
                                            "font-weight: 700;"
                                            "color: #FFFFFF;")
        self.button_dataFiles_ymd.setStyleSheet("border-radius: 16px;"
                                            "background-color: #1dcaff;"
                                            "padding: 8px;"
                                            "font-size: 14px;"
                                            "font-weight: 700;"
                                            "color: #FFFFFF;")
        self.button_data_yw.setStyleSheet("border-radius: 16px;"
                                            "background-color: #00aced;"
                                            "padding: 8px;"
                                            "font-size: 14px;"
                                            "font-weight: 700;"
                                            "color: #FFFFFF;")
        self.button_data_ymd.setStyleSheet("border-radius: 16px;"
                                            "background-color: #0084b4;"
                                            "padding: 8px;"
                                            "font-size: 14px;"
                                            "font-weight: 700;"
                                            "color: #FFFFFF;")

        # Create QTableWidget for data display
        self.data_table = QtWidgets.QTableWidget()

        # Layout
        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.date_input)
        layout.addWidget(self.button_select_file)  # Add the file selection button
        layout.addWidget(self.button_dataFiles_ymd)
        layout.addWidget(self.button_data_yw)
        layout.addWidget(self.button_data_ymd)
        layout.addWidget(self.data_table)
        self.setLayout(layout)

        # Connect buttons to functions
        self.button_select_file.clicked.connect(self.select_file)
        self.button_dataFiles_ymd.clicked.connect(self.get_dataFiles_ymd)
        self.button_data_yw.clicked.connect(self.get_data_yw)
        self.button_data_ymd.clicked.connect(self.get_data_ymd)

    def display_data(self, data):
        self.data_table.setRowCount(0)
        self.data_table.setColumnCount(0)

        if data is None:
            self.data_table.setRowCount(1)
            self.data_table.setColumnCount(1)
            self.data_table.setItem(0, 0, QtWidgets.QTableWidgetItem("Nothing was found for this date!!!\nTry input a different date"))
        else:
            if isinstance(data, pd.DataFrame):
                self.data_table.setColumnCount(len(data.columns))
                self.data_table.setRowCount(len(data))
                self.data_table.setHorizontalHeaderLabels(data.columns)

                for i in range(len(data)):
                    for j in range(len(data.columns)):
                        item = QtWidgets.QTableWidgetItem(str(data.iat[i, j]))
                        self.data_table.setItem(i, j, item)

                self.data_table.resizeColumnsToContents()
                self.data_table.resizeRowsToContents()

    def select_file(self):
        file_name, _ = QtWidgets.QFileDialog.getOpenFileName(self, "Select Data File", "", "CSV Files (*.csv)")
        
        if file_name:
            data = pd.read_csv(file_name)
            self.display_data(data)

    def get_dataFiles_ymd(self):
        target_date_input = self.date_input.text()
        try:
            data = get_dataFiles_ymd(target_date_input)
            self.display_data(data)
        except ValueError:
            self.display_data(pd.DataFrame({"Error": ["Invalid date format. Please use YYYY-MM-DD format."]}))

    def get_data_yw(self):
        target_date_input = self.date_input.text()
        try:
            data = get_data_yw(target_date_input)
            self.display_data(data)
        except ValueError:
            self.display_data(pd.DataFrame({"Error": ["Invalid week format. Please use YYYY-WW format."]}))

    def get_data_ymd(self):
        target_date_input = self.date_input.text()
        try:
            data = get_data_ymd(target_date_input)
            self.display_data(data)
        except ValueError:
            self.display_data(pd.DataFrame({"Error": ["Invalid date format. Please use YYYY-MM-DD format."]}))

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())