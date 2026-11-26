# A vertex cover becomes a blocking coalition

The [looping figure](blocking-coalition.gif) rotates the tetrahedral drawing of the four-vertex cubic input. Its six edges are requirements. Selecting an endpoint pays for the corresponding requirement. To try every selection, unzip [the explorer](coalition-explorer.zip) and open index.html in a browser. It works offline.

In this example the input has six edges. The tether has 14 internal agents, each whole gadget contributes 20 agents, and 28 agents are forced from the original block. Orient each edge alphabetically. Selecting B, C and D includes all six head switches as well as all six tail switches. The resulting coalition has 28 + 60 + 12 = 100 agents, while the original block contains 101 at budget three. At budget two there are just 53 slots beyond the 28 required agents. Three gadgets need 60, and any two vertices miss the edge between the other two. The paper proves the forcing argument for arbitrary cubic input graphs.

Run `python3 render.py` in an environment with Pillow to render the GIF. The [HTML source](index.html) is self-contained and uses the same coordinates and counts.
