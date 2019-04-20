import os

def winlist():
	my_path = os.path.abspath(os.path.dirname(__file__))
	path = os.path.join(my_path, "templates/wins.properties")
	with open(path, 'r') as fl:
		return [strtolist(x) for x in fl]

def strtolist(string):
	indx = string.index('=') + 1
	return [num for num in string[indx:-1].split(',')]

print(winlist())

