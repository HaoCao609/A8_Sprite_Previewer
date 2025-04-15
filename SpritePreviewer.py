#Github repo: https://github.com/HaoCao609/A8_Sprite_Previewer.git

import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class SpritePreviewer(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sprite Previewer")
        self.setGeometry(100, 100, 400, 400)

        # load images
        self.image_index = 0
        self.frames = []
        self.load_frames()

        # create label
        self.image_label = QLabel()
        self.image_label.setAlignment(Qt.AlignCenter)
        if self.frames:
            self.image_label.setPixmap(QPixmap(self.frames[0]))

        # set layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        self.setLayout(layout)

    def load_frames(self):
        # load sprite_0.png, sprite_1.png ...
        folder = self.image_folder = os.path.join(os.getcwd(), "sprites")
        for filename in sorted(os.listdir(folder)):
            if filename.startswith("sprite_") and filename.endswith(".png"):
                self.frames.append(os.path.join(folder, filename))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpritePreviewer()
    window.show()
    sys.exit(app.exec_())