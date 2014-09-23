#takes a list and returns True if there is any elements that appear more than once. Does not modify original list.
def has_duplicates(list):
	duplicates = []
	for i in range(len(list)):
		for j in range(len(list)):
			if list[i] == list[j] and i != j:
				duplicates.append(list[i])
			
	if len(duplicates) > 0:
		return 'True'
	else:
		return 'False'

def generate_birthdays():
	months = range(1,13)
	days = range(1,32)

	import random

	birthday = {}

	for i in range(23):
		birthday[i] = [random.choice(months),random.choice(days)]
		while birthday[i] in [4, 6, 9, 11] and birthday[i][1] > 30:
			birthday[i] = [random.choice(months),random.choice(days)]
		while birthday[i] == 2 and birthday[i][1] > 28:
			birthday[i] = [random.choice(months),random.choice(days)]

	print birthday
	return birthday

print has_duplicates(generate_birthdays())