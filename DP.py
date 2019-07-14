#8.1
def triple_step(n):
    steps = [1,2,4] + [0]*(n-3)
    for i in range(3,n):
        steps[i] = steps[i-3] + steps[i-2] + steps[i-1]
    return steps[-1]
'''
if __name__ =='__main__':
    print(triple_step(4))
    print(triple_step(10))
'''

#8.3
def magic_index(array):
    return find_index(0,len(array)-1,array)

def find_index(start,end,array):
    i = (end + start)//2 
    if array[i] == i :
        return i
    elif array[i] < i:
        return find_index(i+1,end,array)
    else:
        return find_index(start,i-1,array)
'''
if __name__ == '__main__':
    print(magic_index([-2,-1,2,4,6,8]))
    print(magic_index([-2,-1,0,1,3,5]))
'''

#8.4
def powerset(s):
    included = [False]*len(s)
    find_subset(0,included,s)

def find_subset(k,included,s):
    if k == len(s) :
        for i in range(k):
            if included[i]:
                print(s[i],end=' ')
        print()
        return
    else:
        included[k] = False
        find_subset(k+1,included,s)
        included[k] = True
        find_subset(k+1,included,s)
'''
if __name__ == '__main__':
    powerset(['a','b','c'])
    powerset(['1','2','3','4'])
'''

#8.5
def recursive_mul(n,m):
    pass



#8.7
def permutation(s,index=0):
    s = list(s)
    if index == len(s):
        print(s)
        return
    
    for i in range(index, len(s)):
        s[i], s[index] = s[index], s[i]
        permutation(s,index+1)
        s[i], s[index] = s[index], s[i]

if __name__ == '__main__':
    permutation("abcd")