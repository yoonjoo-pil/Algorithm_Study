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
            return search_3(lst,item.mid+1,end)
        
        else:
            return search_3(lst, item, start, mid-1)

if __name__ == '__main__':
    sol_3([3,5,7,10,1,2],10)
    sol_3([4,5,6,10,11,23,1,3],5)