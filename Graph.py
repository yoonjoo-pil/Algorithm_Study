import queue
import Linked_list

# directed graph
class Node:
    def __init__(self,vertex):
        self.vertex = vertex
        self.neighbor = []
        self.visited = False
    def connect(self,v):
        if v in self.neighbor:
            print("Already connected")
            return
        self.neighbor.append(v)
        return

class Node_forBST :
    def __init__(self, vertex, left=None, right=None) :
        self.vertex = vertex
        self.left = left
        self.right = right
    
    def printing(self) :
        if self.left :
            self.left.printing()
        if self.vertex:
            print(self.vertex)
        if self.right :
            self.right.printing()

class Node_forBST2(Node_forBST):
    def __init__(self,vertex, left=None,right=None, parent=None):
        super().__init__(vertex,left,right)
        self.parent = parent

#depth for binary tree
def depth(root) :
    if root.left == None and root.right == None :
        return 1
    if root.left :
        return 1 + depth(root.left)
    if root.right :
        return 1 + depth(root.right)
    

#4.1 
def search(start_vertex, v1, v2):
    if v1 == v2 :
        return True
    
    visited = queue.Queue()
    visited.put(start_vertex)
    if start_vertex == v1:
        flag = True
    else :
        flag = False

    while not visited.empty() :
        temp = visited.get()
        temp.visited = True
        for v in temp.neighbor :
            if v == v1 :
                flag = True
            if flag and v == v2 :
                return True
            if not v.visited :
                visited.put(v)
    return False

'''
if __name__=="__main__" :
    v1 = Node(1)
    v2 = Node(2)
    v3 = Node(3)
    v4 = Node(4)
    v1.connect(v2)
    v1.connect(v4)
    v2.connect(v3)
    v3.connect(v4)

    print(search(v1,v3,v1))
'''

#4.2
def bst(lst) :
    n = len(lst)
    if n == 1:
        return Node_forBST(lst[0])
    elif n == 2:
        v1 = Node_forBST(lst[0])
        v2 = Node_forBST(lst[1])
        v2.left = v1
        return v2
    else :
        root = Node_forBST(lst[n//2])
        root.left = bst(lst[:n//2])
        root.right = bst(lst[n//2+1:])
    return root

'''
if __name__ == '__main__' :
    lst = list(range(1,7))  
    root = bst(lst)
    root.printing()
'''

#4.3 솔루션 참고.
def create_linked_list(root):
    result = []
    current_level = []
    if root:
        current_level.append(root)
    while current_level :
        result.append(current_level)
        parents = current_level
        current_level = []
        for parent in parents:
            if parent.left:
                current_level.append(parent.left)
            if parent.right:
                current_level.append(parent.right)
    
    return result
'''
if __name__ == '__main__' :
    lst = list(range(1,7))  
    root = bst(lst)
    #root.printing()
    lst = create_linked_list(root)
    for i in range(len(lst)):
        print("depth : ",i)
        for node in lst[i]:
            print(node.vertex)
'''
#4.4 균형 확인 - 좀 더 효율적으로 고쳐보기.
def is_balanced(root) :
    if not root :
        return True
    if root.left : 
        left_sub = depth(root.left)
    else :
        left_sub = 0
    if root.right : 
        right_sub = depth(root.right)
    else :
        right_sub = 0
    if abs(left_sub-right_sub) > 1 :
        return False
    else :
        if not is_balanced(root.left) :
            return False
        if not is_balanced(root.right) :
            return False
    return True
'''
if __name__ == "__main__" :
    
    lst = list(range(1,7))  
    root = bst(lst)
    print(is_balanced(root))
    root = Node_forBST(1)
    nodes=[]
    for i in range(2,8) :
        nodes.append(Node_forBST(i))
    root.left = nodes[0]
    root.right = nodes[1]
    nodes[0].left = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]
    nodes[2].left = nodes[-1]
    root.printing()
    print(is_balanced(root))
'''

#4.5 Check BST
def is_bst(root, minval=None, maxval=None):
    if not root:
        return True
    if minval and root.vertex > minval :
        return False
    if maxval and root.vertex > maxval :
        return False
    if root.left and root.vertex < root.left.vertex:
        return False
    if root.right and root.vertex > root.right.vertex:
        return False
    if not is_bst(root.left,maxval=root.vertex):
        return False
    if not is_bst(root.right,minval=root.vertex):
        return True

    return True
'''
if __name__=='__main__':
    lst = list(range(1,7))  
    root = bst(lst)
    root.printing()
    print("//////////")
    print(is_bst(root))
    
    
    root = Node_forBST(20)
    nodes=[]
    for i in [10,30,5,15,3,7,17] :
        nodes.append(Node_forBST(i))
    root.left = nodes[0]
    root.right = nodes[1]
    nodes[0].left = nodes[2]
    nodes[0].right = nodes[3]
    nodes[2].left = nodes[4]
    nodes[2].right = nodes[5]
    nodes[3].right = nodes[6]
    #print(root.printing())
    print(is_bst(root))
    '''

#4.6
def successor(node):
    if node.right:
        pointer = node.right
        while pointer.left:
            pointer = pointer.left
        return pointer.vertex

    if node.parent.left == node :
        return node.parent.vertex

    pointer = node.parent
    while pointer.parent and pointer.parent.left != pointer:
        pointer = pointer.parent
    if pointer.parent:
        return pointer.parent.vertex
    return "No Successor"

'''
if __name__ == '__main__':
    root = Node_forBST2(20)
    nodes=[]
    for i in [10,30,5,15,3,7,17] :
        nodes.append(Node_forBST2(i))
    root.left = nodes[0]
    root.right = nodes[1]
    nodes[0].parent = root
    nodes[1].parent = root
    nodes[0].left = nodes[2]
    nodes[0].right = nodes[3]
    nodes[2].parent = nodes[0]
    nodes[3].parent = nodes[0]
    nodes[2].left = nodes[4]
    nodes[2].right = nodes[5]
    nodes[4].parent = nodes[2]
    nodes[5].parent = nodes[2]
    nodes[3].right = nodes[6]
    nodes[6].parent = nodes[3]
    print(root.printing())
    print("////////////////")
    for n in nodes:
        print(n.vertex,successor(n))
'''
