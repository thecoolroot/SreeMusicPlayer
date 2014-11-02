#!/usr/bin/env python3

import sys, readline
from pygame import mixer as core_player
import add_command_parser

print("Working...")

playlist = []
SONG_END = pygame.USEREVENT + 1

def commandline():
	run = True;

	while run:
		core_player.init()
		command = input("Command: ")
		if command == "play":
			if len(playlist) == 0:
				print ("Playlist empty...")
			else:
				if core_player.music.get_busy():
					core_player.music.unpause()
					print ("Unpaused...")
				else:
					pygame.mixer.music.set_endevent(SONG_END)
					core_player.music.load(playlist[0])
					core_player.music.play()
					print ("Playing...")
		elif command == "pause":
			core_player.music.pause()
			print ("Song paused...")
		elif command == "list":
			print (playlist)
		elif command == "clear":
			playlist.clear()
			print ("playlist cleared...")
		elif command == "stop":
			if core_player.get_init() is not None:
				core_player.music.stop()
				core_player.quit()
				print("Stopped")
			else:
				print("Nothing is playing")
		elif command == "add":
			print ("Give us a song to add in the form of 'add SongPath1 SongPath2 SongPath3...'")
		elif command[0:3] == "add":
			playlist.extend(add_command_parser.add_command_string_parser(command))
			print("Added successfully...")
		elif (command == "exit"):
			run = False;
			print("Bye bye")

if len(sys.argv) == 1:
	commandline();
else:
	for item in sys.argv:
		playlist.append(item)
	else:
		playlist.pop(0)

	print("Added successfully")
	commandline();
