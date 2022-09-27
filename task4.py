#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Создайте изображение на холсте
"""

import random
import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QBrush, QPen, QPainterPath
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout

app = QApplication(sys.argv)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Task4")
        self.setGeometry(570, 490, 570, 490)
        self.setStyleSheet(f"background-color:#69b9d0 ;")
        self.create()

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.darkYellow,  8, Qt.SolidLine))
        painter.setBrush(Qt.white)
        painter.drawRect(80, 240, 200, 200)
        painter.setPen(QPen(Qt.gray, 8, Qt.SolidLine))
        painter.drawRect(140, 290, 70, 70)
        painter.setPen(QPen(Qt.darkGreen,  8, Qt.SolidLine))
        painter.setBrush(Qt.green)
        painter.drawRect(0, 430, 570, 70)
        path = QPainterPath()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(Qt.darkGreen)
        painter.setBrush(Qt.lightGray)
        path.moveTo(140, 240)
        path.cubicTo(-60, 290, 230, -40, 290, 250)
        painter.drawPath(path)
        painter.setPen(QPen(Qt.red, 7, Qt.SolidLine))
        painter.setBrush(QBrush(Qt.yellow, Qt.SolidPattern))
        painter.drawEllipse(400, 20, 80, 80)
        self.drawGrass(painter)

    def drawGrass(self, painter):
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QPen(Qt.darkGreen, 4, Qt.SolidLine))
        painter.setBrush(Qt.darkGreen)
        for i in range(20):
            painter.drawArc(random.randint(0, 10), 320, i * 30, 360, 0 * 100, random.randint(45, 75) * 10)

    def create(self):
        vbox = QVBoxLayout()
        self.setLayout(vbox)


if __name__ == '__main__':
    application = Window()
    application.show()
    sys.exit(app.exec())