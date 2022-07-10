class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def prepend(self, new_value):
        new_node = Node(new_value)
        new_node.next = self.head
        self.head = new_node
    
    def append(self, new_value):
        #create new node
        new_node = Node(new_value)

        #check if the linked list is empty
        if self.head is None:
            self.head = new_node
            return

        #But if the list is not empty, i need to traverse to the end
        # add the new node to the end

        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def insertAfter(self, prev_node, new_value):
        #check if the prev node even exists
        if prev_node is None:
            print("the given node is empty!")
            return
        
        #if node is not empty, then create a new node
        new_node = Node(new_value)
        #update the prev Node to point at the new node
        new_node.next = prev_node.next
        #update the prev Node to point at the new node
        prev_node.next = new_node

    def traverse(self):
        node = self.head
        while node != None:
            print(node.value)
            node = node.next

weekday_links = LinkedList()
weekday_links.prepend('Mon')
weekday_links.append('Tue')
weekday_links.append('Thur')
weekday_links.insertAfter(weekday_links.head.next, 'Wed')
weekday_links.prepend('Sun')

weekday_links.traverse()