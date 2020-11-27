# Node Class
class Node:

    # function to initialise the node object
    def __init__(self,data):
        self.data = data # assign data
        self.prev = None
        self.next = None # Initialize next as null

    # I know I need the following two functions, but I can't figure out how to use them.
    def __repr__(self):
        pass

    def __str__(self):
        pass


    def print_list(self):
    # printing list
        node = self # changed node = head to node = self
        while True:
            if node:
                print("Previous node: Node[%s] " % str(int(node.data)-1))
                print("Node data: %s " % (node.data))
                print("Next node: Node[%s] " % (node.next))
                print("")
                node = node.next
            else:
                break
    
    def get_length(self): # wouldn't need to send head as a parameter
        node = self # node = self.head
        size = 0
        while True:
            if node:
                size += 1
                node = node.next
            else:
                print("Size of Linked List: %s " % size)
                break




if __name__ == "__main__":
    head = Node(1)
    node = head
    # list creation
    for index in range(2, 10):
        node.next = Node(int(index))
        node.prev = Node((index-2))
        node = node.next


    head.get_length()
    head.print_list()

    # head = Node(1)
    # node = head
    # node.add_node(1)
    # node.print_list()
    # node.add_node(2)
    # node.add_node(3)