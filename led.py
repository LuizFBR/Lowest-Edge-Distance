import parse
import sympy
import sys

""" ENTRADA
Assumindo que o número de arestas é menor ou igual do que o número de arestas máximo para um grafo simples:

n -> inteiro representando o número de arestas
(1,2) (1,3) -> par de pontos representando aresta entre pontos (com coordenadas reais)
(0.5,4.13) (1,3) -> ...
...
"""

def edge_facing(e1,e2): # assumindo que se dois vértices se interseccionam isso não conta como um "facing"
    return  not(     (max(e1[0],e1[2]) <= min(e2[0],e2[2]) or max(e2[0],e2[2]) <= min(e1[0],e1[2]) )
                 and (max(e1[1],e1[3]) <= min(e2[1],e2[3]) or max(e2[1],e2[3]) <= min(e1[1],e1[3]) )
            )

assert(edge_facing([0,2,4,3],[-2,3,4,0]) == True) # interseção em x e em y
assert(edge_facing([0,2,4,3],[-2,1,4,0]) == True) # interseção em x e não em y
assert(edge_facing([0,2,4,3],[-2,1,0,0]) == False) # interseção apenas em vértice de x
assert(edge_facing([0,2,4,3],[-2,1,-1,3]) == True) # interseção em y e não em x
assert(edge_facing([0,2,4,3],[-2,1,-1,2]) == False) # interseção apenas em vértice de y
assert(edge_facing([0,2,4,3],[-2,1,-1,0]) == False) # sem interseção em x ou y


def lowest_edge_distance(edge_list):
    min_dist = ("Missing_NO","Missing_NO",sys.maxsize)
    p1,p2,p3,p4 = sympy.symbols('p1 p2 p3 p4')
    for i in range(len(edge_list)):
        for j in range(i):
            e1,e2 = edge_list[i],edge_list[j]
            if edge_facing(e1,e2):
                expr = sympy.sqrt(
                    ( e1[0] + (e1[2] - e1[0])*p1 - (e2[0] + (e2[2] - e2[0])*p3) )**2 +
                    ( e1[1] + (e1[3] - e1[1])*p2 - (e2[1] + (e2[3] - e2[1])*p4) )**2
                )
                # print(f" e1: {e1} \n e2: {e2}")
                # print(sympy.solve([expr.diff(p1),expr.diff(p2),expr.diff(p3),expr.diff(p4)]))
                # print(expr.diff(p1))
                # print( sympy.printing.latex( expr.diff(p2)) )
                dist = expr.subs(sympy.solve([expr.diff(p1),expr.diff(p2),expr.diff(p3),expr.diff(p4)]))
                if dist.compare(min_dist[2]) == -1: min_dist = (e1,e2,dist)
    return min_dist

if __name__ == "__main__":
    pattern = "({},{}) ({},{})"
    # edge_list = [ [float(i) for i in parse.parse(pattern, input())] for _ in range(int(input())) ]
    with open('./t1','r') as f:
        f.readline()
        # [print(parse.parse(pattern, line.strip())) for line in f.readlines()]
        edge_list = [ [float(i) for i in parse.parse(pattern, line.strip())] for line in f.readlines() ]
        assert(lowest_edge_distance(edge_list) == ("Missing_NO","Missing_NO",sys.maxsize))
        print('t1')
    with open('./t2', 'r') as f:
        f.readline()
        edge_list = [ [float(i) for i in parse.parse(pattern, line.strip())] for line in f.readlines() ]
        assert(lowest_edge_distance(edge_list) == ("Missing_NO","Missing_NO",sys.maxsize))
        print('t2')
    with open('./t3', 'r') as f:
        f.readline()
        edge_list = [ [float(i) for i in parse.parse(pattern, line.strip())] for line in f.readlines() ]
        assert(lowest_edge_distance(edge_list) == ([5.0, 7.0, 5.0, 5.0], [7.0, 5.0, 7.0, 7.0], 2.00000000000000))
        print('t3')
    with open('./t4', 'r') as f:
        f.readline()
        edge_list = [ [float(i) for i in parse.parse(pattern, line.strip())] for line in f.readlines() ]
        a = lowest_edge_distance(edge_list)
        print(a)
        assert(a == ([5.1, 7.1, 5.1, 5.1], [7.1, 5.1, 7.1, 7.1], 2.00000000000000))
        print('t4')
    pass
    with open('./t5', 'r') as f:
        f.readline()
        edge_list = [ [float(i) for i in parse.parse(pattern, line.strip())] for line in f.readlines() ]
        a = lowest_edge_distance(edge_list)
        print(a)
        # assert(a == ([5.0, 7.0, 5.0, 5.0], [7.0, 5.0, 7.0, 7.0], 1.2632990900000003))
        # retornou uma distância minúscula: ([7.0653, 7.0324, 8.0192, 8.0192], [9.0125, 5.1301, 7.0252, 5.0521], 5.84973735727867e-15)
        print('t5')
    with open('./t6', 'r') as f:
        f.readline()
        edge_list = [ [float(i) for i in parse.parse(pattern, line.strip())] for line in f.readlines() ]
        a = lowest_edge_distance(edge_list)
        print(a)
        assert(a == ([5.0, 7.0, 5.0, 5.0], [7.0, 5.0, 7.0, 7.0], 1.2632990900000003))
        # retornou uma distância minúscula: ([1.0019011, 10.0079507, 1.101010101, 7.010210004], [7.0653, 7.032, 8.01921, 8.01921], 2.12192745214831e-14)
        print('t6')




# def lowest_edge_distance():
#     pattern = "({},{}) ({},{})"
#     adj_list = {}
#     for _ in range(int(input())): # pra cada linha de entrada representando uma aresta
#         line = [float(i) for i in parse.parse(pattern, input())]
#         if (line[0],line[1]) not in adj_list:
#             adj_list[line[0],line[1]] = set()
#         if (line[2],line[3]) not in adj_list:
#             adj_list[line[2],line[3]] = set()
#         adj_list[line[0],line[1]].add((line[2],line[3]))
#         adj_list[line[2],line[3]].add((line[0],line[1]))
#     for v in adj_list:
#         for v in adj_list: