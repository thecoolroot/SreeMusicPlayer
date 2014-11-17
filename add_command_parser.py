def add_command_string_parser(add_string):

	while add_string[0] == " ": #spaces before commands auto removed
		add_string = add_string[1:]
	else:
		while add_string[-1] == " ": #spaces after commands auto removed.
			add_string = add_string[0:-1]
	
	space = add_string.find(' ')
	last_stopped_point = 0

	playlist =[]

	if last_stopped_point == 0:
		playlist.append(add_string[0:space])

	while (last_stopped_point+1):
		space = add_string.find(' ', last_stopped_point)
		if add_string[space+1] == "'" or add_string[space+1] == '"':
			colon_end = add_string.find("'", space+2) if add_string[space+1] == "'" else add_string.find('"', space+2)
			playlist.append(add_string[(space+2):colon_end])
			last_stopped_point = colon_end
		elif add_string[space+1] == " ":
			last_stopped_point += 1
		elif last_stopped_point == (len(add_string)-1):
			break
		else:
			next_space = add_string.find(" ", space+1)
			if next_space !=  -1:
				playlist.append(add_string[(space+1):next_space])
			else:
				playlist.append(add_string[(space+1):])
			last_stopped_point = next_space
	else:
		playlist.pop(0)
		print ("Added songs:", end=" ")
		print (playlist)

	return playlist