from collections import deque

class Graph:
    def __init__(self, adjac_list):
        self.adjac_list = adjac_list

    def neighbors(self, v):
        return self.adjac_list[v]

    def heuristic_value(self, n):
        H = {
            'A': 1,
            'B': 1,
            'C': 1,
            'D': 1,
            'E': 1
        }

        return H[n]

    def a_star_algorithm(self, start, stop):
        open_lst = set([start])
        closed_lst = set([])
        present = {}
        present[start] = 0
        par = {}
        par[start] = start

        while len(open_lst) > 0:
            n = None

            for v in open_lst:
                if n == None or present[v] + self.heuristic_value(v) < present[n] + self.heuristic_value(n):
                    n = v

            if n == None:
                print('Path does not exist!')
                return None

            if n == stop:
                reconst_path = []

                while par[n] != n:
                    reconst_path.append(n)
                    n = par[n]

                reconst_path.append(start)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path
            for (m, weight) in self.neighbors(n):
                if m not in open_lst and m not in closed_lst:
                    open_lst.add(m)
                    par[m] = n
                    present[m] = present[n] + weight

                else:
                    if present[m] > present[n] + weight:
                        present[m] = present[n] + weight
                        par[m] = n

                        if m in closed_lst:
                            closed_lst.remove(m)
                            open_lst.add(m)

            open_lst.remove(n)
            closed_lst.add(n)

        print('Path does not exist!')
        return None

adjac_list = {
    'A': [('B', 2), ('C', 3), ('D', 9)],
    'B': [('D', 6)],
    'C': [('D', 2)],
    'D': [('E', 10)]
}

graph1 = Graph(adjac_list)
graph1.a_star_algorithm('A', 'E')
