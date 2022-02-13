import sys

from PyQt5.QtWidgets import (
    QApplication,
    QDialog,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
)

from yt_audio_dl import download_audio


class Dialog(QDialog):
    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setWindowTitle("Download Audio from Youtube")

        v_layout = QVBoxLayout()
        form_layout = QFormLayout()

        self.video_url = QLineEdit()
        self.file_name = QLineEdit()

        form_layout.addRow("Video URL:", self.video_url)
        form_layout.addRow("[Optional] File name:", self.file_name)

        button = QPushButton("Download mp3 file")
        button.clicked.connect(self._slot_func)  # type: ignore

        v_layout.addLayout(form_layout)
        v_layout.addWidget(button)

        self.setLayout(v_layout)

    def _slot_func(self):
        video_url = self.video_url.text()
        file_name = self.file_name.text()
        self.video_url.setText("")
        self.file_name.setText("")
        download_audio(video_url, file_name)


def main():
    app = QApplication([])

    window = Dialog()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
