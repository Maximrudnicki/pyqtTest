import sys
import mysql.connector

from PyQt5.QtWidgets import *
from DBConnection import database_name, user, password


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.name = QLabel('Cartoon name: ')
        self.year = QLabel('Year of publishing: ')
        self.duration = QLabel('Duration: ')
        self.producer = QLabel('Producer: ')

        self.nameEdit = QLineEdit()
        self.yearEdit = QLineEdit()
        self.durationEdit = QLineEdit()
        self.producerEdit = QLineEdit()

        self.button = QPushButton('Save')
        self.button1 = QPushButton('Delete')
        self.button2 = QPushButton('Show')
        self.button3 = QPushButton('Close')

        self.button.clicked.connect(self.write_to_file)
        self.button1.clicked.connect(self.delete_by_name)
        self.button2.clicked.connect(self.show_btn_click)
        self.button3.clicked.connect(self.close)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(self.name, 1, 0)
        grid.addWidget(self.nameEdit, 1, 1)

        grid.addWidget(self.year, 2, 0)
        grid.addWidget(self.yearEdit, 2, 1)

        grid.addWidget(self.duration, 3, 0)
        grid.addWidget(self.durationEdit, 3, 1)

        grid.addWidget(self.producer, 4, 0)
        grid.addWidget(self.producerEdit, 4, 1)

        grid.addWidget(self.button, 5, 0)
        grid.addWidget(self.button1, 5, 1)
        grid.addWidget(self.button2, 6, 0)
        grid.addWidget(self.button3, 6, 1)

        self.setLayout(grid)

        self.setGeometry(300, 300, 150, 150)
        self.setWindowTitle('9')
        self.show()

    def write_to_file(self):
        conn = mysql.connector.connect(
            host='localhost',
            database=database_name,
            user=user,
            password=password)
        cursor = conn.cursor()
        add_cartoon = ("INSERT INTO cartoon"
                       "(name, year, duration, producer) "
                       "VALUES (%s, %s, %s, %s)")

        data_cartoon = (self.nameEdit.text(), self.yearEdit.text(), self.durationEdit.text(), self.producerEdit.text())

        cursor.execute(add_cartoon, data_cartoon)

        conn.commit()
        cursor.close()
        conn.close()

    def delete_by_name(self):
        conn = mysql.connector.connect(
            host='localhost',
            database=database_name,
            user=user,
            password=password)
        cursor = conn.cursor()

        delete_by_name = "DELETE FROM cartoon WHERE name = %s "

        cartoon_name = (self.nameEdit.text())

        cursor.execute(delete_by_name, (cartoon_name,))

        conn.commit()
        cursor.close()
        conn.close()

    def show_btn_click(self):
        conn = mysql.connector.connect(
            host='localhost',
            database=database_name,
            user=user,
            password=password)
        cursor = conn.cursor(buffered=True)

        query = "SELECT * FROM cartoon"

        cursor.execute(query)

        result = cursor.fetchall()
        print(result)

        conn.commit()
        cursor.close()
        conn.close()

    def close(self):
        QApplication.quit()


def main():

    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
