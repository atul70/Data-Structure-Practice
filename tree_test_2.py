class Node():
    def __init__(self,value):
        self.left = None
        self.head = value
        self.right = None


def create_BST(root, value):
    node = Node(value)
    if root == None:
        root = node
    #return root
    else:
        last_node = root
        #previous_node = last_node
        while( last_node != None):
            previous_node = last_node
            if last_node.head < node.head:
                last_node= last_node.right
            else:
                last_node= last_node.left
        if previous_node.head < node.head:
            previous_node.right = node
        else:
            previous_node.left = node

    return root


"""
root = None
data_list = [201,43,23,76,91,3,95,73,10,82,73]
for data in data_list:
    root = create_BST(root,data)

def inorder(root):
    if root == None:
        return

    inorder(root.left)
    print(root.head)
    inorder(root.right)

inorder(root)
"""
X = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,37,27,28,29,30,31,32,33,34,35,36,37,38,39,40
     ,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,67,68,69,70,71,72,73,74,75,76,77,78,79,80]
y = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
     1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

print(len(y))