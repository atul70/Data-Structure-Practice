
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

n1 = Node(12)
n1.right = Node(25)
n1.left = Node(10)
n1.left.left = Node(534)
n1.left.right = Node(11)
n1.right.left = Node(76)
n1.right.right = Node(87)


def searching(search_value, data):
    if search_value == Node(data):
        return True

print(searching(12,n1))



'''
def inOrder(root):
    if root == None:
        return ;

    inOrder(root.left)
    print(root.data)
    inOrder(root.right)
'''
"""
def post_order(root):
    if root == None:
        return

    post_order(root.left)
    post_order(root.right)
    print(root.data)

"""
"""
def preorder(root):
    if root == None:
        return
    print(root.data)
    preorder(root.left)
    preorder(root.right)

n1 = Node(12)
n1.right = Node(25)
n1.left= Node(10)
n1.left.left = Node(534)
n1.left.right = Node(11)
n1.right.left = Node(76)
n1.right.right = Node(87)

#print(inOrder(n1))



print(preorder(n1))

"""













"""
class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

def Binary_Tree(root,data):
    if root == None:
        return Node(data)

    else:
        child_node = root
        if child_node.data ==None:
            child_node = child_node.left
        else:
            child_node =child_node.right
    return child_node
arr = [21,32,121,32,43]
root = None
print(Binary_Tree(root,arr))

"""
















