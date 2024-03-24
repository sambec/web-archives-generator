from moviepy.editor import *

# Load the mp4 file
video = VideoFileClip("Mixtape/Z_light_academia_playlist.mp4")

# Extract audio from video
video.audio.write_audiofile("Musique/A_light_academia_playlist.mp3")
