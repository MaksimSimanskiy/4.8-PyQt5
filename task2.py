#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу по следующему описанию.
Нажатие Enter в однострочном текстовом поле приводит к перемещению текста из него в список (экземпляр Listbox ).
При двойном клике ( <Double-Button-1> ) по элементу-строке списка, она должна копироваться в текстовое поле.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit,  QVBoxLayout, QListWidget
app = QApplication(sys.argv)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task2")
        self.setGeometry(270, 290, 270, 290)
        self.lst1 = QListWidget()
        self.lst1.itemDoubleClicked.connect(self.replace_item)
        self.inp1 = QLineEdit()
        self.inp1.returnPressed.connect(self.replace_text)
        self.create()

    def create(self):
        vbox = QVBoxLayout()
        vbox.addWidget(self.inp1)
        vbox.addWidget(self.lst1)
        self.setLayout(vbox)

    def replace_text(self):
        self.lst1.addItem(self.inp1.text())
        self.inp1.clear()

    def replace_item(self):
        listItems = self.lst1.selectedItems()
        if not listItems: return
        for item in listItems:
            self.inp1.setText(item.text())


application = Window()
application.show()

if __name__ == '__main__':
    sys.exit(app.exec())
