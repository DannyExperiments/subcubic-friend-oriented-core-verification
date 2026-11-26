# Mathematical audit of Q236

**Disposition.** Pass for the stated theorem after editorial and source corrections. High confidence. Review date 26 November 2026.

I reconstructed both directions of the reduction. Comparing friend counts then coalition sizes gives the distinct thresholds for strict and weak improvements. Saturation forces the cycle and its neighbours once reached. A member of either triangle in any acceptable coalition of size at least four forces all three friends, taking both triangles, all ports, the tether and gate. Conversely an included tether vertex forces its complete path. A switch with two required friends must lead to an endpoint gadget. Without an outside agent, the fallback would force a terminal and the cycle. These implications force B into every weak block and exclude the entire fallback, since the cycle caps the size by |C| and S=C is indifferent. Small outside triples can only be old triangles by the interblock matching. Each input edge consequently requires an endpoint gadget, and F<(k+1)L bounds the count by k. In the converse direction the selected head switches and all tail switches give every selected gadget its ports, while kL+2m<F guarantees every old-block member strictly improves. The construction is polynomial, simple and subcubic even at k=0. This proves both complement hardness statements, and certificates establish membership.

The authorless candidate clarifies the 2023 degree convention and credits the degree-two half of the dichotomy to the literature. The finite replay uses an independently implemented coalition search and the original instance generator.

The input includes the partition. Nonedges represent mutual enemies. The reduction permits nonplanar graphs. The threshold concerns the maximum number of distinct friends; degree-two tractability is a prior theorem.

The standard-library solver matched exhaustive enumeration in 240 small-game comparisons and the source Vertex Cover decisions in 38 checks on three cubic graphs for both blocking predicates. The proof is independent of those tests. Larger experiments mentioned in the earlier draft are outside this evidence package.
