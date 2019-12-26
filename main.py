from time import sleep
from yandex_music.client import Client
import os
import sys

os.system("killall mocp")
os.system("mocp -S")

if __name__ == "__main__":
	for param in sys.argv:
		print ("The next track number {}!".format(param))
		n_song = param
client = Client()
client = Client.from_credentials('username@ya.ru', 'password')
if (n_song == None or n_song == 0):
	n_song = 1
print ("START downloading...")
client.users_likes_tracks()[int(n_song)].track.download('playing.mp3')
print (" FINISHED!")

while(1):
	print ("Track No \"{}\"".format(client.users_likes_tracks()[int(n_song)].track.title))
	t_dur = client.users_likes_tracks()[int(n_song)].track.duration_ms
	os.system('mocp -l playing.mp3')
	n_song = int(n_song) + 1
	client.users_likes_tracks()[int(n_song)].track.download('buffer.mp3')
	print ("PLAYING...")
	sleep(t_dur / 1000)
	print (" OVER.")
	os.system('mocp -G')
	os.system('mv buffer.mp3 playing.mp3')
