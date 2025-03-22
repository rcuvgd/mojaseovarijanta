from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QApplication, QGridLayout
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import sys

class SEOScoreViewer(QWidget):
    def __init__(self, seo_report: dict):
        super().__init__()
        self.setWindowTitle("SEO Score Report")
        self.setGeometry(100, 100, 400, 400)
        self.seo_report = seo_report
        self.init_ui()

    def get_color(self, value):
        if value > 0:
            return 'green'
        elif value == 0:
            return 'orange'
        else:
            return 'red'

    def init_ui(self):
        layout = QVBoxLayout()
        grid = QGridLayout()

        row = 0
        for key, value in self.seo_report.items():
            if key == "total_score":
                continue
            label_key = QLabel(key.replace("_", " ").title())
            label_value = QLabel(str(value))
            label_value.setStyleSheet(f"color: {self.get_color(value)}; font-weight: bold")
            grid.addWidget(label_key, row, 0)
            grid.addWidget(label_value, row, 1)
            row += 1

        total = QLabel(f"Total Score: {self.seo_report.get('total_score', 0)} / 100")
        total.setAlignment(Qt.AlignCenter)
        total.setStyleSheet("font-size: 16px; font-weight: bold; margin-top: 10px")

        layout.addLayout(grid)
        layout.addWidget(total)
        self.setLayout(layout)

# Test primer za pokretanje GUI-ja samostalno
if __name__ == "__main__":
    app = QApplication(sys.argv)
    test_report = {
        "title": 20,
        "meta_description": 15,
        "h1": 10,
        "h2_h3": 10,
        "first_paragraph": 10,
        "alt_texts": 6,
        "keyword_density": 15,
        "meta_length": 5,
        "word_count": 5,
        "total_score": 96
    }
    viewer = SEOScoreViewer(test_report)
    viewer.show()
    sys.exit(app.exec_())
