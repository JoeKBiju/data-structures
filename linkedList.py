

class Node:
	def __init__(self, value, next_node=None):
		self.value = value
		self.next_node = next_node

class LinkedList():
	def create_node(head, value, next_node=None):
		#Creates Node
		
		if head is None:
			head = Node(value)
			return head
		else:
			current_node = head
			while current_node is not None:
				if current_node.next_node is None:
					node = Node(value)
					current_node.next_node = node
					return node
				current_node = current_node.next_node

	def delete_node(head, value):
		#Deletes node if found
		
		prev_node = None
		current_node = head

		while current_node:
			if current_node.value == value:
				prev_node.next_node = current_node.next_node
			else:
				prev_node = current_node
				current_node = current_node.next_node


	def find_value(head, value):
		#Finds node with value
		
		current_node = head

		while current_node:
			if current_node.value == value:
				return True
			else:
				current_node = current_node.next_node
			
		return False

	def print_values(head):
		#Prints entire linked list
		
		current_node = head

		print("List:", end='')
		while current_node:
			print(current_node.value, end=' ')
			current_node = current_node.next_node

	def delete_list():
		return None

if __name__ == "__main__":
	n1 = None #Head Initilisation
	n1 = LinkedList.create_node(n1, 5)
	n2 = LinkedList.create_node(n1, 13)
	n3 = LinkedList.create_node(n1, -45)
	n4 = LinkedList.create_node(n1, 100)
	n5 = LinkedList.create_node(n1, 69)
	n6 = LinkedList.create_node(n1, 21)
	n7 = LinkedList.create_node(n1, 999999)
	n8 = LinkedList.create_node(n1, -2398347)
	n9 = LinkedList.create_node(n1, 0)
	print(LinkedList.find_value(n1, 69)) #True
	print(LinkedList.find_value(n1, 0)) #True
	print(LinkedList.find_value(n1, 1)) #False
	LinkedList.print_values(n1)
	LinkedList.delete_node(n1, 21)
	LinkedList.print_values(n1)
	n1 = delete_list(n1)
	LinkedList.print_values(n1)


