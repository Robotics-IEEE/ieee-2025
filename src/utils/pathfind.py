from constructs import *
from level import *

NORTH = Vec2i(1, 0)
EAST = Vec2i(0, 1)
SOUTH = Vec2i(-1, 0)
WEST = Vec2i(0, -1)

NORTHEAST = Vec2i(1, 0)
NORTHWEST = Vec2i(0, 1)
SOUTHEAST = Vec2i(-1, 0)
SOUTHWEST = Vec2i(0, -1)

class DirAmtPair:
    def __init__(self, dir: Vec2i, amt: int):
        self.dir = dir
        self.amt = amt

def pathlist_from_nodelist(root: Vec2Node) -> list:
    dirs = list()
    last_dir = None
    last_amt = 0

    nd = root
    while nd is not None:
        if nd.parent is not None:
            ndir = nd.loc - nd.parent.loc
            if last_dir == ndir:
                last_amt = last_amt + 1
            else:
                if last_dir is not None:
                    dirs.append(DirAmtPair(last_dir, last_amt))

                last_dir = ndir
                last_amt = 1

        nd = nd.parent
    return dirs

o = SimulatedLevel()
res = o.pathfind2(Vec2i(2, 2), Vec2i(12, 10))
nd = res
pathlist_from_nodelist(res)

allNodes = set()
while not nd is None:
    allNodes.add(nd.loc)
    nd = nd.parent

for x in range(0, 32):
    for z in range(0, 32):
        vec = Vec2i(x, z)
        if Vec2i(2, 2) == vec:
            print("^", end="")
        elif Vec2i(12, 10) == vec:
            print("%", end="")
        elif allNodes.__contains__(vec):
            print("#", end="")
        else:
            print(".", end="")
    print("")