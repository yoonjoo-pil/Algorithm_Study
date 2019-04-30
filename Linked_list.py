class Node:
    def __init__(self,data):
        self.data = data
        self.nextNode = None
        
    def __str__(self):
        string = str(self.data)
        n = self.nextNode
        while n != None:
            string+=(' -> '+str(n.data))
            n = n.nextNode
        return string
    
    def appendToTail(self,d):
        end = Node(d)
        n = self
        while n.nextNode :
            n = n.nextNode
        n.nextNode = end
        
    def deleteNode(self,d):
        n = self
        if n.data == d:
            return n.nextNode
        while n.nextNode :
            if n.nextNode.data == d:
                n.nextNode = n.nextNode.nextNode
                return self
            n = n.nextNode
        return self
    
    def removeDuplication(self):
        #using buffer
        n = self
        root = n
        buffer = set([n.data])
        while n.nextNode :
            if n.nextNode.data in buffer:
                n.nextNode = n.nextNode.nextNode
            else:
                buffer.add(n.nextNode.data)
                n = n.nextNode    
        #last item checking
        if n.data in  buffer:
            n=None
        return root
              
    def removeDuplication_2(self):
        #without buffer
        flag = False
        p2 = self
        while p2.nextNode :
            p1 = self
            flag = False
            while p1 != p2.nextNode:
                print(p1.data,p2.nextNode.data)
                if p1.data == p2.nextNode.data:
                    p2.nextNode = p2.nextNode.nextNode
                    flag = True
                    break
                p1 = p1.nextNode
            if not flag:
                p2 = p2.nextNode
        #last item
        p1 = self
        while p1 != p2:
            if p1.data == p2.data:
                p2 = None
            p1 = p1.nextNode
        return self