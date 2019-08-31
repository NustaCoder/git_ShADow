def convertToBinary(val):
    st=""
    s=len(str(val))
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
    while(len(st) <= s):
        st += "0"
    return st[ : :-1]

def solution(N):
    bir = convertToBinary(N)
    cnt=0
    tmp=0
    for i in bir:
        if (i == "0"):
            tmp+=1
        elif (i == "1"):
            if cnt < tmp:
                cnt = tmp
            tmp = 0
    return cnt
print(solution(1041))