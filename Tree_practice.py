class Node():
    def __init__(self,value):
        self.main = value
        self.right = None
        self.left = None



def Binary_Search_Tree(root,input):
    node = Node(input)
    if root == None:
        root = node
    else:
        last_node = root
        previous_node = last_node
        while (last_node!= None):
            if node.main > last_node.main:
                last_node = last_node.right
            else:
                last_node = last_node.left
        if previous_node.main < node.main:
            previous_node.right = node
        else:
            previous_node.left = node


    return root

root = None
array = [21,2,10,19,8,64,31,92,1,81]

for i in range(0,len(array)):
    root = Binary_Search_Tree(root, i)

def inorder(root):
    if root == None:
        return
    inorder(root.left)
    print(root.main)
    inorder(root.right)
inorder(root)



