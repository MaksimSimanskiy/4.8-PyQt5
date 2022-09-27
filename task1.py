#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
напишите программу, состоящую из двух списков Listbox . В первом будет,
например, перечень товаров, заданный программно. Второй изначально пуст, пусть это
будет перечень покупок. При клике на одну кнопку товар должен переходить из одного
списка в другой. При клике на вторую кнопку – возвращаться (человек передумал покупать).
Предусмотрите возможность множественного выбора элементов списка и их перемещения.
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout,  QVBoxLayout, QListWidget, QAbstractItemView
app = QApplication(sys.argv)

LISTS = ("Морковь", "Капуста", "Яблоки", "Помидоры", "Салат",)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task1")
        self.setGeometry(370, 390, 370, 390)
        self.lst1 = QListWidget()
        self.lst1.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lst2 = QListWidget()
        self.lst2.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.lst1.addItems(LISTS)
        self.inp1 = QPushButton(">>>")
        self.inp2 = QPushButton("<<<")
        self.create()
        self.inp1.clicked.connect(self.ItemToRight)
        self.inp2.clicked.connect(self.ItemToLeft)

    def create(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        hbox.addWidget(self.lst1)
        hbox.addLayout(vbox)
        vbox.addWidget(self.inp1)
        vbox.addWidget(self.inp2)
        hbox.addWidget(self.lst2)
        self.setLayout(hbox)

    def ItemToRight(self):
        listItems = self.lst1.selectedItems()
        for item in listItems:
            self.lst1.takeItem(self.lst1.row(item))
            self.lst2.addItem(item)

    def ItemToLeft(self):
        listItems = self.lst2.selectedItems()
        for item in listItems:
            self.lst2.takeItem(self.lst2.row(item))
            self.lst1.addItem(item)


application = Window()
application.show()


if __name__ == '__main__':
    sys.exit(app.exec())