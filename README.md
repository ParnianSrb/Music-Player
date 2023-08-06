# Music Player
### Playing MP3 & WAVE files from a local place on the Pc

A Python based project, which plays music using the "file" button on the application; moreover, you can choose the file type (MP3/Wave) aswell.

The GUI is designed by QtDesigner and Libraries are: PyQt5, vlc, time


---------- ![music player](https://github.com/ParnianSrb/Music-Player/assets/82469872/95af2c24-bb89-4e1d-9d9e-a70f69bccee4) ----------


Expectations and Problem:
1. The slider widget, that is expected to change the Volume, does not work. I have tried different ways and some code is commented in the relevant function → slide_it()
2. I wanted the duration label starts decreasing while the music starts, and goes on playing, however I could only show the total duration of the song constantly.
3. The next_song() and previous_song() functions are almost the same, thus the code ought to be much cleaner, than what I wrote here.
4. The fname() variable, which is created by QFileDialog.getOpenFileName() method, is the address of a music file in a specific local directory -C:\\Users\IT CITY\PycharmProjects\pythonProject\Practice\P3-Music_Player- that I wrote in this method. This directory is local, and users/developers ought to change it by their own music files' address.

***Tip: I had difficulty, importing the vlc library i.e. I used the direct way to import vlc → os.add_dll_directory(r'C:\Program Files\VideoLAN\VLC')
