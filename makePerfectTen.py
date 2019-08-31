val = input()
tmp = 10 - int(val)
if tmp > 0:
    val+=str(tmp)
print(val)
arr=[int(i) for i in range(3,10) if(i%j!=0 for j in range(2,j)) ]
print(arr)