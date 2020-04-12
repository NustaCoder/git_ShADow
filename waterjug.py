from copy import deepcopy

def fillJug(x):
    global jug_a
    global jug_b
    return [[jug_a, x[1]], [x[0], jug_b]]
    
def emptyJug(x):
    global jug_a
    global jug_b
    return [[0, x[1]], [x[0], 0]]
    
def transfer(x):
    global jug_a
    global jug_b
    temp = []
    t1 = jug_a - x[0]
    t2 = jug_b - x[1]

    if t1 == 0 or t2 == 0:
        temp.append([x[0],x[1]])
    if t2 < x[0]:
        temp.append([x[0]-t2, x[1]+t2])
    if t2 > x[0]:
        temp.append([0, x[1]+x[0]])
    if t1 < x[1]:
        temp.append([x[0]+t1, x[1]-t1])
    if t1 > x[1]:
        temp.append([x[0]+x[1], 0])

    return temp

jug_a, jug_b = 5, 4
ini_a, ini_b = 0, 0
goal_a, goal_b = 2, 0
main_lst = [[ini_a, ini_b]]
st, ed = 0, 1
while True:
    temp_one = deepcopy(main_lst[st:ed])
    temp_two = []
    temp_three = []
    
    for i in temp_one:
        temp_two.extend(fillJug(i))
        temp_two.extend(emptyJug(i))
        temp_two.extend(transfer(i))
    
    if [goal_a, goal_b] in temp_two:
        print('yuuss')
        break
    else:
        cnt = 0
        for i in temp_two:
            if i not in main_lst:
                main_lst.append(i)
                cnt += 1
    
    st = ed
    ed += cnt
    if cnt == 0:
        print("no solution")
        break
