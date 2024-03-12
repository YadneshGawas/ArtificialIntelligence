tree = {'A': [('B', 12), ('C', 14)], 'B': [('D', 7), ('E', 3)], 'C': [('F', 8), ('G', 2)], 'E': [('H', 0)], 'F': [('H', 0)], 'G': [('H', 0)]}
node = tree['A']
# print(node[1][0])
start = input('Enter the starting node: ')
goal = input('Enter the ending node: ')
open = []
close = []
def bestfs(tree,start,goal,open,close):
    if start not in open:
        print(start)
        close.append(start)
        neighbors = tree[start]
        for i in neighbors:
            if i[0] not in open:
                open.append(i)
    open.sort(key = lambda i: i[1])
    if open[0][0] == goal:
        print(open[0][0])
    else:
        node = open[0]
        bestfs(tree,node[0],goal,open,close)
open.remove(node)
