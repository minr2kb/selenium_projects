import math
def minimumBribes(q):
    # Write your code here
    count = 0
    i = len(q)-1
    while i >= 0:
        diff = q[i]-i-1
        if diff > 2:
            print("Too chaotic")
            return
        elif diff <= 0 :
            i -= 1
        else:
            q = q[:i]+q[i+1:i+1+diff]+q[i:i+1]+q[i+1+diff:]
            count += diff
    print(count)

def minimumBribes2(q):
    moves=0
    for i,p in enumerate(q):
        if p - i > 3:
            print("Too chaotic")
            return
        for j in range(max(p-2,0),i):
            if q[j] > p-1:
                moves += 1
    print(moves)

def minimumSwaps(arr):
    count = 0
    i = 0
    while i < len(arr):
        if arr[i]==(i+1):
            i+=1
            continue
        temp = arr[arr[i]-1]
        arr[arr[i]-1] = arr[i]
        arr[i] = temp
        count += 1
    return count

def arrayManipulation(n, queries):
    # Write your code here
    arr = [0 for elem in range(n)]
    for q in queries:
        arr = arr[:q[0]-1]+[i+q[2] for i in arr[q[0]-1:q[1]]]+arr[q[1]:]
    return arr

def solve(n,m):
    if n == 0 and m == 0:
        return 1
    elif n == 0:
        return solve(n,m-1)
    elif m == 0:
        return solve(n-1,m)
    else:
        return solve(n-1,m) + solve(n,m-1)

def solve2(n,m):
    res = math.factorial(n+m)//math.factorial(n)//math.factorial(m)
    # for i in range(n+1,n+m+1):
    #     num *= i
    # for j in range(1, m+1):
    #     den *= j
    # res = num//den
    return int(res % (10**9+7))

# n=5
# m=2
# print(solve(m,n))
# arr = ['asdf', 'sdfg']
# print(solve2(m,n))
# str = 'asdf'
# str= str + str[3]
# print(arr.count('asdf'))

# def passwordCracker(passwords, loginAttempt):
#     # Write your code here
#     head = 0
#     tail = 1
#     res = ''   
#     while True:
#         str = loginAttempt[head:tail]
#         if str in passwords:
#             res += str
#             head = tail
#             if tail == len(loginAttempt):
#                 return res.strip(' ')
#             else:
#                 res += ' '
#         else:
#             if tail == len(loginAttempt):
#                 return 'WRONG PASSWORD'
#             else:
#                 tail += 1

# def passwordCracker(passwords, loginAttempt):
#     # Write your code here
#     # head = 0
#     # tail = 1
#     res = ''   
#     while True:
#         for i in range(len(passwords)+1):
#             if i == len(passwords):
#                 return 'WRONG PASSWORD'
#             if loginAttempt[:len(passwords[i])]==passwords[i]:
#                 sub = loginAttempt[len(passwords[i]):]
#                 res += passwords[i]
#                 if sub == '':
#                     return res
#                 res += ' '
#                 loginAttempt = sub
#                 break

# lst = ['ab','ba']
# pw = "aba"
# print(passwordCracker(lst, pw))

# import re
# def makeDict():
#     f = open('corpus.txt', 'r')
#     dict = {}
#     while True:
#         line = f.readline()
#         if "END-OF-CORPUS" in line:
#             break
#         arr = re.split("[^a-zA-Z]", line)
#         for token in arr:
#             dict.setdefault(token.lower(),0)
#             dict[token.lower()] += 1
#     f.close()
#     return dict

# def delete(word):
#     for i in range(len(word)):
#         # for j in range(97,123):
#         print(word[:i]+ word[i+1:])

# def swap(word, i, j):
#     return word[:i]+word[j]+word[i]+word[j+1:]

# delete("abcd")
# print(swap("asdf", 1, 2))
# print(makeDict())
# print(1 != 0)
# for i in range(97,123):
#     print(chr(i))
# str = "asdf"
# str[1]='r'
# print(str)
# lst = 'asdf g'.split(' ')
# str = 'asdfgasdf'
# print(passwordCracker(lst,str))

# lst = [2, 1, 5, 3, 4]
# lst = [2, 3, 4, 1, 5]
# lst = [4,3,1,2]
# print(minimumSwaps(lst))

# lst = lst[:3]+[i+1 for i in lst[3:5]]+lst[5:]
# print(max(lst))

# arr = [[1,2,100], [5, 5, 100], [3,4,100]]
# print(arrayManipulation(5, arr))

# minimumBribes2(lst)
import re 

def makeDict():
    f = open('corpus.txt', 'r')
    dict = {}
    while True:
        line = f.readline()
        if "END-OF-CORPUS" in line:
            break
        arr = re.split("[^a-zA-Z\-\']", line)
        for token in arr:
            dict.setdefault(token.lower(),0)
            dict[token.lower()] += 1
    f.close()
    return dict

def correction(word, dict):
    if word in dict:
        return word
    else:
        answers = {}
        new = deletion(word, dict)
        if new != '':
            answers[new] = dict[new]
        new = transposition(word, dict)
        if new != '':
            answers[new] = dict[new]
        new = replacement(word, dict)
        if new != '':
            answers[new] = dict[new]
        new = insertion(word, dict)
        if new != '':
            answers[new] = dict[new]
        print(answers)
        if len(answers) == 0:
            return word
        else:
            lst = []
            for i in answers:
                if answers[i] == max(answers.values()):
                    lst.append(i)
            print(lst)
            return min(lst)
            
def deletion(word, dict):
    answers = {}
    for i in range(len(word)+1):
        for j in range(97,123):
            new = word[:i]+chr(j)+word[i:]
            if new in dict:
                answers[new] = dict[new]
    if len(answers) == 0:
        return ''
    else:
        lst = []
        for i in answers:
            if answers[i] == answers[max(answers)]:
                lst.append(i)
        return min(lst)
        
    
def replacement(word, dict):
    answers = {}
    for i in range(len(word)):
        for j in range(97,123):
            new = word[:i]+chr(j)+word[i+1:]
            if new in dict:
                answers[new] = dict[new]
    if len(answers) == 0:
        return ''
    else:
        lst = []
        for i in answers:
            if answers[i] == answers[max(answers)]:
                lst.append(i)
        return min(lst)

def swap(word, i, j):
    return word[:i]+word[j]+word[i]+word[j+1:]
    
def transposition(word, dict):
    answers = {}
    for i in range(len(word)-1):
        new = swap(word, i, i+1)
        if new in dict:
            answers[new] = dict[new]
    if len(answers) == 0:
        return ''
    else:
        lst = []
        for i in answers:
            if answers[i] == answers[max(answers)]:
                lst.append(i)
        return min(lst)
    
def insertion(word, dict):
    answers = {}
    for i in range(len(word)):
        new = word[:i]+word[i+1:]
        if new in dict:
            answers[new] = dict[new]
    if len(answers) == 0:
        return ''
    else:
        lst = []
        for i in answers:
            if answers[i] == answers[max(answers)]:
                lst.append(i)
        return min(lst)

dict = makeDict()
# print(dict)
print(dict['ccess'])
print(dict['bscess'])

# print("sence" in dict)

print(correction("bcess", dict))
# str = "asdf"
# str=str.lstrip('rr')
# print(str)

# ans = {}
# print(len(ans))
# lst = []
# ans['a'] = 0
# ans['b'] = 1
# ans['c'] = 1
# for i in ans:
#     if ans[i] == ans[max(ans)]:
#         lst.append(i)

# print(min(lst))
# print(dict['billty'])

# while True:
#     word = input()
#     print(correction(word, dict))

