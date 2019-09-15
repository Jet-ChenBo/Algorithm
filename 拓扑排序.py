from collections import defaultdict

class Graph():
    def __init__(self, vertices):
        self.graph = defaultdict(list)  # key是u，value是v(list类型)
        self.V = vertices  # 点的总个数

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topo_sort(self):
        in_degrees = defaultdict(int)  # 初始化每个点入度为0
        for u in self.graph:
            in_degrees.setdefault(u,0)  # 若键不存在，则添加进去
            for v in self.graph[u]:
                in_degrees[v] += 1  # 计算每个点的入度
        quene = [u for u in in_degrees if in_degrees[u] == 0]  # 筛选入度为0的点
        stack = []  # 保存输出的点的顺序
        while quene:
            u = quene.pop()
            stack.append(u)
            for v in self.graph[u]:
                in_degrees[v] -= 1  # 将u对应的v的入度减1
                if in_degrees[v] == 0:
                    quene.append(v)  # 如果入度为0，就放入quene
        if len(stack) == self.V:
            print('拓扑排序结果：', stack)
        else:
            print("图中有环，无法进行拓扑排序")

if __name__ == '__main__':
    g = Graph(6)
    g.add_edge(5,2)
    g.add_edge(5,0)
    g.add_edge(4,0)
    g.add_edge(4,1)
    g.add_edge(2,3)
    g.add_edge(3,1)
    g.topo_sort()
