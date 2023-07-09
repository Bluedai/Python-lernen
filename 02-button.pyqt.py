#!/usr/bin/env python3
#  pip install pyqt5

import sys
from PyQt5.QtWidgets import QApplication, QLabel, QPushButton, QVBoxLayout, QWidget

# Funktion, die aufgerufen wird, wenn der Button geklickt wird
def button_clicked():
    print("Button wurde geklickt!")

# Erstellen Sie eine Instanz der Anwendung
app = QApplication(sys.argv)

# Erstellen Sie ein Hauptfenster
window = QWidget()

# Erstellen Sie ein vertikales Layout für das Hauptfenster
layout = QVBoxLayout()

# Erstellen Sie ein Label-Widget mit dem Text "Hello World"
label = QLabel("Hello World!")

# Erstellen Sie einen Button-Widget
button = QPushButton("Klick mich!")

# Verbinden Sie die button_clicked-Funktion mit dem Button-Klickereignis
button.clicked.connect(button_clicked)

# Fügen Sie das Label und den Button dem Layout hinzu
layout.addWidget(label)
layout.addWidget(button)

# Setzen Sie das Layout für das Hauptfenster
window.setLayout(layout)

# Zeigen Sie das Hauptfenster auf dem Bildschirm an
window.show()

# Starten Sie die Anwendungsschleife
sys.exit(app.exec_())

