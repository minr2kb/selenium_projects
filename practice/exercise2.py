def arrayManipulation(n, queries):
    # Write your code here
    high = max([int(p[1]) for p in queries])
    low = min([int(p[0]) for p in queries])-1
    arr = [0 for elem in range(int(n))]
    for q in queries:
        arr = arr[:int(q[0])-1]+[i+int(q[2]) for i in arr[int(q[0])-1:int(q[1])]]+arr[int(q[1]):]
    return max(arr[low:high])
    # return arr[low:high]

def test():
    f = open('practice/testcase.txt', 'r')
    lst = []
    n = f.readline().split(' ')[1]
    while True:
        line = f.readline()
        if line == '':
            break
        lst.append(line.split(' '))
    f.close()
    return n, lst

n, queries = test()
print(arrayManipulation(n,queries))