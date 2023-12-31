# Music Player
### Playing MP3 & WAVE files from a local place on the Pc

A Python based project, which plays music using the "file" button on the application; moreover, you can choose the file type (MP3/Wave) aswell.

The GUI is designed by QtDesigner and Libraries are: PyQt5, vlc, time

![music player](https://github.com/ParnianSrb/Music-Player/assets/82469872/95af2c24-bb89-4e1d-9d9e-a70f69bccee4) 


Tips:
1. vlc.EventType.MediaParsedChanged: Checks the code, in order to make sure if it is parsed, and ready to do other things on the my_media() object. To be percise, parsing happens when the music starts to play; and the time.sleep() method that has come after the play() method in some functions, gives the my_media() object enough time to parse the music file.
2. Creating Playlist: While one chooses songs and play them, a playlist is created, and the songs that are being played, get added to this list. So, it gives the ability to go through these songs, via the Next and Previous buttons on the application.
3. To find a song name, I used the fname variable, containing the full address, which includes the song name in the full path of the address. Going through each charachter of the path.
4. I had difficulty, importing the vlc library i.e. I used the absolute way to import vlc → os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')

Expectations and Problem:
1. The slider widget, that is expected to change the Volume, does not work. I have tried different ways and some code is commented in the relevant function → slide_it()
2. I wanted the duration label starts decreasing while the music starts, and goes on playing, however I could only show the total duration of the song constantly.
3. The next_song() and previous_song() functions are almost the same, thus the code ought to be much cleaner, than what I wrote here.
4. The fname() variable, which is created by QFileDialog.getOpenFileName() method, is the address of a music file in a specific local directory -C:\\Users\IT CITY\PycharmProjects\pythonProject\Practice\P3-Music_Player- that I wrote in this method. This directory is local, and users/developers ought to change it by their own music files' address.

Installation Instructions:
To use python I have tried coding with PyCharm which has been easy and straightforward. Here is the link to download and install: https://www.jetbrains.com/pycharm/download/?section=windows / https://www.jetbrains.com/help/pycharm/installation-guide.html#snap
