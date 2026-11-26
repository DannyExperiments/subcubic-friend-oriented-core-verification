# Problem and proof

Can one efficiently verify core stability or strict core stability when everyone has at most three mutual friends? [Simola, dissertation, §5.5](https://doi.org/10.34726/hss.2026.138201)

**Theorem.** Both partition verification problems are coNP-complete for symmetric friend-oriented hedonic games without neutrals and with at most three mutual friends. With at most two they are polynomial-time decidable.

One cubic Vertex Cover reduction ensures all-strict blocking in yes instances and excludes every weak block in no instances.

I reconstructed both directions of the reduction. Comparing friend counts then coalition sizes gives the distinct thresholds for strict and weak improvements. Saturation forces the cycle and its neighbours once reached. A member of either triangle in any acceptable coalition of size at least four forces all three friends, taking both triangles, all ports, the tether and gate. Conversely an included tether vertex forces its complete path. A switch with two required friends must lead to an endpoint gadget. Without an outside agent, the fallback would force a terminal and the cycle. These implications force B into every weak block and exclude the entire fallback, since the cycle caps the size by |C| and S=C is indifferent. Small outside triples can only be old triangles by the interblock matching. Each input edge consequently requires an endpoint gadget, and F<(k+1)L bounds the count by k. In the converse direction the selected head switches and all tail switches give every selected gadget its ports, while kL+2m<F guarantees every old-block member strictly improves. The construction is polynomial, simple and subcubic even at k=0. This proves both complement hardness statements, and certificates establish membership.

The [complete proof](../paper/manuscript.pdf) is accompanied by its [LaTeX source](../paper/manuscript.tex). The input includes the partition. Nonedges represent mutual enemies. The reduction permits nonplanar graphs. The threshold concerns the maximum number of distinct friends; degree-two tractability is a prior theorem.
