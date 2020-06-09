class Node():
    def __init__(self, value):
        self.value = value
        self.next = None

#head = None
def linked_list(head, value):
    node = Node(value)
    if head == None:
        head = node
    else:
        last_node = head
        while(last_node.next != None):
            last_node = last_node.next
        last_node.next = node
    return head

head = None
data_list = [12,32,43,10,65]
for data in data_list:
    head = linked_list(head, data)


while(head != None):
    print(head.value)
    head = head.next




