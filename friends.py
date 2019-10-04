"""
    File: friends.py
    Author: David Weinflash
    Purpose: Uses code from linked_list.py to create a linked_list of 
    names. Each name in linked_list contains a linked_list of friends. 
    Output will return the mutual friends of two input names.
"""
import linked_list

def main():
	input_file = input('Input file: ')
	
	try:
		name_file = open(input_file)
	except IOError:
		print("ERROR: Could not open file " + input_file)
		exit()
	
	name_list = linked_list.LinkedList()
	
	for line in name_file:
		split_line = line.split()
		
		# name node for each name in line
		name_1 = linked_list.Node(split_line[0].lower())
		name_2 = linked_list.Node(split_line[1].lower())
		
		name_list.add_node(name_1)
		name_list.add_node(name_2)
		
		# friend node for each name in line
		friend_1 = linked_list.Node(split_line[0].lower())
		friend_2 = linked_list.Node(split_line[1].lower())
		
		# add friend_1 to name_2's friend list and vice versa
		name_list.update_nodes(friend_1,friend_2)
		name_list.update_nodes(friend_2,friend_1)
	
	name1 = input('Name 1: ').strip().lower()
	name2 = input('Name 2: ').strip().lower()
	
	# get each name's friend list
	name1_friends = name_friends(name1, name_list)
	name2_friends = name_friends(name2, name_list)
	
	# get and print mutual friends of name1 and name2
	same_friends = mutual_friends(name1_friends,name2_friends)
	print_mutual_friends(same_friends)

def name_friends(name, name_list):
	"""
	Search name_list for name. Get the friend list of name.
			
	Parameters: Name is user input. name_list is a linked_list.
			
	Returns: A list of the friends belonging to name. Assertion error if 
	name not found in name_list.
					
	Pre-condition: Name can be found in name_list.
			
	Post-condition: All items in name_list searched for matches with
	name.
	"""
	name_friends = []
	name_match = None
	
	# search name_list to find a match of name
	curr = name_list.get_head()
	if curr != None:
		if curr.get_name() == name:
			name_match = 1
			# returns the friend list of name
			name_friends = iterate_friends(curr._friends.get_head())
		else:
			while(curr.get_next() != None):
				curr = curr.get_next()
				if curr.get_name() == name:
					name_match = 1
					name_friends = iterate_friends(curr._friends.get_head())
	
	# name_match = 1 if name found in name_list
	assert name_match != None
	
	return name_friends

def iterate_friends(list_head):
	"""
	Get the friend list of name.
			
	Parameters: list_head is the head node of name's friend list.
			
	Returns: A list of the friends belonging to name.
					
	Pre-condition: Friend list of name is a linked list.
			
	Post-condition: All friends belonging to name iterated and returned.
	"""
	friends = []
	
	curr = list_head
	if curr != None:
		friends.append(curr.get_name())
		while(curr.get_next() != None):
			curr = curr.get_next()
			friends.append(curr.get_name())
	
	return friends
		
def mutual_friends(friends1, friends2):
	"""
	Get the mutual friends in friends1 list and friends2 list.
			
	Parameters: friends1 and friends2 are both lists.
			
	Returns: A list of mutual friends between friends1 and friends2.
					
	Pre-condition: friends1 and friends2 both initialized with friends.
			
	Post-condition: All friend matches between the two lists returned.
	"""
	mutual_friends = []
	return[friend for friend in friends1 if friend in friends2]

def print_mutual_friends(same_friends):
	"""
	Print all names in same_friends list.
			
	Parameters: same_friends is a list.
			
	Returns: A print statement for each name in same_friends. First 
	letter of each name is capitalized.
					
	Pre-condition: same_friends intitialized with names.
			
	Post-condition: All names in same_friends printed one per line.
	"""
	for name in same_friends:
		name = name.title()
		print(name)

main()
