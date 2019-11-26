class Node: 
	#constructor
	def __init__(self, data):
		self.data = data
		self.left_node = left_node 
		self.right_node = right_node

	def node_insert(self, d):
		if (self.data > d):
			if(self.left_node == None):
				self.left_node = Node(data = d)
				return(True)
			else: 
				return(self.left_node.node_insert(d))
		else:
			if(self.right_node == None):
				self.right_node = Node(data = d)
				return(True)
			else:
				return(self.right_node.node_insert(d))

	def node_find(self, d):
		if(self.data == d):
			return (True)

		elif(self.data > d):
			if (self.left_node):
				return(self.left_node.node_find(d))
			else:
				return(False)
		else: 
			if(self.right_node):
				return(self.right_node.node_find(d))
			else:
				return(False)

	def node_preorder(self):
		if(self):
			print(str(self.data))
			if(self.left_node):
				self.left_node.node_preorder()
			if(self.right_node):
				self.right_node.node_preorder()




class Tree:
	#constructor
	def __init__(self, root = None):
		self.root = root

	#tree insert
	def tree_insert(self, d):
		if (self.root):
			return(self.root.node_insert())
		else:
			self.root = Node(data = d)

	#tree find
	def tree_find(self, d):
		if(self.root):
			return(self.root.node_find())

		else:
			return(sle)

