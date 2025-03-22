from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QPushButton, QTextEdit, QHBoxLayout, QApplication, QMessageBox
)
import sys

from ai_models.ai_detector_exporter import extract_ai_generated_text
from ai_models.ai_humanizer import humanize_text
# from ai_models.undetectable_adapter import humanize_with_undetectable  # ako želiš ovo, odkomentariši

class AIHumanizerViewer(QWidget):
    def __init__(self, full_text: str, keyword: str, language: str = "srpski"):
        super().__init__()
        self.setWindowTitle("AI Humanizator")
        self.setGeometry(100, 100, 800, 600)

        self.keyword = keyword
        self.language = language
        self.full_text = full_text
        self.ai_text = extract_ai_generated_text(full_text)

        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        layout.addWidget(QLabel("🧠 AI Generisani Deo:"))
        self.ai_box = QTextEdit()
        self.ai_box.setPlainText(self.ai_text)
        layout.addWidget(self.ai_box)

        layout.addWidget(QLabel("👤 Humanizovan Tekst:"))
        self.result_box = QTextEdit()
        self.result_box.setPlaceholderText("Klikni 'Humanizuj' da vidiš rezultat...")
        layout.addWidget(self.result_box)

        button_layout = QHBoxLayout()
        gpt_btn = QPushButton("Humanizuj (ChatGPT)")
        gpt_btn.clicked.connect(self.use_gpt)

        # undetect_btn = QPushButton("Humanizuj (Undetectable)")
        # undetect_btn.clicked.connect(self.use_undetectable)

        button_layout.addWidget(gpt_btn)
        # button_layout.addWidget(undetect_btn)

        layout.addLayout(button_layout)
        self.setLayout(layout)

    def use_gpt(self):
        ai_text = self.ai_box.toPlainText().strip()
        if not ai_text:
            QMessageBox.warning(self, "Greška", "Nema AI sadržaja za slanje.")
            return
        try:
            result = humanize_text(ai_text, self.language)
            self.result_box.setPlainText(result)
        except Exception as e:
            QMessageBox.critical(self, "Greška", str(e))

    # def use_undetectable(self):
    #     ai_text = self.ai_box.toPlainText().strip()
    #     if not ai_text:
    #         QMessageBox.warning(self, "Greška", "Nema AI sadržaja za slanje.")
    #         return
    #     try:
    #         result = humanize_with_undetectable(ai_text, api_key="YOUR_API_KEY", language=self.language)
    #         self.result_box.setPlainText(result)
    #     except Exception as e:
    #         QMessageBox.critical(self, "Greška", str(e))

if __name__ == "__main__":
    app = QApplication(sys.argv)
    test_text = '''
    Ovo je originalni deo teksta.

    <!-- AI_START -->
    Ovo je automatski dodat tekst koji bi možda trebalo prepraviti da zvuči ljudskije.
    <!-- AI_END -->
    '''
    viewer = AIHumanizerViewer(test_text, keyword="seo strategija")
    viewer.show()
    sys.exit(app.exec_())
