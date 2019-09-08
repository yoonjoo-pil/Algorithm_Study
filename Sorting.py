#10.1
def merge(a,b):
    index_a = len(a)-1
    index_b = len(b)-1
    a += [0]*len(b)
    index = index_a + index_b + 1

    while index_b >= 0:
        if index_a >= 0 and a[index_a] > b[index_b]:
            a[index] = a[index_a]
            index_a -= 1
        else:
            a[index] = b[index_b]
            index_b -= 1
        index -= 1
    return a

'''
if __name__ == '__main__':
    a = [2,4,6,10]
    b = [1,3,8]
    print(merge(a,b))
'''

#10.2 아직 수정중
def anagram(string_lst):
    dict_list = []
    for string in string_lst:
        temp = dict()
        for s in string:
            if s in temp:
                temp[s] += 1
            else:
                temp[s] = 1
        if temp in dict_list:
            anagrams = dict_list[temp]
            anagrams.append(string)
            dict_list[temp] = anagrams
        else:
            dict_list[temp] = [string]
    print(dict_list)
'''
if __name__ == '__main__':
    anagram(["abcd","egf","bcda","rf","fge"])
'''
#10.3
def sol_3(lst, item):
    n = len(lst)
    print(search_3(lst, item, 0, n-1))

def search_3(lst, item, start, end):
    mid = (start + end)//2
    if start > end :
        return "No item"
    if lst[mid] == item :
        return mid
    
    if lst[start] <= lst[mid]:
        if lst[start] <= item and lst[mid]>=item:
            return search_3(lst,item,start, mid-1)
        else:
            return search_3(lst,item,mid+1,end)
    
    else:
        if lst[mid]<=item and lst[end]>=item:
            return search_3(lst,item,mid+1,end)
        
        else:
            return search_3(lst, item, start, mid-1)

'''
if __name__ == '__main__':
    sol_3([3,5,7,10,1,2],10)
    sol_3([4,5,6,10,11,23,1,3],5)
    sol_3([15,16,19,20,25,1,3,4,5,7,10,14],5)
'''

#10.4
class Listy():
    def __init__(self, lst):
        self.lst = lst
    def elementAt(self,i):
        if 0<=i<=len(self.lst):
            return self.lst[i]
        return -1

def sol_4(listy, x):
    start, i = 0, 0
    while True:
        temp = listy.elementAt(i**2)
        if temp == x :
            return i**2
        elif temp == -1 :
            end = i**2
            break
        elif temp > x :
            end = i**2 - 1
            break
        elif temp < x :
            start = i**2 + 1
        i += 1
    
    while start < end :
        mid = (start + end)//2
        temp = listy.elementAt(mid)
        if temp  == x:
            return mid
        elif temp > x :
            end = mid - 1
        else :
            start = mid + 1
    return "No item"

'''
if __name__ == '__main__':
    listy = Listy([1,3,5,7,9,11,13,20])
    print(sol_4(listy, 5))
    print(sol_4(listy, 20))
'''

#10.5
def sol_5(target, lst,start=0,end=None):
    if end == None:
        end = len(lst)
    mid = (start+end)//2
    if start > end :
        return -1
    if lst[mid] == "":
        left = mid-1
        right = mid+1
        while True:
            if left < start and right > end:
                return -1
            elif left >= start and lst[left]!="":
                mid = left
                break
            elif right<=end and lst[right]!="":
                mid = right
                break
            left -= 1
            right +=1
    
    if lst[mid] == target :
        return mid
    elif lst[mid] < target :
        return sol_5(target, lst,mid+1,end)
    else:
        return sol_5(target,lst,start,mid-1)
    
'''
if __name__ == "__main__":
    print(sol_5("ban",["","","a","abc","banana","","pineapple"]))
'''

#10.8
def sol_8(lst):
    n= len(lst)
    check = [None]*n
    ans = []
    for i in range(n):
        temp = lst[i]
        if not check[temp-1]:
            check[temp-1] = 1
            ans.append(temp)
    return ans

'''
if __name__ == '__main__':
    print(sol_8([1,1,3,5,6,7,8,9,9,4]))
'''

#10.9 무한 loop 수정 필요
def sol_9(mat,target):
    row, col = 0, 0
    row_index, col_index = 0, 0
    
    while row < len(mat) and col < len(mat[0]):
        print(row,col)
        if mat[row][col_index] == target:
            return (row,col_index)
        elif mat[row][col_index] < target:
            if col_index+1 < len(mat[0]):
                col_index += 1
        else:
            if row- 1 >= 0:
                row -= 1
        if mat[row_index][col] ==target:
            return (row_index,col)
        elif mat[row_index][col]<target:
            if row_index + 1 < len(mat):
                row_index += 1
        else:
            if col - 1 >= 0 :
                col-= 1
    return False

#10.11
def sol_11(lst):
    lst.sort()
    for i in range(1,len(lst),2):
        lst[i], lst[i-1] = lst[i-1], lst[i]
    return lst

'''
if __name__ == '__main__':
    print(sol_11([2,4,6,1,3,5]))
'''
