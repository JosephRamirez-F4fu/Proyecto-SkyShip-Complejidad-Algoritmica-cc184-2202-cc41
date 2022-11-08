INF=10**5

class G:
    def __init__(self,data,dirigido=False):
        self.nV=len(data)
        self.G=[]
        self.data=data
        self.dirigido=dirigido
        for i in range(len(data)):
            self.G.append([INF]*len(data))
    
    def set_h_adj_list(self,h,adjlist):
        self.h=h
        self.adjac_lis=adjlist

    def set_matrix(self):
        self.G=[]
        for i in range(self.nV):
            self.G.append([INF]*len(self.nV))

    def add_edge(self,v,w,g=1):
        if v in self.data and w in self.data :
            self.G[v][w]=g
            if self.dirigido ==False:
                self.G[w][v]=g  

    def dfs_ma(self,r):
        n = len(self.G)
        visitado = [False]*n
        camino = [-1]*n
        visitado[r] = True
        pila=[r]
        if r in self.data:
            visitado[r]=True
            while pila :
                u = pila.pop()
                for v in range(n):
                    if self.G[u][v]!=0 and not visitado[v]:
                        visitado[v]=True
                        camino[v]=u
                        pila.append(v)
        return camino
    
    def get_neighbors(self, v):
        return self.adjac_lis[v]
 
    def h(self, n):
        return self.H[n]
 
    def a_star_algorithm(self, start, stop):
        open_lst = set([start])
        closed_lst = set([])
        poo = {}
        poo[start] = 0
        par = {}
        par[start] = start
 
        while len(open_lst) > 0:
            n = None 
            for v in open_lst:
                if n == None or poo[v] + self.h[v] < poo[n] + self.h[n]:
                    n = v;
 
            if n == None:
                print('Path does not exist!')
                return False

            if n == stop:
                reconst_path = []
 
                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]
 
                reconst_path.append(start)
 
                reconst_path.reverse()
 
                print('Path found: {}'.format(reconst_path))
                return reconst_path
 
            for (m, weight) in self.get_neighbors(n):
                
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    poo[m] = poo[n] + weight
                else:
                    if poo[m] > poo[n] + weight:
                        poo[m] = poo[n] + weight
                        par[m] = n
 
                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)
 
            open_lst.remove(n)
            closed_lst.add(n)
 
        print('Path does not exist!')
        return False

    def floyd_warshall(self):
        nV=len(self.G)
        distance = list(map(lambda i: list(map(lambda j: j, i)), self.G))

        for k in range((nV)):
            for i in range(nV):
                for j in range(nV):
                    distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
        
        for i in range(nV):
            for j in range(nV):
                if(distance[i][j] == INF):
                    distance[i][j]=False
                else:
                    distance[i][j]=round(distance[i][j],2)
            
        self.distance=distance





