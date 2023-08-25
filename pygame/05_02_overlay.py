import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtCore import Qt
import time

class OverlayWindow(QMainWindow):
    def __init__(self):
        super().__init__(flags=Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setGeometry(0, 0, 200, 100)

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
        remaining_minutes = ((target_minute - current_minute) % 60) -1
        remaining_seconds = 60 - current_second

        time_text = f"{current_hour:02d}:{current_minute:02d}:{current_second:02d}"
        rest_time_text = f"Restzeit: {remaining_minutes:02d}:{remaining_seconds:02d}"
        combined_text = f"{time_text} \n\n{rest_time_text}"

        self.label = QLabel(combined_text, self)
        self.label.setStyleSheet("background-color: rgba(0, 0, 0, 0); color: black;")
        self.label.setGeometry(10, 10, 180, 80)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    overlay = OverlayWindow()
    overlay.show()
    sys.exit(app.exec_())
