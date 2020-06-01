import collections
import random

cord_node = []
def cord():
    arr = []
    with open('SCOTPOS.txt','r') as f:
        for line in f:
            list = []
            for word in line.split():
                list.append(word)
            cord = tuple(list)
            cord_node.append(cord)         
cord()

def conv(node):
    return ((cord_node[node][1],cord_node[node][2]))


def start():
    arr = []
    start_station = [103,112,34,155,94,117,132,53,174,198,50,91,26,29,141,13,138,197]
    num = 6
    random_start = random.sample(start_station, num)
    start1 = random_start[0]
    start2 = random_start[1]
    start3 = random_start[2]
    start4 = random_start[3]
    start5 = random_start[4]
    mr_x = random_start[5]
    arr.append(cord_node[start1])
    arr.append(cord_node[start2])
    arr.append(cord_node[start3])
    arr.append(cord_node[start4])
    arr.append(cord_node[start5])
    arr.append(cord_node[mr_x])
    return arr

def map():
    sgraph = {}
    cord_node = []
    arr = []
    with open('SCOTMAP.txt','r') as f:
        for line in f:
            list = []
            for word in line.split():
                list.append(word)
            cord = tuple(list)
            cord_node.append(cord)
    graph = {}
    for i in range(470):
        u = cord_node[i][0]
        v = cord_node[i][1]
        w = cord_node[i][2]
        graph.setdefault(u,[]).append((v,w))
        graph.setdefault(v,[]).append((u,w))
    sgraph = collections.OrderedDict(sorted(graph.items()))
    return sgraph


card_det = []
for i in range(5):
    card_det.append((10,8,4)) # order of card is taxi bus underground
card_x = (4,3,3,2,5) # order is taxi bus underground double move and black

def poss_mov_det(curr_pos,det_no):
    rem_taxi = card_det[det_no-1][0]
    rem_bus = card_det[det_no-1][1]
    rem_und = card_det[det_no-1][2]
    graph = map()
    lis = []
    lis = graph[curr_pos]
    m = []
    for i in range(len(lis)):
        mode = lis[i][1]
        if mode == 'T' and rem_taxi>0:
            m.append(lis[i])
        if mode == 'B' and rem_bus>0:
            m.append(lis[i])
        if mode == 'U' and rem_und>0:
            m.append(lis[i])
    return m

def update(move,det_no):
    mode = move.split(" ")
    l = card_det[det_no-1]
    lst = list(l)
    if mode[1] == 'T':
        lst[0] = lst[0]-1
    if mode[1] == 'B':
        lst[1] = lst[1]-1
    if mode[1]=='U':
        lst[2] = lst[2]-1
    l = tuple(lst)
    card_det[det_no-1] = l