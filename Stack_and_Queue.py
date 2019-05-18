#Stack 
class Node() :
    def __init__(self, data=None) :
        self.data = data
        self.nextNode = None
        self.minVal = None

class Stack() :

    def __init__(self) :
        self.size = 0
        self.top = None
    def pop(self) :
        if self.top :
            item = self.top.data
            self.top = self.top.nextNode
        self.size -= 1
        return item

        return "Empty stack"
    
    def push(self, data) :
        new_node = Node(data)
        new_node.nextNode = self.top
        self.top = new_node
        self.size += 1
    
    def peek(self) :
        if self.top :
            return self.top.data
        else :
            return 'Empty stack'
    
    def isEmpty(self) :
        return self.top == None
    
class Queue() :
    first = None
    last = None
    
    def add(self, data) :
        new_node = Node(data)
        if not self.first :
            self.first = new_node
            self.last = new_node
        else :
            self.last.nextNode = new_node
            self.last = new_node
    
    def remove(self) :
        if self.first :
            item = self.first.data
            self.first = self.first.nextNode
            if self.first == None :
                last = self.first
            return item
        return "Empty queue" 

    def peek(self) :
        if self.first :
            item = self.first.data
            return item
        return "Empty "

    def isEmpty(self) :
        return self.first == None


#3.1 한 개로 세 개
#각 스택은 100 만큼의 크기를 갖는다. 
class stackList() :

    def __init__(self) :
        self.numstacks = 3
        self.array = [None] * 100 * 3
        self.tops = [-1] * 3

    def push(self, index, data) :
        if self.tops[index] == (index + 1) * 100 - 1 :
            print("This Stack is full")
            return
        self.array[self.tops[index] + 1 + index * 100] = data
        self.tops[index] += 1

    def pop(self, index) :
        if self.isEmpty(index) :
            print("Empty stack")
            return
        pointer = self.tops[index] + index * 100
        data = self.array[pointer]
        self.array[pointer] = None
        self.tops[index] -= 1
        return data

    def peek(self, index) :
        if self.isEmpty(index) :
            print("Empty stack")
            return
        return self.array[self.tops[index] + index * 100]
    
    def isEmpty(self, index) :
        return self.tops[index] == -1 

'''
if __name__=='__main__' :
    stack_lst = stackList()
    for i in range(3) :
        print(stack_lst.isEmpty(i))
    for i in range(3) :
        stack_lst.push(i, 2*i)
        stack_lst.push(i, 3*i)
    for i in range(3) :
        print(stack_lst.pop(i))
    for i in range(3) :
        print(stack_lst.peek(i))
    for i in range(3) :
        print(stack_lst.isEmpty(i))
'''

class Stack_Mins() :
    top = None 
    min_point = None

    def __init__(self) :
        self.size = 0

    def pop(self) :
        if self.top :
            item = self.top.data
            self.top = self.top.nextNode
        self.size -= 1
        return item

        return "Empty stack"
    
    # Not O(1)  - 다시 수정해보기.
    def push(self, data) :
        new_node = Node(data)
        new_node.nextNode = self.top
        self.top = new_node
        self.size += 1
        if data < self.min_point.data :
            new_node.minVal = self.min_point
            self.min_point = new_node
        else :
            temp = self.min_point.minVal
            while data >= temp.data : 
                if temp.minVal :
                    temp = temp.minVal
                else :
                    temp.minVal = new_node
                    return
            new_node.minVal = temp.minVal
            
            
    
    def peek(self) :
        if self.top :
            return self.top.data
        else :
            return 'Empty stack'
    
    def isEmpty(self) :
        return self.top == None

#3.3 SetofStacks
# 1 stack contains 5 items
class SetOfStacks() :

    limit = 5
    def __init__(self) :
        self.stack_lst = []

    def push(self, data) :
        if self.isEmpty() :
            self.stack_lst.append(Stack())
        last_stack = self.stack_lst[-1]
        if last_stack.size == self.limit :
            self.stack_lst.append(Stack())
            last_stack = self.stack_lst[-1]
        last_stack.push(data)

    def pop(self) :
        last_stack = self.stack_lst[-1]
        item = last_stack.pop()
        if last_stack.isEmpty() :
            self.stack_lst.pop()
        return item
    
    def peek(self) :
        last_stack = self.stack_lst[-1]
        return last_stack.peek()
    
    def isEmpty(self) :
        return self.stack_lst == []

'''
if __name__ == '__main__' :
    stacks = SetOfStacks()
    print(stacks.isEmpty())
    for i in range(12) :
        stacks.push(i)
    for i in range(8) :
        print(stacks.pop())
    
    print(stacks.peek())
    print(stacks.isEmpty())
'''

#3.4 스택2개로 큐 1개 구현
class MyQueue() :
    def __init__(self) :
        self.stack1 = Stack()
        self.stack2 = Stack()
    
    def push(self, data) :
        self.stack1.push(data)
    
    def pop(self) :
        while not self.stack1.isEmpty() :
            self.stack2.push(self.stack1.pop())
        return self.stack2.pop()
    
    def peek(self) :
        while not self.stack1.isEmpty() :
            self.stack2.push(self.stack1.pop())
        item = self.stack2.peek()
        return item
    
    def isEmpty(self) :
        return self.stack1.isEmpty() and self.stack2.isEmpty()
'''
if __name__ == '__main__' :
    stack = MyQueue()
    for i in range(4) :
        stack.push(i)
    print(stack.pop())
    print(stack.peek())
    print(stack.isEmpty())
'''

# 3.5 스택 정렬
def sorting_stack(stack) :
    sorted_stack = Stack()
    while not stack.isEmpty() :
        item = stack.pop()
        while (not sorted_stack.isEmpty()) and item > sorted_stack.peek() :
            stack.push(sorted_stack.pop())
        sorted_stack.push(item)
    output = str(sorted_stack.pop())
    while not sorted_stack.isEmpty() :
        output += "- > " + str(sorted_stack.pop())
    return output

'''
if __name__ == '__main__' :
    s = Stack()
    for i in [3,4,1,5,2,8] :
        s.push(i)
    print(sorting_stack(s)) #작은 수부터 출력됨.
'''

#3.6 동물 수용소
class AnimalShelter() :
    order = 1
    def __init__(self) : 
        self.dog = Queue()
        self.cat = Queue()

    def enqueue(self, animal) :
        if animal == 'dog' :
            self.dog.add((animal,self.order))
            self.order += 1
        elif animal == 'cat' :
            self.cat.add((animal,self.order))
            self.order += 1
        else :
            print("Check the type of animal")
            return

    def dequeueAny(self) :
        c, d = None, None
        if not self.cat.isEmpty() :
            c = self.cat.peek()
        if not self.dog.isEmpty() :
            d = self.dog.peek()
        if c :
            if d :
                if c[1] < d[1] :
                    return self.cat.remove()
                else :
                    return self.dog.remove()
            return self.cat.remove()
        else :
            if d :
                return self.dog.remove()
        return "Empty queue"
    
    def dequeueDog(self) :
        if self.dog.isEmpty() :
            return "Empty Dog Queue"
        return self.dog.remove()
    
    def dequeueCat(self) :
        if self.cat.isEmpty() :
            return 'Empty Cat Queue'
        return self.cat.remove()

if __name__ == '__main__' :
    ani = AnimalShelter()
    for animal in ["cat","dog","dog", "dog", "cat", "cat"] :
        ani.enqueue(animal)
    print(ani.dequeueAny())
    print(ani.dequeueAny())
    print(ani.dequeueDog())
    print(ani.dequeueCat())
    print(ani.dequeueAny())
