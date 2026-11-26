"""Finite corroboration: coalition feasibility by propagation and exhaustive branching."""
from itertools import combinations

def instance(n, edges, k):
    adj, block_size, old = [], [], []
    def new(count, size, friends):
        out=list(range(len(adj),len(adj)+count))
        adj.extend(set() for _ in out)
        block_size.extend([size]*count)
        old.extend([friends]*count)
        return out
    def link(a,b):
        assert a!=b and b not in adj[a]
        adj[a].add(b); adj[b].add(a)
    m=len(edges)
    W=2*m+2
    F=k*(W+6)+2*m+1
    C=2*m+4*n+F
    spine=new(m+2*n,C,3)
    for a,b in zip(spine,spine[1:]+spine[:1]):
        link(a,b)
    path=new(F,C,0)
    for a,b in zip(path,path[1:]):
        link(a,b)
    arms={}
    for x in range(n):
        A,=new(1,C,2)
        J,=new(1,C,2)
        link(A,spine[m+2*x]); link(J,spine[m+2*x+1]); link(A,J)
        a,b,c,d,e,f=new(6,3,2)
        for ii,jj in [(a,b),(b,c),(a,c),(d,e),(e,f),(d,f),(a,d)]:
            link(ii,jj)
        R=new(W,2,1)
        for ii,jj in zip([f]+R,R+[A]):
            link(ii,jj)
        arms[x]=[b,c,e]
    for i,(x,y) in enumerate(edges):
        T,=new(1,C,2)
        U,V=new(2,2,1)
        for a,b in [(T,spine[i]),(T,path[i]),(T,U),(U,V),
                    (U,arms[x].pop()),(V,arms[y].pop())]:
            link(a,b)
    for v in path:
        old[v]=len(adj[v])
    assert all(not p for p in arms.values())
    assert sum(s==C for s in block_size)==C and max(map(len,adj))==3
    return adj,block_size,old,C

def set_bits(mask):
    while mask:
        bit = mask & -mask
        yield bit.bit_length() - 1
        mask ^= bit


def accepts(G, chosen, strict):
    adj, sizes, old, _ = G
    if not chosen:
        return False
    size = len(chosen)
    pairs = [((len(adj[v] & chosen), -size), (old[v], -sizes[v])) for v in chosen]
    return (all(now > before for now, before in pairs) if strict else
            all(now >= before for now, before in pairs) and any(now > before for now, before in pairs))


def witness(G, strict):
    adj, sizes, old, _ = G
    n = len(adj)
    all_bits = (1 << n) - 1
    neighbors = [sum(1 << j for j in friends) for friends in adj]
    cuts = sorted({1, n + 1, *sizes, *(s + 1 for s in sizes)})

    for low, end in zip(cuts, cuts[1:]):
        high = end - 1
        required = [o + int(low > p or (strict and low == p)) for o, p in zip(old, sizes)]
        stack = [(0, all_bits)]
        while stack:
            inside, available = stack.pop()
            while True:
                if inside & ~available or inside.bit_count() > high or available.bit_count() < low:
                    break
                excluded = forced = 0
                for v in set_bits(available):
                    friends = neighbors[v] & available
                    if friends.bit_count() < required[v]:
                        excluded |= 1 << v
                    elif inside >> v & 1 and friends.bit_count() == required[v]:
                        forced |= friends
                if excluded or forced & ~inside:
                    available &= ~excluded
                    inside |= forced
                    continue
                if inside.bit_count() >= low:
                    candidate = set(set_bits(inside))
                    if accepts(G, candidate, strict):
                        return candidate
                if available.bit_count() <= high:
                    candidate = set(set_bits(available))
                    if accepts(G, candidate, strict):
                        return candidate
                if inside.bit_count() == high or available.bit_count() == low or inside == available:
                    break
                # Branch on an undecided friend needed by an included agent, if possible.
                pool = available & ~inside
                for v in set_bits(inside):
                    if (neighbors[v] & inside).bit_count() < required[v]:
                        pool &= neighbors[v]
                        if pool:
                            break
                        pool = available & ~inside
                bit = pool & -pool
                stack.extend(((inside, available ^ bit), (inside | bit, available)))
                break
    return None


def brute(G, strict):
    vertices = range(len(G[0]))
    return any(accepts(G, set(s), strict) for k in range(1, len(vertices)+1)
               for s in combinations(vertices, k))


def test_solver():
    from random import Random
    rng = Random(236)
    for _ in range(120):
        n = rng.randint(2, 8)
        labels = [rng.randrange(3) for _ in range(n)]
        neighbors = [set() for _ in labels]
        for i, j in combinations(range(n), 2):
            if rng.random() < .35:
                neighbors[i].add(j)
                neighbors[j].add(i)
        sizes = [labels.count(c) for c in labels]
        old = [sum(labels[u] == c for u in neighbors[i]) for i, c in enumerate(labels)]
        graph = neighbors, sizes, old, None
        for strict in (False, True):
            assert (witness(graph, strict) is not None) == brute(graph, strict)


if __name__ == '__main__':
    test_solver()
    graphs = [(4,list(combinations(range(4),2))),
              (6,[(i,j) for i in range(3) for j in range(3,6)]),
              (6,[(0,1),(1,2),(0,2),(3,4),(4,5),(3,5),(0,3),(1,4),(2,5)])]
    checks = 0
    for n, edges in graphs:
        for k in range(n+1):
            cover = any(all(x in C or y in C for x,y in edges)
                        for C in map(set, combinations(range(n), k)))
            G = instance(n, edges, k)
            for strict in (False, True):
                assert (witness(G, strict) is not None) == cover
                checks += 1
    print('240 small-game comparisons with exhaustive enumeration passed.')
    print(f'{checks} coalition checks matched the vertex-cover decision.')
