GRAPH = {'Arad':[['Zerind',374],['Timisoara',329],['Sibiu',253]],
         'Zerind':[['Oradea',380],['Arad',366]],
         'Oradea':[['Sibiu',253]],
         'Sibiu':[['Rimniciu Vilcea',193],['Fagaras',178],['Arad',366]],
         'Fagaras':[['Sibiu',253],['Bucharest',0]],
         'Rimniciu Vilcea':[['Pitesti',98],['Craiova',160],['Sibiu',253]],
         'Timisoara':[['Lugoj',244],['Arad',366]],
         'Lugoj':[['Mehadia',241]],
         'Mehadia':[['Lugoj',244],['Dorbeta',242]],
         'Dobreta':[['Mehadia',241],['Craiova',160]],
         'Pitesti':[['Craiova',160],['Bucharest',0]],
         'Craiova':[['Pitesti',98],['Dobreta',242],['Rimniciu Vilcea',193]],
         'Bucharest':[['Giurgiu',77],['Urziceni',80],['Fagaras',178],['Pitesti',98]],
         'Giurgiu': [['Bucharest',0]],
         'Urziceni':[['Vaslui',199],['Hirsova',151],['Bucharest',0]],
         'Vaslui':[['Lasi',226],['Urziceni',80]],
         'Lasi':[['Neamt',234],['Vaslui',199]],
         'Neamt':[['Lasi',226]],
         'Hirsova':[['Eforie',161],['Urziceni',80]],
         'Eforie':[['Hirsova',151]]
}

def gbfs(GRAPH, start, end):
    explored = []
    queue = [start]
    while queue:
        print (queue)
        node = queue.pop(0)
        if node not in explored:
            explored.append(node)
            if node == end:
                break
            neighbors = GRAPH[node]
            neighbors.sort(key=lambda a: a[1])
            print (neighbors)
            queue=neighbors.pop(0)

    print(explored)
 
Start = input("Enter Starting node ")
End = input("Enter Ending node ")
print()
print("GBFS from staring node to goal node" )
gbfs(GRAPH, Start, End)