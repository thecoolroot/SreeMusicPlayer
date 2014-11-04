#!/usr/bin/env python3

import sys, threading
from time import sleep
from pygame import mixer as core_player

try:
	import readline
	#for linux
except ImportError:
	try:
		import rlcompleter
		#for windows
	except ImportError:
		import libedit
		#for Mac OSX

import add_command_parser

print("Working...")

playlist = []

current_song = 0

def thread_to_go():
	while True:
		sleep(1) # Time in seconds.
		if command != "stop" or not core_player.music.get_busy():
			global current_song
			current_song += 1
			if current_song < len(playlist):
				core_player.music.load(playlist[current_song])
				core_player.music.play()
			else:
				break


def commandline():
	run = True;

	while run:
		core_player.init()
		global command
		command = input("Command: ")

		if command == "":
			print("Please enter a command...")
		else:
			while command[0] == " ": #spaces before commands auto removed
				command = command[1:]
			else:
				while command[-1] == " ": #spaces after commands auto removed.
					command = command[0:-1]
			
			if command == "play":
				if len(playlist) == 0:
					print ("Playlist empty...")
				else:
					if core_player.music.get_busy():
						core_player.music.unpause()
						print ("Unpaused...")
					else:
						global current_song
						if current_song >= len(playlist):
							current_song = 0

						core_player.music.load(playlist[current_song])
						core_player.music.play()
						t = threading.Thread(target=thread_to_go)
						t.setDaemon(True)
						t.start()
						print ("Playing...")
			elif command == "pause":
				core_player.music.pause()
				print ("Song paused...")
			elif command == "list":
				print (playlist)
			elif command == "current":
				print(playlist[current_song])
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
			elif command[0:3] == "add" and command[3] == " ": # add command reply improved from previous
				playlist.extend(add_command_parser.add_command_string_parser(command))
				print("Added successfully...")
			elif (command == "exit"):
				run = False;
				print("Bye bye")
			else:
				print("Invalid command...")

def startup():
	if len(sys.argv) == 1:
		commandline()
	else:
		for item in sys.argv:
			playlist.append(item)
		else:
			playlist.pop(0)

		print("Added successfully")
		commandline()

startup()