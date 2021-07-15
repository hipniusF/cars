from PySide2.QtWidgets import QApplication

from city import City

if __name__ == '__main__':
    app = QApplication([])
    city = City()
    city.show()
    app.exec_()
