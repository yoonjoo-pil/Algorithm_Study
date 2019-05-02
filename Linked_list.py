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
    
    def size(self) :
        n = self
        num =1
        n = n.nextNode
        while n :
            num += 1
            n = n.nextNode
        return num
    
    #포인터 2개 써서 좀 더 효율적으로 해보기.
    def search_kth_item(self,k) :
        p1 = self
        n = self.size()
        #순차 잡근이 더 빠른 케이스
        if k > n//2 :
            num = 1
            while num < n-k+1 :
                p1 = p1.nextNode
                num +=1
        #뒤에서부터 접근하는 케이스
        else :
            p2 = self.nextNode
            while p2 :
                if p2.nextNode == None :
                    break
                p2 = p2.nextNode.nextNode
                p1 = p1.nextNode
            num = n//2
            while num >= k :
                p1 = p1.nextNode
                num -= 1
        
        return p1.data
    #완성 못함
    def delete_midterm(self) :
        p1 = self
        if p1.size()<=2 :
            return False
        pass

    def divide(self,x) :
        pivot = self
        while pivot :
            if pivot.data >= x :
                p = pivot.nextNode
                while p :
                    if p.data < x :
                        pivot.data, p.data = p.data, pivot.data
                        break
                    else :
                        p = p.nextNode
            pivot = pivot.nextNode
        return self 
    
    def sum_of_lists(self,lst1, lst2) :
        n1, n2 = lst1, lst2
        temp = n1.data + n2.data
        if temp >= 10 :
            sum_lst = Node(temp%10)
            temp = temp//10
        else :
            sum_lst = Node(temp)
        
        pass
