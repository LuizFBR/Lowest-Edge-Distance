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
    p1,p2,p3,p4 = sympy.symbols('p1 p2 p3 p4', positive=True)
    for i in range(len(edge_list)):
        for j in range(i):
            e1,e2 = edge_list[i],edge_list[j]
            if edge_facing(e1,e2):
                expr = sympy.sqrt(
                    ( e1[0] + (e1[2] - e1[0])*p1 - (e2[0] + (e2[2] - e2[0])*p3) )**2 +
                    ( e1[1] + (e1[3] - e1[1])*p2 - (e2[1] + (e2[3] - e2[1])*p4) )**2
                )
                # expr = sympy.refine(expr, sympy.Contains(p1, sympy.Interval(0,1) ) &  sympy.Contains(p2, sympy.Interval(0,1) ) &
                #                           sympy.Contains(p3, sympy.Interval(0,1) ) &  sympy.Contains(p4, sympy.Interval(0,1) )
                # )
                expr = sympy.refine(expr,   sympy.And(sympy.Contains(p1, sympy.Interval(0,1)),
                                            sympy.And(sympy.Contains(p2, sympy.Interval(0,1)),
                                            sympy.And(sympy.Contains(p3, sympy.Interval(0,1)),
                                                      sympy.Contains(p4, sympy.Interval(0,1)) ) ) )
                )
                dist = expr.subs(sympy.solve([expr.diff(p1),expr.diff(p2),expr.diff(p3),expr.diff(p4)]))
                if dist.compare(min_dist[2]) == -1: min_dist = (e1,e2,dist)
    return min_dist


if __name__ == "__main__":
    pattern = "({},{}) ({},{})"
    with open('./t1','r') as f:
        f.readline()
        edge_list = [ [float(i) for i in parse.parse(pattern, line.strip())] for line in f.readlines() ]
        assert(lowest_edge_distance(edge_list) == ("Missing_NO","Missing_NO",sys.maxsize))
        print('teste t1 pronto')
    with open('./t2', 'r') as f:
        f.readline()
        edge_list = [ [float(i) for i in parse.parse(pattern, line.strip())] for line in f.readlines() ]
        assert(lowest_edge_distance(edge_list) == ("Missing_NO","Missing_NO",sys.maxsize))
        print('teste t2 pronto')
    with open('./t3', 'r') as f:
        f.readline()
        edge_list = [ [float(i) for i in parse.parse(pattern, line.strip())] for line in f.readlines() ]
        assert(lowest_edge_distance(edge_list) == ([5.0, 7.0, 5.0, 5.0], [7.0, 5.0, 7.0, 7.0], 2.00000000000000))
        print('teste t3 pronto')
    with open('./t4', 'r') as f:
        f.readline()
        edge_list = [ [float(i) for i in parse.parse(pattern, line.strip())] for line in f.readlines() ]
        assert(lowest_edge_distance(edge_list) == ([5.1, 7.1, 5.1, 5.1], [7.1, 5.1, 7.1, 7.1], 2.00000000000000))
        print('teste t4 pronto')
    with open('./t5', 'r') as f:
        f.readline()
        edge_list = [ [float(i) for i in parse.parse(pattern, line.strip())] for line in f.readlines() ]
        a = lowest_edge_distance(edge_list)
        print(a)
        # assert(a == ([5.0, 7.0, 5.0, 5.0], [7.0, 5.0, 7.0, 7.0], 1.2632990900000003))
        # retornou uma distância minúscula: ([9.021, 8.0925, 10.05, 9.1021], [8.015, 1.1025, 9.213, 2.101], 1.77610994307881e-14)
        print('teste t5 pronto')
    with open('./t6', 'r') as f:
        f.readline()
        edge_list = [ [float(i) for i in parse.parse(pattern, line.strip())] for line in f.readlines() ]
        a = lowest_edge_distance(edge_list)
        print(a)
        # retornou uma distância minúscula: ([1.0019011, 10.0079507, 1.101010101, 7.010210004], [1.0, 2.152124, 2.100212, 1.1302102], 1.57892738974034e-14)
        print('teste t6 pronto')
