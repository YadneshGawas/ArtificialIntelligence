graph = [
    ['A', 'H', 7, 0], ['A', 'B', 1, 3], ['A', 'C', 2, 4],
    ['B', 'E', 6, 6], ['B', 'D', 4, 2],
    ['C', 'F', 3, 3], ['C', 'G', 2, 1],
    ['D', 'E', 7, 6],
    ['F', 'H', 1, 0],
    ['G', 'H', 2, 0]
]

temp = set()
temp1 = set()
for i in graph:
    temp.add(i[0])
    temp.add(i[1])
nodes = temp.union(temp1)
cost = dict()
path = dict()
for i in nodes:
    cost[i] = 99
    path[i] = ' '

start = input('Enter the starting node: ')
goal = input('Enter the goal node: ')
close = set()
cost[start] = 0
path[start] = start


def a_star(graph, open, close, cost, current_nodes):
    if current_nodes in open:
        open.remove(current_nodes)
    close.add(current_nodes)
    for i in graph:
        if (i[0] == current_nodes & cost[i[0] + i[2] + i[3] < cost[i[1]]):
            open.add(i[1])
            cost[i[1]] = cost[i[0]+i[2]+i[3]]
            path[i[1]] = path[i[0]]+'->'+i[1]
