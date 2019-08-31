import math
#create a power set and return the multiplication value
def findPowerSet(a):
    s = len(a)
    p = (int) (math.pow(2, s))
    m = 0
    for i in range(p):
        cnt = 1
        tmp = convertToBinary(i,s)
        if(tmp.count("1") is 3):
            for j in range(s):
                if int(tmp[j]) is 1:
                    cnt *= a[j]
            if(cnt > m):
                m = cnt
    return m

#def isThreeBit(n):
#    cnt = 0
#    while(n != 0):
#        n = n & (n-1)
#        cnt += 1
#    if(cnt == 3):
#        return True

def convertToBinary(val,s):
    st=""
    while(val > 0):
        if(val % 2 == 0):
            st += "0"
            val = int(val / 2)
        elif(val == 1):
            st += "1"
            break
        else:
            st += "1"
            val = int(val / 2)
    while(len(st) != s):
        st += "0"
    return st[ : :-1]
list1 = [2,2,1,2]
print(findPowerSet(list1))