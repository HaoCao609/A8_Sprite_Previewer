#Github repo: https://github.com/HaoCao609/A8_Sprite_Previewer.git

#The demo sprite has 16 frames in total, so setting the FPS to 16 will be the best!
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

        # FPS slider
        self.fps_slider = QSlider(Qt.Horizontal)
        self.fps_slider.setMinimum(1)
        self.fps_slider.setMaximum(100)
        self.fps_slider.setValue(30)  # Default FPS value
        self.fps_slider.setTickPosition(QSlider.TicksBelow)
        self.fps_slider.setTickInterval(10)

        # FPS label
        self.fps_label = QLabel(f"FPS: {self.fps_slider.value()}")

        # Connect the slider to update the FPS label
        self.fps_slider.valueChanged.connect(self.update_fps_label)

        # Start/Stop button
        self.start_stop_button = QPushButton("Start")
        self.start_stop_button.clicked.connect(self.toggle_animation)

        # set layout
        layout = QVBoxLayout()
        layout.addWidget(self.image_label)
        layout.addWidget(self.fps_slider)
        layout.addWidget(self.fps_label)
        layout.addWidget(self.start_stop_button)
        self.setLayout(layout)

        # Timer for animation
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

    def load_frames(self):
        # load sprite_0.png, sprite_1.png ...
        folder = os.path.join(os.getcwd(), "sprites")
        for filename in sorted(os.listdir(folder)):
            if filename.startswith("sprite_") and filename.endswith(".png"):
                self.frames.append(os.path.join(folder, filename))

    def update_frame(self):
        # Update the image shown
        if self.frames:
            self.image_index = (self.image_index + 1) % len(self.frames)
            self.image_label.setPixmap(QPixmap(self.frames[self.image_index]))

    def toggle_animation(self):
        # Toggle start/stop
        if self.timer.isActive():
            self.timer.stop()
            self.start_stop_button.setText("Start")
        else:
            self.timer.start(1000 // self.fps_slider.value())  # Start with the selected FPS
            self.start_stop_button.setText("Stop")

    def update_fps_label(self):
        self.fps_label.setText(f"FPS: {self.fps_slider.value()}")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = SpritePreviewer()
    window.show()
    sys.exit(app.exec_())
