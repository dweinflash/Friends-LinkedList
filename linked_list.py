"""
    File: linked_list.py
    Author: David Weinflash
    Purpose: Contains code implementing the LinkedList and Node classes.
"""

class LinkedList:
	def __init__(self):
		# initialize the instance variables of the LinkedList class
		self._head = None
	
	def get_head(self):
		# getter method for _head instance variable
		return self._head
	
	def add_node(self, node):
		"""
		Add a node to linked list. Do not add node if name already in list.
				
		Parameters: node is of Node class and is initialized with a name.
				
		Returns: None.
						
		Pre-condition: node is initialzed with a name.
				
		Post-condition: node is added to the head or end of the linked
		list. Node is not added if name already exists in list.
		"""
		curr = self.get_head()
		if curr == None:
			self._head = node
		else:
			name_match = 0
			if(curr.get_name() == node.get_name()):
				name_match += 1
			while(curr.get_next() != None and name_match == 0):
				curr = curr.get_next()
				if(curr.get_name() == node.get_name()):
					name_match += 1
			# add node to end of linked list if name not in list
			if(name_match == 0):
				curr.set_next(node)
	
	def update_nodes(self,node1,node2):
		"""
		Search linked list for a name matching node2. If match is found,
		add node1 to node2's friend list.
				
		Parameters: node1 and node2 both from Node class.
				
		Returns: None.
						
		Pre-condition: node1 and node2 both initialzed with names.
				
		Post-condition: node1 added to node2's friend list if node2 in
		linked list.
		"""
		curr = self.get_head()
		if(curr.get_name() == node2.get_name()):
			curr.set_friends(node1)
		else:
			while(curr.get_next() != None):
				curr = curr.get_next()
				if(curr.get_name() == node2.get_name()):
					curr.set_friends(node1)
	
	def __str__(self):
		"""
		Print each name in linked list.
				
		Parameters: linked_list is an object of LinkedList class.
				
		Returns: A print statement for each name in node.
						
		Pre-condition: linked_list is initialized with names.
				
		Post-condition: All names in linked list printed.
		"""
		name = self.get_head()
		if name != None:
			print(name)
			while(name.get_next() != None):
				name = name.get_next()
				print(name)
		return ""

class Node:
	def __init__(self,name):
		# initialize the instance variables of the LinkedList class
		self._name = name
		self._friends = LinkedList()
		self._next = None
	
	def get_next(self):
		# getter method for the _next instance variable
		return self._next
	
	def set_next(self, node):
		# setter method for the _next instance variable
		self._next = node
	
	def get_name(self):
		# getter method for the _name instance variable
		return self._name
	
	def set_friends(self,node):
		"""
		Add node to friend linked list.
				
		Parameters: node is an object of the Node class.
				
		Returns: None.
						
		Pre-condition: friend list is a linked list. node is a Node
		object.
				
		Post-condition: head of friend list instance variable linked to 
		new, updated list.
		"""
		friend_node = node
		friend_list = self._friends
		
		friend_list.add_node(friend_node)
		self._friends._head = friend_list.get_head()
	
	def __str__(self):
		# getter method for the string representation of name variable
		name = str(self.get_name())
		return name
