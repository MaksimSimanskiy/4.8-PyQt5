#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
В данной программе создается анимация круга, который движется от левой границы холста до правой.
"""

import sys
from PyQt5.Qt import QWidget, QPushButton, QPropertyAnimation, QApplication
from PyQt5.QtCore import QPoint


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setWindowTitle('Task5')
        self.resize(500, 500)
        self.move(400, 200)
        self.btn = QPushButton(self)
        self.setMouseTracking(True)
        self.init_ui()

    def init_ui(self):
        self.btn.resize(50, 50)
        self.btn.move(0, 0)
        self.btn.setStyleSheet("border-radius : 25px; border : 2px solid black;background-color: red;")
        self.animation = QPropertyAnimation(self.btn, b'pos', self)
        self.animation.setStartValue(QPoint(0, 0))
        self.animation.setDuration(5000)
        self.animation.start()

    def mouseMoveEvent(self, event):
        self.animation.setEndValue(QPoint(event.x(), event.y()))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec_())
