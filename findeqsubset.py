import math
def makeSet(A):
    B = []
    n = len(A)
    m = (int)(math.pow(2,n))
    for i in range(m):
        temp = []
        for j in range(n):
            if((i & (1<<j)) >0):
                temp.append(A[j])
        B.append(temp)
        if(findEq(A,temp)):
            return True
    else:
        return False
def findEq(A,B):
    temp = []
    for i in range(len(A)):
        if A[i] not in B:
            temp.append(A[i])
    if sum(temp) is sum(B):
        return True
list1 = [1,2,2,4]
print(makeSet(list1))
#for i in range(len(list2)):
#    temp=[]
#    for j in range(len(list1)):
#        if list1[j] not in list2[i]:
#            temp.append(list1[j])
#    if(sum(list2[i]) is sum(temp)):
#        print(list2[i],temp)
#        break
