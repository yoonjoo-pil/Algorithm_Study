#8.8
def make_dic(s):
    dic = dict()
    for i in s:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    permutation(dic,len(s))

def permutation(dic,remaining, substring=""):
    if remaining == 0:
        print(substring)
        return
    
    for char in dic :
        temp = dic[char]
        if temp > 0:
            dic[char] -= 1
            permutation(dic,remaining-1,substring+char)
            dic[char] = temp
'''
if __name__ == '__main__':
    make_dic("aabc")
'''

#8.9
def parenthesis(left, right, string, index):
    if left<0 or right < left :
        return
    if left == right and left == 0:
        print(string)
    else:
        string[index] = '('
        parenthesis(left-1, right,string,index+1)
        string[index] = ')'
        parenthesis(left,right-1,string,index+1)

def make_paren(n):
    string = [0]*(2*n)
    parenthesis( n,n,string,0)

if __name__ == '__main__':
    make_paren(4)
