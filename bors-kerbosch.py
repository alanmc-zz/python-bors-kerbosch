#!/usr/bin/python

import sys, collections

def bors_kerbosch_v1(R, P, X, G, C):

    if len(P) == 0 and len(X) == 0:
        if len(R) > 2:
            C.append(sorted(R))
        return 
    
    for v in P.union(set([])):
        bors_kerbosch_v1(R.union(set([v])), P.intersection(G[v]), X.intersection(G[v]), G, C)
        P.remove(v)
        X.add(v)

def bors_kerbosch_v2(R, P, X, G, C):

    if len(P) == 0 and len(X) == 0:
        if len(R) > 2:
            C.append(sorted(R))            
        return

    (d, pivot) = max([(len(G[v]), v) for v in P.union(X)])
                     
    for v in P.difference(G[pivot]):
        bors_kerbosch_v2(R.union(set([v])), P.intersection(G[v]), X.intersection(G[v]), G, C)
        P.remove(v)
        X.add(v)
        
def test():
    input = [('a', 'b'), ('b', 'a'), ('a', 'c'), ('c', 'a'), ('b', 'c'), ('c', 'b'), ('d', 'e'), ('e', 'd'), ('d', 'f'), ('f', 'd'), ('e', 'f'), ('f', 'e')]

    G = collections.defaultdict(set) 
    C1 = []
    C2 = []
    for (src,dest) in input:
        G[src].add(dest)

    bors_kerbosch_v1(set([]), set(G.keys()), set([]), G, C1)
    bors_kerbosch_v2(set([]), set(G.keys()), set([]), G, C2)

    for c in sorted(C1):
        print ', '.join(c)

    for c in sorted(C2):
        print ', '.join(c)


if __name__ == '__main__':
    test()
