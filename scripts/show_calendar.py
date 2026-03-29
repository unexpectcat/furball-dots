import sys
from PyQt6.QtWidgets import QApplication, QWidget, QCalendarWidget, QVBoxLayout
from PyQt6.QtCore import Qt

class CalendarPopup(QWidget):
    def __init__(self):
        super().__init__()
        # Remove .Popup and use .Window instead
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # Give it a specific object name so Hyprland can find it easily
        self.setObjectName("WaybarCalendar")
        
        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        self.cal = QCalendarWidget()
        
        # Matching your grey Hyprland setup
        self.cal.setStyleSheet("""
            QCalendarWidget QWidget { background-color: #111111; color: #eeeeee; border: 1px solid #444444; }
            QCalendarWidget QAbstractItemView:enabled { color: #eeeeee; selection-background-color: #444444; }
            QCalendarWidget QToolButton { color: #eeeeee; background-color: #222222; }
            QCalendarWidget QMenu { background-color: #111111; }
        """)
        
        layout.addWidget(self.cal)
        self.setLayout(layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = CalendarPopup()
    w.show()
    sys.exit(app.exec())