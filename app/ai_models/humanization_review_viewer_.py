from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QPushButton, QListWidget,
    QListWidgetItem, QHBoxLayout, QApplication
)
import sys

class HumanizationReviewViewer(QWidget):
    def __init__(self, results: list):
        super().__init__()
        self.setWindowTitle("Pregled Humanizacije")
        self.setGeometry(100, 100, 900, 600)
        self.results = results
        self.init_ui()

    def init_ui(self):
        layout = QHBoxLayout()

        self.list_widget = QListWidget()
        for res in self.results:
            item = QListWidgetItem(f"{res['title']} - {'✅' if res['status'] == 'success' else '❌'}")
            self.list_widget.addItem(item)
        self.list_widget.currentRowChanged.connect(self.show_details)

        self.text_display = QTextEdit()
        self.text_display.setReadOnly(True)

        layout.addWidget(self.list_widget, 2)
        layout.addWidget(self.text_display, 5)

        self.setLayout(layout)

    def show_details(self, index):
        if index < 0 or index >= len(self.results):
            self.text_display.setPlainText("")
            return
        self.text_display.setPlainText(self.results[index]['text'])

if __name__ == "__main__":
    app = QApplication(sys.argv)
    sample_results = [
        {
            "title": "SEO strategija za 2024.",
            "status": "success",
            "text": "Original + <!-- AI_START -->Humanizovan tekst<!-- AI_END -->"
        },
        {
            "title": "Kako pisati blog postove",
            "status": "failed",
            "text": "Original + <!-- AI_START -->AI tekst koji nije prošao<!-- AI_END -->"
        }
    ]
    viewer = HumanizationReviewViewer(sample_results)
    viewer.show()
    sys.exit(app.exec_())
