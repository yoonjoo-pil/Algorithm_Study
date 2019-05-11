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
        return root
              
    def removeDuplication_2(self):
        #without buffer
        flag = False
        p2 = self
        while p2.nextNode :
            p1 = self
            flag = False
            while p1 != p2.nextNode:
                if p1.data == p2.nextNode.data :
                    p2.nextNode = p2.nextNode.nextNode
                    flag = True
                    break
                p1 = p1.nextNode
            if not flag:
                p2 = p2.nextNode
        return self
    
    def size(self) :
        n = self
        num =1
        n = n.nextNode
        while n :
            num += 1
            n = n.nextNode
        return num
    
    def append_list(self, lst) :
        head = self
        while head.nextNode :
            head = head.nextNode
        head.nextNode = lst 

    def search_kth_item(self,k) :
        p1 = self
        p2 = self

        for i in range(k) :
            if p1 == None :
                print("Out of bound")
                return
            p1 = p1.nextNode
        
        while p1 :
            p1 = p1.nextNode
            p2 = p2.nextNode
        return p2.data

    def delete_midterm(self, node) :
        if node == None or node.nextNode == None :
            print("Impossible")
            return
        node.data = node.nextNode.data
        node.nextNode = node.nextNode.nextNode
        return node
        
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
    
    #Linked_list의 head 자체가 변경되지는 않는다.
    def divide_2(self,x) :
        n = self
        head = self
        tail = self
        while n :
            next_node = n.nextNode
            if n.data < x :
                n.nextNode = head
                head = n
            else :
                tail.nextNode = n
                tail = n
            n = next_node

        tail.nextNode = None
        return head

    def sum_of_lists(self,lst1, lst2) :
        n1, n2 = lst1, lst2
        sum_lst = Node((n1.data + n2.data) % 10)
        temp = (n1.data + n2.data) // 10
        n1 = n1.nextNode
        n2 = n2.nextNode
        while n1 :
            if not n2 :
                print("Check to inputs")
                return
            n_term = n1.data + n2.data + temp
            temp, value =n_term // 10, n_term % 10
            sum_lst.appendToTail(value)

            n1 = n1.nextNode
            n2 = n2.nextNode
        
        if temp :
            sum_lst.appendToTail(temp)
        return sum_lst

    def check_palindrome(self) :
        slow, fast = self, self.nextNode
        stack = []
        while fast :
            stack.append(slow.data)
            if not fast.nextNode :
                break
            fast = fast.nextNode.nextNode
            slow = slow.nextNode
        
        slow = slow.nextNode
        while slow :
            item = stack.pop()
            if item != slow.data :
                return False
            slow = slow.nextNode
        return True

    def find_intersection(self, node1, node2) :
        n1, n2 = node1, node2
        #check intersection
        while n1.nextNode or n2.nextNode :
            if n1.nextNode :
                n1 = n1.nextNode
            if n2.nextNode :
                n2 = n2.nextNode
        
        if n1 != n2 :
            return False
        #find intersection
        n1, n2 = node1, node2 
        size1 = n1.size()
        size2 = n2.size()
        if size1 > size2 :
            for i in range(size1-size2, 0, -1) :
                n1 = n1.nextNode
        else :
            for i in range(size2-size1, 0, -1) :
                n2 = n2.nextNode
        
        while n1 :
            if n1 == n2 :
                return n1
            n1 = n1.nextNode
            n2 = n2.nextNode
    
    def find_loop(self) :
        slow = self
        fast = self.nextNode
        while fast and fast.nextNode :
            slow = slow.nextNode
            fast = fast.nextNode.nextNode
            if slow == fast :
                break
        if fast == None or fast.nextNode == None :
            return None
        
        slow = self
        fast = fast.nextNode
        while slow != fast :
            slow = slow.nextNode
            fast = fast.nextNode
        
        return fast.data
