from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QApplication
)
from PyQt5.QtCore import QTimer
import sys
import json
from ai_models.text_quality import analyze_text_quality

class ManualTextAnalyzer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("✍️ Ručna analiza teksta (real-time)")
        self.setGeometry(200, 200, 800, 600)
        self.init_ui()
        self.timer = QTimer()
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.analyze_text)
        self.timer.start()

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("📝 Unesi tekst:"))
        self.text_input = QTextEdit()
        layout.addWidget(self.text_input)

        layout.addWidget(QLabel("📈 Analiza u realnom vremenu:"))
        self.result_box = QTextEdit()
        self.result_box.setReadOnly(True)
        layout.addWidget(self.result_box)

        self.setLayout(layout)

    def analyze_text(self):
        text = self.text_input.toPlainText()
        if not text.strip():
            self.result_box.setPlainText("⚠️ Unesi tekst za analizu.")
            return
        metrics = analyze_text_quality(text)
        pretty = json.dumps(metrics, indent=2, ensure_ascii=False)
        self.result_box.setPlainText(pretty)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ManualTextAnalyzer()
    viewer.show()
    sys.exit(app.exec_())
