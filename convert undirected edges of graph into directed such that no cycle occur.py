from sys import stdin
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt
#tt = int(stdin.readline())
tt=1
 
for loop in range(tt):
    #G=nx.DiGraph();
    Query = []
    ans = []
    t1=[]
 
    n,m = map(int,stdin.readline().split())
    n+=1
    lis = [ [] for i in range(n) ]
    inum = [0] * n
    ilis = inum
    index = [None] * n
 
    for i in range(m):
 
        st,x,y = map(int,stdin.readline().split())
        
        if st == 1:
            ilis[y] += 1
            lis[x].append(y)
            ans.append((x,y))
            t1.append((x,y))
        else:
            Query.append( (x,y) )
            t1.append((x,y))
    
 
    endnum = 0
    q = deque([])
    for i in range(n):
        if ilis[i] == 0:
            q.append(i)
    while len(q) > 0:
        v = q.popleft()
        index[v] = endnum
        endnum += 1
 
        for nex in lis[v]:
            inum[nex] -= 1
            if inum[nex] == 0:
                q.append(nex)
    #G.add_edges_from(t1)
    #pos = nx.spring_layout(G)
    #nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'), 
          #            node_size = 500)
    #nx.draw_networkx_labels(G, pos)
    #nx.draw_networkx_edges(G, pos, edgelist=Query, edge_color='r', arrows=False)
    #nx.draw_networkx_edges(G, pos, edgelist=ans, arrows=True)
    #plt.show()
    result=[]
    if endnum != n:
        print ("NO")
    else:
        print ("YES")
        
        for x,y in Query:
            if index[x] < index[y]:
                ans.append((x,y))
            else:
                ans.append((y,x))
        G1=nx.DiGraph()
        G1.add_edges_from(ans)
        pos1 = nx.spring_layout(G1)
        nx.draw_networkx_nodes(G1, pos1, cmap=plt.get_cmap('jet'), node_size = 200)
        nx.draw_networkx_labels(G1, pos1)
                  #nx.draw_networkx_edges(G1, pos, edgelist=Query, edge_color='r', arrows=False)
        nx.draw_networkx_edges(G1, pos1, edgelist=ans, arrows=True)
        plt.show()
        

        
