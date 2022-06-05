# cannot figure out how to get it to stop printing "none" and have not been able to get the first name to print properly

def format_name(first_name, last_name):
	# code goes here
	if last_name == "":
		print('Name: ' + str(first_name))
	elif first_name == "":
		print('Name: ' + str(last_name))
	elif first_name and last_name == "":
		print(last_name, first_name)
	else:
    print(last_name, first_name)

print(format_name("Ernest", "Hemingway"))
# Should return the string "Name: Hemingway, Ernest"

print(format_name("", "Madonna"))
# Should return the string "Name: Madonna"

print(format_name("Voltaire", ""))
# Should return the string "Name: Voltaire"

print(format_name("", ""))
# Should return an empty string
