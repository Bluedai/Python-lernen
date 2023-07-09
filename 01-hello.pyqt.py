#!/usr/bin/env python3
#  pip install pyqt5

import sys
from PyQt5.QtWidgets import QApplication, QLabel

# Erstellen Sie eine Instanz der Anwendung
app = QApplication(sys.argv)

# Erstellen Sie ein Label-Widget mit dem Text "Hello World"
label = QLabel("Hello World!")

# Zeigen Sie das Label-Widget auf dem Bildschirm an
label.show()

# Starten Sie die Anwendungsschleife
sys.exit(app.exec_())

