"""Render a cubic Vertex Cover instance and its use in the reduction. Requires Pillow."""
from itertools import combinations
from math import cos, sin, pi
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent
POINTS = {"A": (1, 1, 1), "B": (-1, -1, 1), "C": (-1, 1, -1), "D": (1, -1, -1)}
EDGES = list(combinations(POINTS, 2))
STAGES = [
    ("The cubic input", [], ["Four vertices, six edges.", "Each vertex meets three.", "", "A cover chooses at least", "one end of every edge."]),
    ("Try two vertices", ["B", "C"], ["B and C cover five edges.", "Edge AD has neither end", "selected. By symmetry,", "every pair misses an edge."]),
    ("Choose three", ["B", "C", "D"], ["B, C and D cover all six.", "In the game each choice", "requires a whole gadget", "of 20 agents."]),
    ("Build the coalition", ["B", "C", "D"], ["28 original agents", "+ 60 in three gadgets", "+ 12 edge-switch agents", "= 100 in the coalition.", "", "Old block size: 101."]),
    ("Why the converse works", ["B", "C"], ["At budget two, at most", "53 slots remain after the", "28 required agents.", "Three gadgets need 60.", "Two miss the red edge."]),
]
BG, INK, GRAY, GREEN, RED, EDGE = "#f6f4eb", "#142f35", "#536769", "#00746b", "#ba482d", "#9faeaa"

def font(size, bold=False):
    for name in (("DejaVuSans-Bold.ttf", "Arial Bold.ttf") if bold else ("DejaVuSans.ttf", "Arial.ttf")):
        try:
            return ImageFont.truetype(name, size)
        except OSError:
            continue
    return ImageFont.load_default(size=size)

TITLE, HEAD, BODY, LABEL, SMALL = font(34, True), font(27, True), font(22), font(21, True), font(18)

def project(point, angle):
    x, y, z = point
    u, v = x*cos(angle)+z*sin(angle), -x*sin(angle)+z*cos(angle)
    til = 0.26
    height, depth = y*cos(til)-v*sin(til), y*sin(til)+v*cos(til)
    return 213+94*u, 245-94*height, depth

def frame(stage, angle):
    image = Image.new("RGB", (880, 456), BG)
    draw = ImageDraw.Draw(image)
    title, chosen, lines = STAGES[stage]
    draw.text((26, 16), "From a vertex cover to a blocking coalition", font=TITLE, fill=INK)
    draw.line((26, 76, 854, 76), fill=EDGE)
    draw.text((26, 86), "Cubic input graph  ·  K4", font=SMALL, fill=GRAY)
    pos = {k: project(v, angle) for k, v in POINTS.items()}
    def paint_edge(pair):
        s, t = pair
        paid = s in chosen or t in chosen
        color = (GREEN if paid else RED) if chosen else EDGE
        draw.line((pos[s][:2], pos[t][:2]), fill=color, width=(6 if chosen and not paid else 3))
    for pair in sorted(EDGES, key=lambda e:sum(pos[k][2] for k in e)):
        paint_edge(pair)
    for v in sorted(POINTS, key=lambda k:pos[k][2]):
        x, y, depth = pos[v]
        radius = round(18 + depth)
        draw.ellipse((x-radius,y-radius,x+radius,y+radius), fill=GREEN if v in chosen else BG, outline=INK,width=2)
        draw.text((x,y), v, font=LABEL, anchor="mm", fill="white" if v in chosen else INK)
    draw.text((422, 96), title, font=HEAD, fill=INK)
    for i,line in enumerate(lines):
        draw.text((422, 145+32*i), line, font=BODY, fill=INK)
    paid = sum(bool(set(e) & set(chosen)) for e in EDGES)
    draw.text((26, 402), f"{paid} of 6 edges covered", font=LABEL,fill=GREEN if paid==6 else INK)
    draw.text((422, 403), "●  selected vertex" if stage!=1 and stage!=4 else "Red line = uncovered edge AD", font=SMALL,fill=RED if stage in (1,4) else GREEN)
    for j in range(5):
        draw.rectangle((26+167*j,441,185+167*j,444),fill=GREEN if j==stage else EDGE)
    return image.convert("P", palette=Image.Palette.ADAPTIVE, colors=48)

if __name__ == "__main__":
    assert all(sum(bool(set(e)&set(x)) for e in EDGES)==5 for x in combinations(POINTS,2))
    assert all(sum(bool(set(e)&set(x)) for e in EDGES)==6 for x in combinations(POINTS,3))
    frames = []
    times = []
    for j in range(len(STAGES)):
        for i in range(10):
            # Avoid edge-on views during holds, then continue rotating into the next stage.
            frames.append(frame(j, 0.43+(j+i/10)*2*pi/5))
            times.append(1950 if i==0 else 155)
    frames[0].save(HERE/"blocking-coalition.gif",save_all=True,append_images=frames[1:],duration=times,loop=0,optimize=True,disposal=1)
