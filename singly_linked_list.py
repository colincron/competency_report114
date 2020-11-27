# Node Class
class Node:

    # function to initialise the node object
    def __init__(self,data):
        self.data = data # assign data
        self.next = None # Initialize next as null

    def print_list(self):
    # printing list
        node = self # changed node = head to node = self
        while True:
            if node:
                print(node.data)
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

    # def deleteNode(self, key):

    #     # store head node
    #     temp = self

    #     # if head node itself holds the key to be deleted
    #     if temp is not None:
    #         if temp.data == key:
    #             self.head = temp.next
    #             temp = None
    #             return
            
    #     # search for the key to be deleted, keep track of the
    #     # previous node as we need to change 'prev.next'
    #     while temp is not None:
    #         if temp.data == key:
    #             break
    #         prev = temp
    #         temp = temp.next

    #         # if key was not present in linked list
    #         if temp == None:
    #             return
            
    #         # unlink the node form linked list
    #         prev.next = temp.next

    #         temp = None


if __name__ == "__main__":
    head = Node(1)
    node = head
    # list creation
    for index in range(2, 10):
        node.next = Node(index)
        node = node.next

    head.print_list()
    head.get_length()
    head.print_list()