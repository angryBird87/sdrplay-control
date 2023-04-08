#!/usr/bin/python3

import sys
import subprocess

from PyQt6.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget,
)

def restart():
    subprocess.run("systemctl restart sdrplay", shell=True)

def stop():
    subprocess.run("systemctl stop sdrplay", shell=True)

app = QApplication([])
window = QWidget()
window.resize(240, 240)
window.setWindowTitle("SDRPlay-Treiber-Management")

layout = QVBoxLayout()
restartButton = QPushButton("Neustarten")
restartButton.clicked.connect(restart)
layout.addWidget(restartButton)

stopButton = QPushButton("Stoppen")
stopButton.clicked.connect(stop)
layout.addWidget(stopButton)

window.setLayout(layout)

window.show()

sys.exit(app.exec())