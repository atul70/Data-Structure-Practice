class Node():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

#pointer = 0
def create_BST(root, data):
    node = Node(data)
    if root  == None:
        root = node
    else:
        last_node = root
        previous_node = last_node
        while(last_node != None):
            previous_node = last_node
            if last_node.value < node.value:
                last_node = last_node.right
            else:
                last_node = last_node.left

        if previous_node.value < node.value:
            previous_node.right = node
        else:
            previous_node.left = node
    return root


root = None
data_list = [201,43,23,76,91,3,95,73,10,82]
for data in data_list:
    root = create_BST(root,data)

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.value)
    inorder(root.right)

inorder(root)




"================================="




