#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Напишите программу по описанию. Размеры многострочного текстового поля определяются значениями,
введенными в однострочные текстовые поля. Изменение размера происходит при нажатии мышью на кнопку,
а также при нажатии клавиши Enter. Цвет фона экземпляра Text светлосерый ( lightgrey ),
когда поле не в фокусе, и белый, когда имеет фокус. Событие получения фокуса обозначается как <FocusIn> ,
 потери – как <FocusOut> .Для справки: фокус перемещается по виджетам при нажатии Tab,
Ctrl+Tab, Shift+Tab, а также при клике по ним мышью (к кнопкам последнее не относится).
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QHBoxLayout,  QVBoxLayout, QPushButton, QTextEdit
from PyQt5 import QtCore
app = QApplication(sys.argv)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        QApplication.instance().focusChanged.connect(self.on_focusChanged)
        self.setWindowTitle("Task3")
        self.setGeometry(370, 390, 370, 390)
        self.inp1 = QLineEdit()
        self.inp2 = QLineEdit()
        self.inp2.returnPressed.connect(self.EditSize)
        self.txtbox = QTextEdit()
        self.btn1 = QPushButton("Изменить")
        self.btn1.clicked.connect(self.EditSize)
        self.create()

    def create(self):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        hbox.addWidget(self.inp1)
        hbox.addWidget(self.inp2)
        hbox.addWidget(self.btn1)
        vbox.addLayout(hbox)
        vbox.addWidget(self.txtbox)
        self.setLayout(vbox)

    def EditSize(self):
        self.txtbox.resize(int(self.inp1.text()),int(self.inp2.text()))

    @QtCore.pyqtSlot("QWidget*", "QWidget*")
    def on_focusChanged(self, old, now):
        if self.txtbox == now:
            self.txtbox.setStyleSheet(f"background-color: white;")
        elif self.txtbox == old:
            self.txtbox.setStyleSheet(f"background-color: lightgrey;")


application = Window()
application.show()

if __name__ == '__main__':
    sys.exit(app.exec())
