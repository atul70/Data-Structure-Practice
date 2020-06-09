class Node():
    def __init__(self,data):
        self.data = data
        self.next = None

def create_linkedlist(root, data):
    node = Node(data)
    if root == None:
        root = node
    else:
        last_node = root
        while(last_node.next != None):
            last_node = last_node.next
        last_node.next = node
    return root

root = None
data_list = [15,16,17,18,19,20]
for data in data_list:
    root = create_linkedlist(root, data)

while(root != None):
    print(root.data)
    root = root.next


