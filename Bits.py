5.1
def insert(N, M, i, j):
    M <<= i
    mask = N | (-1 << i)
    N = N & (-1<<j)
    N |= M
    N &= mask
    return N

'''
if __name__ == '__main__':
    N = 1024
    M = 19
    i = 2
    j = 6
    print(format(insert(N,M,i,j),'b'))
'''

#5.2
def to_binary(N):
    ans = "0."
    cur = 0.5
    cnt = 2
    while N>0:
        if cnt == 32:
            return 'Error'
        if N>=cur:
            ans += "1"
            N -= cur
        else:
            ans += "0"
        cur /= 2
        cnt +=1
    return ans

'''
if __name__ == '__main__':
    print(to_binary(0.72))
    print(to_binary(0.875))
'''

#5.3
def solution(N):
    N = format(N,'b')
    print(N)
    lst = [0]*len(N)
    if N[0] == '1':
        lst[0] = 1
    max_length = 0
    temp = None
    
    for i in range(1,len(N)):
        if N[i] == '1':
            lst[i] = lst[i-1]+1
        else:
            if temp == None :
                temp = 0
            if temp + 1 + lst[i-1] > max_length :
                max_length = temp + 1 + lst[i-1]
            temp = lst[i-1]
    if temp !=None :
        if temp + 1 + lst[-1] > max_length :
            max_length = temp + 1 + lst[-1]
    if temp == None:
        max_length = lst[-1]
    return max_length

'''
if __name__ == '__main__':
    print(solution(799))
    #print(solution(31))
    #print(solution(100))
'''

#5.5
''' 
n & (n-1) 의 값이 0이 되기 위해서는 n의 가장 왼쪽 비트만 1, 나머지는 0 이어야 한다.
따라서 n = 2^k 인 수여야 한다.
'''

#5.6
def solution_6(a,b):
    n = a^b
    count = 0
    while n > 0:
        count += 1
        n = n & (n-1)
    return count

'''
if __name__ == '__main__':
    print(solution_6(29,15))
    print(solution_6(15,20))
'''

#5.7
def solution_7(N):
    pattern = int("10"*32,2)
    print(((N & pattern)<<1))
    print(((N & (pattern<<1))>>1))
    return ((N & pattern)<<1) | ((N & (pattern<<1))>>1)

'''
if __name__ == '__main__':
    print(solution_7(23))
    print(solution_7(16))
'''
