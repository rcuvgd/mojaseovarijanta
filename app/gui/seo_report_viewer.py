from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTableWidget, QTableWidgetItem, QApplication
)
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
import sys

class SEOReportViewer(QWidget):
    def __init__(self, report: dict):
        super().__init__()
        self.setWindowTitle("SEO Izveštaj")
        self.setGeometry(100, 100, 600, 700)
        self.report = report
        self.init_ui()

    def get_color(self, value):
        if isinstance(value, int) or isinstance(value, float):
            if value > 0:
                return 'green'
            elif value == 0:
                return 'orange'
            else:
                return 'red'
        return 'black'

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel(f"🔍 Ključna reč: {self.report.get('keyword', '')}"))

        # SEO score sekcija
        layout.addWidget(QLabel("🎯 SEO Poeni"))
        seo_score = self.report.get("seo_score", {})
        for k, v in seo_score.items():
            if k == "total_score":
                continue
            lbl = QLabel(f"{k.replace('_', ' ').title()}: {v}")
            lbl.setStyleSheet(f"color: {self.get_color(v)}; font-weight: bold")
            layout.addWidget(lbl)

        total = QLabel(f"Ukupno: {seo_score.get('total_score', 0)} / 100")
        total.setAlignment(Qt.AlignCenter)
        total.setStyleSheet("font-size: 16px; font-weight: bold; margin-top: 10px")
        layout.addWidget(total)

        # Konkurencija sekcija
        layout.addWidget(QLabel("\n⚔️ Poređenje sa konkurencijom"))
        competition = self.report.get("competition", {})
        for k, v in competition.items():
            lbl = QLabel(f"{k.replace('_', ' ').title()}: {v}")
            lbl.setStyleSheet(f"color: {self.get_color(v)};")
            layout.addWidget(lbl)

        # Tabela sa SERP rezultatima
        layout.addWidget(QLabel("\n📄 SERP Rezultati"))
        serp = self.report.get("serp_results", [])
        table = QTableWidget()
        table.setRowCount(len(serp))
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Pozicija", "Naslov", "URL"])
        table.horizontalHeader().setStretchLastSection(True)

        for i, result in enumerate(serp):
            table.setItem(i, 0, QTableWidgetItem(str(result.get("position", ""))))
            table.setItem(i, 1, QTableWidgetItem(result.get("title", "")))
            table.setItem(i, 2, QTableWidgetItem(result.get("url", "")))

        layout.addWidget(table)
        self.setLayout(layout)

# Test primer za pokretanje GUI-ja samostalno
if __name__ == "__main__":
    app = QApplication(sys.argv)
    test_report = {
        "keyword": "seo strategija",
        "seo_score": {
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
        },
        "competition": {
            "naslov_jaci_od": 6,
            "opis_duzi_od": 4,
            "keyword_u_naslovu": 7,
            "prosek_reci_konkurencije": 742,
            "nas_prosek": 613
        },
        "serp_results": [
            {"position": 1, "title": "Šta je SEO?", "url": "https://primer.com/seo"},
            {"position": 2, "title": "SEO strategija 2024", "url": "https://seoexpert.com/strategija"},
        ]
    }
    viewer = SEOReportViewer(test_report)
    viewer.show()
    sys.exit(app.exec_())
