from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QTextEdit, QApplication, QListWidget, QListWidgetItem
)
import sys
import json
import os

class QualityViewer(QWidget):
    def __init__(self, output_folder: str = "output"):
        super().__init__()
        self.setWindowTitle("📊 Ocene kvaliteta teksta")
        self.setGeometry(150, 150, 800, 600)
        self.output_folder = output_folder
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.file_list = QListWidget()
        self.file_list.currentItemChanged.connect(self.load_metrics)

        for file in os.listdir(self.output_folder):
            if file.endswith("_metrics.json"):
                item = QListWidgetItem(file)
                self.file_list.addItem(item)

        self.text_box = QTextEdit()
        self.text_box.setReadOnly(True)

        layout.addWidget(QLabel("📁 Izaberite fajl sa metrikama:"))
        layout.addWidget(self.file_list)
        layout.addWidget(QLabel("📊 Rezultati analize:"))
        layout.addWidget(self.text_box)

        self.setLayout(layout)

    def load_metrics(self):
        item = self.file_list.currentItem()
        if not item:
            return
        path = os.path.join(self.output_folder, item.text())
        try:
            with open(path, "r", encoding="utf-8") as f:
                data = json.load(f)
            pretty = json.dumps(data, indent=2, ensure_ascii=False)
            self.text_box.setPlainText(pretty)
        except Exception as e:
            self.text_box.setPlainText(f"Greška: {e}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = QualityViewer("output")
    viewer.show()
    sys.exit(app.exec_())
