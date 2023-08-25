import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QFont 
import time

class OverlayWindow(QMainWindow):
    def __init__(self):
        super().__init__(flags=Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setGeometry(0, 400, 200, 100)

        self.label = QLabel(self)
        self.label.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: yellow;")
        self.label.setGeometry(10, 10, 180, 80)

        self.label.setFont(QFont("Arial", 14))  # Setze die Schriftart und Größe hier

        self.update_display()  # Initialanzeige aufrufen

        # Timer erstellen, um die Anzeige alle Sekunde zu aktualisieren
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_display)
        self.timer.start(1000)  # Timer alle 1000 Millisekunden (1 Sekunde) aufrufen

    def update_display(self):
        # Aktuelle Zeit abrufen
        current_time = time.localtime()
        current_hour = current_time.tm_hour
        current_minute = current_time.tm_min
        current_second = current_time.tm_sec

        # Berechne die verbleibende Zeit bis zur nächsten viertel Stunde (15 oder 45)
        if current_minute < 15:
            target_minute = 15
        elif current_minute < 45:
            target_minute = 45
        else:
            target_minute = 15  # Nächste Stunde, nächstes Ziel ist 15
        remaining_minutes = ((target_minute - current_minute) % 60) - 1
        remaining_seconds = 60 - current_second

        time_text = f"{current_hour:02d}:{current_minute:02d}:{current_second:02d}"
        rest_time_text = f"Restzeit: {remaining_minutes:02d}:{remaining_seconds:02d}"
        combined_text = f"{time_text} \n\n{rest_time_text}"

        self.label.setText(combined_text)  # Text im Label aktualisieren

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = OverlayWindow()
    overlay.show()
    sys.exit(app.exec_())
