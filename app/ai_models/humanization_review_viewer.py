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
    def add_retry_button(self):
        retry_btn = QPushButton("🔁 Ponovo humanizuj označeni tekst")
        retry_btn.clicked.connect(self.retry_humanization)
        return retry_btn

    def retry_humanization(self):
        index = self.list_widget.currentRow()
        if index < 0 or index >= len(self.results):
            return
        from ai_models.ai_humanizer import humanize_text
        ai_text = self.results[index]['text']
        extracted = self.extract_ai_section(ai_text)
        if not extracted:
            self.text_display.setPlainText("⚠️ Nema označenog AI teksta za humanizaciju.")
            return
        try:
            new_text = humanize_text(extracted)
            updated = ai_text.replace(extracted, new_text)
            self.results[index]['text'] = updated
            self.results[index]['status'] = 'success'
            self.text_display.setPlainText(updated)
            self.list_widget.item(index).setText(self.results[index]['title'] + " - ✅")
        except Exception as e:
            self.text_display.setPlainText(f"❌ Greška: {e}")

    def extract_ai_section(self, full_text: str):
        import re
        match = re.search(r"<!-- AI_START -->(.*?)<!-- AI_END -->", full_text, re.DOTALL)
        return match.group(1).strip() if match else ""
