import numpy as np
from queue import PriorityQueue
import constructs
import pathfind

class SimulatedLevel:
    """ Constructor """
    def __init__(self):
        # TODO: one unit should be 1 inch, get size of board
        self.x_size = 32
        self.z_size = 32

        # calloc
        self.field = np.zeros((self.x_size, self.z_size), float)

    def in_range(self, x: int, z: int):
        return 0 <= x < self.x_size and 0 <= z < self.z_size

    def can_pathfind_thru(self, x: int, z: int):
        return self.in_range(x, z) and self.field[x, z] == 0

    # Private, do not call!!
    def __pathfind(self, start: Vec2i, target: Vec2i):
        closed = set()
        openQ = ContainingPrioQueue()
        openQ._put(Vec2Node(start, target))

        self.stored_start = start
        self.stored_target = target

        while not openQ.empty():
            pop = openQ._get()
            if (target == pop.loc):
                return pop

            for dir in SQUARE:
                dx = pop.loc.x + dir.x
                dz = pop.loc.z + dir.z

                node = Vec2Node(Vec2i(dx, dz), target)

                if (not closed.__contains__(node) and not openQ.__contains__(node)):
                    if self.can_pathfind_thru(dx, dz):
                        node.setParent(pop)
                        openQ.put(node)

            closed.add(pop)

        return None

    def pathfind(self, start: Vec2i, target: Vec2i):
        res_node = self.__pathfind(start, target);
        nd = res_node

        if (res_node is not None):
            self.allNodes = set()
            while not nd is None:
                self.allNodes.add(nd.loc)
                nd = nd.parent

    def clear_field(self):
        np.fill(self.field, 0)

    def apply_object(self, x: int, z: int, x_size: int, z_size: int):
        for i in range(x, x + x_size):
            for j in range(z, z + z_size):
                if (self.in_range(i, j)):
                    self.field[x, z] = 1
    def debug(self):
        for x in range(0, self.x_size):
            for z in range(0, self.z_size):
                vec = Vec2i(x, z)
                if self.stored_start == vec:
                    print("^", end="")
                elif self.stored_target == vec:
                    print("%", end="")
                elif self.allNodes.__contains__(vec):
                    print("~", end="")
                elif self.field[x, z] != 0:
                    print("#", end="")
                else:
                    print(".", end="")
            print("")
