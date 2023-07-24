from PyQt5.QtWidgets import QMainWindow, QApplication, QLabel, QSlider, QPushButton, QFileDialog, QMessageBox
from PyQt5 import uic
import sys
import os
os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')  # to import vlc library
import vlc
import time


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load The Ui File
        self.playlist = []
        uic.loadUi('P3-Music_Player.ui', self)

        # Define Our Widgets
        self.play_btn = self.findChild(QPushButton, 'play_btn')
        self.stop_btn = self.findChild(QPushButton, 'stop_btn')
        self.pause_btn = self.findChild(QPushButton, 'pause_btn')
        self.pre_btn = self.findChild(QPushButton, 'pre_btn')
        self.next_btn = self.findChild(QPushButton, 'next_btn')
        self.directory_btn = self.findChild(QPushButton, 'directory_btn')

        self.slider_btn = self.findChild(QSlider, 'slider_btn')

        self.name_label = self.findChild(QLabel, 'name_label')
        self.time_label = self.findChild(QLabel, 'time_label')
        self.volume_label = self.findChild(QLabel, 'volume_label')
        self.volume_icon_label = self.findChild(QLabel, 'volume_icon_label')

        # Slider
        self.slider_btn.setRange(0, 10)
        self.slider_btn.setValue(5)
        self.slider_btn.setTickPosition(QSlider.TicksBothSides)
        self.slider_btn.setTickInterval(1)
        self.slider_btn.setSingleStep(1)

        # Move The Slider
        self.slider_btn.valueChanged.connect(self.slide_it)
        # self.slider_btn.sliderReleased.connect(self.slide_it)

        # Button
        self.pre_btn.clicked.connect(self.previous_song)
        self.next_btn.clicked.connect(self.next_song)

        self.play_btn.clicked.connect(self.play_song)
        self.pause_btn.clicked.connect(self.pause_song)

        self.stop_btn.clicked.connect(self.stop)
        self.directory_btn.clicked.connect(self.directory)

        # Show The App
        self.show()

    def directory(self):
        self.fname = QFileDialog.getOpenFileName(self, 'Music Directory',
                                            'C:\\Users\IT CITY\PycharmProjects\pythonProject\Practice\P3-Music_Player',
                                            'MP3 Files (*.mp3);;Wave Files (*.wav)')

    def play_song(self):
        if self.fname:
            # creating the vlc media player object
            self.my_media = vlc.MediaPlayer(self.fname[0])
            self.my_media.play()
            time.sleep(0.3)

            ms = self.my_media.get_length()
            self.name_time_label(self.fname[0], ms)

            if self.fname[0] not in self.playlist:  # Makes the list of song addresses - with fname[0]
                self.playlist.append(self.fname[0])
        else:
            pass

    def pause_song(self):
        self.my_media.pause()  # play/pause toggle

    def stop(self):
        self.my_media.stop()  # reset
        self.name_label.setText('Song Name')
        self.time_label.setText('00:00:00')

    def previous_song(self):
        self.name_label.setText('Song Name')
        self.time_label.setText('00:00:00')
        for index in range(0, len(self.playlist)):
            if self.playlist[index] == self.fname[0]:  # fname[0] is the song that is/was played now
                self.my_media.stop()  # stops the song that is played now
                if index - 1 >= 0:
                    self.my_media = vlc.MediaPlayer(self.playlist[index-1])  # plays the song that was played before the current one
                    self.my_media.play()
                    time.sleep(0.3)
                    ms = self.my_media.get_length()
                    self.name_time_label(self.playlist[index - 1], ms)
                else:
                    QMessageBox.about(self, 'Error! Not Found', 'You are at the top of the playlist.')

    def next_song(self):
        self.name_label.setText('Song Name')
        self.time_label.setText('00:00:00')
        for index in range(0, len(self.playlist)):
            if self.playlist[index] == self.fname[0]:
                self.my_media.stop()
                if index + 1 <= len(self.playlist):
                    self.my_media = vlc.MediaPlayer(self.playlist[index + 1])
                    self.my_media.play()
                    time.sleep(0.3)
                    ms = self.my_media.get_length()
                    self.name_time_label(self.playlist[index + 1], ms)
                else:
                    QMessageBox.about(self, 'Error! Not Found', 'You are at the bottom of the playlist.')

    # Move The Slider Function
    def slide_it(self, value):
        self.volume_label.setText(str(value))
        '''
        print(self.my_media.audio_get_volume())
        if self.my_media.audio_get_volume() == 100:
            if value > 100:
                pass
        elif self.my_media.audio_get_volume() < 100 | self.my_media.audio_get_volume() > 0:
            self.my_media.audio_set_volume(int(value))
        elif self.my_media.audio_get_volume() == 0:
            if value < 0:
                pass
        '''

    def name_time_label(self, file_name, duration):
        for index in range(1, len(file_name)):
            if file_name[-index] == '/':  # It gives the last Slash
                # print(self.playlist[i + 1][-index:])
                self.name_label.setText(file_name[-index + 1:])  # Letters that come after the last Slash
                break
        if vlc.EventType.MediaParsedChanged:  # check is the code is parsed and ready to do other things on it
            seconds, milliseconds = divmod(duration, 1000)
            # print(seconds, milliseconds)
            minutes, seconds = divmod(seconds, 60)
            # print(minutes, seconds)
            hours, minutes = divmod(minutes, 60)
            # print("%d:%d:%d" % (hours, minutes, seconds))
            self.time_label.setText("%d:%d:%d" % (hours, minutes, seconds))  # placeholder for numbers


# Initialize The App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
