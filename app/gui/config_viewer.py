from PyQt5.QtWidgets import (
    QWidget, QLabel, QSpinBox, QDoubleSpinBox, QCheckBox, QLineEdit,
    QVBoxLayout, QPushButton, QFileDialog, QApplication
)
import sys
from config.config_manager import load_config, save_config

class ConfigViewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Podešavanja sistema")
        self.setGeometry(200, 200, 400, 400)
        self.config = load_config()
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        self.output_folder = QLineEdit(self.config["output_folder"])
        self.db_folder = QLineEdit(self.config["database_folder"])

        self.max_attempts = QSpinBox()
        self.max_attempts.setValue(self.config["max_humanization_attempts"])
        self.max_attempts.setRange(1, 10)

        self.ai_threshold = QDoubleSpinBox()
        self.ai_threshold.setDecimals(2)
        self.ai_threshold.setRange(0.0, 1.0)
        self.ai_threshold.setValue(self.config["ai_score_threshold"])

        self.language = QLineEdit(self.config["language"])
        self.format = QLineEdit(self.config["output_format"])

        self.use_gpt = QCheckBox("Koristi ChatGPT")
        self.use_gpt.setChecked(self.config["use_chatgpt"])

        self.use_undetectable = QCheckBox("Koristi Undetectable.ai")
        self.use_undetectable.setChecked(self.config["use_undetectable"])

        browse_out = QPushButton("Izaberi output folder")
        browse_out.clicked.connect(self.choose_output)

        browse_db = QPushButton("Izaberi folder baze")
        browse_db.clicked.connect(self.choose_db)

        save_btn = QPushButton("💾 Sačuvaj podešavanja")
        save_btn.clicked.connect(self.save_config)

        layout.addWidget(QLabel("📁 Output folder:"))
        layout.addWidget(self.output_folder)
        layout.addWidget(browse_out)

        layout.addWidget(QLabel("🗃️ Folder baze:"))
        layout.addWidget(self.db_folder)
        layout.addWidget(browse_db)

        layout.addWidget(QLabel("🔁 Maks. pokušaja humanizacije:"))
        layout.addWidget(self.max_attempts)

        layout.addWidget(QLabel("🎯 AI skor prag (manje je bolje):"))
        layout.addWidget(self.ai_threshold)

        layout.addWidget(QLabel("🌐 Jezik:"))
        layout.addWidget(self.language)

        layout.addWidget(QLabel("📄 Format izlaza:"))
        layout.addWidget(self.format)

        layout.addWidget(self.use_gpt)
        layout.addWidget(self.use_undetectable)

        layout.addWidget(save_btn)
        self.setLayout(layout)

    def choose_output(self):
        folder = QFileDialog.getExistingDirectory(self, "Izaberi folder")
        if folder:
            self.output_folder.setText(folder)

    def choose_db(self):
        folder = QFileDialog.getExistingDirectory(self, "Izaberi folder baze")
        if folder:
            self.db_folder.setText(folder)

    def save_config(self):
        new_config = {
            "output_folder": self.output_folder.text(),
            "database_folder": self.db_folder.text(),
            "max_humanization_attempts": self.max_attempts.value(),
            "ai_score_threshold": self.ai_threshold.value(),
            "language": self.language.text(),
            "output_format": self.format.text(),
            "use_chatgpt": self.use_gpt.isChecked(),
            "use_undetectable": self.use_undetectable.isChecked()
        }
        save_config(new_config)
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    viewer = ConfigViewer()
    viewer.show()
    sys.exit(app.exec_())
