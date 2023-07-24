from pydub import AudioSegment
import os

CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))

song_path = os.path.dirname(os.path.realpath('music.mp3'))

filename = os.path.join(song_path, 'music.mp3')

app = QtCore.QCoreApplication(sys.argv)

QtMultimedia.QSound.play(filename)