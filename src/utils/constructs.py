import math
from queue import PriorityQueue

# Integer vectors


class Vec2i:

    def __init__(self, x: int, z: int):
        self.x = x
        self.z = z

    def x(self) -> int:
        return self.x

    def z(self) -> int:
        return self.z

    def angle_between(self, vec: 'Vec2i') -> float:
        return math.atan2(self.x - vec.x, self.z - vec.z)

    def dist_to(self, vec: 'Vec2i') -> float:
        dx = self.x - vec.x
        dz = self.z - vec.z

        return math.sqrt((dx * dx) + (dz * dz))

    def __eq__(self, obj: 'Vec2i') -> bool:
        return self.x == obj.x and self.z == obj.z

    def __hash__(self) -> int:
        return self.x * 1319198731747 + self.z * 91317744

    def _kind(self) -> str:
        return "Vec2i"

    def __str__(self) -> str:
        return self._kind() + "[" + str(self.x) + ", " + str(self.z) + "]"

    def __sub__(self, other) -> 'Vec2i':
        return Vec2i(self.x - other.x, self.z - other.z)

    def manhattan_from_origin(self) -> int:
        return abs(self.x) + abs(self.z)


# Mutable Vec2i
class MVec2i(Vec2i):
    def set_x(self, x: int) -> None:
        self.x = x

    def set_z(self, z: int) -> None:
        self.z = z

    def _kind(self) -> str:
        return "MutableVec2i"


class Vec2Node:
    def __init__(self, loc: Vec2i, target: Vec2i):
        self.loc = loc
        self.target = target
        self.parent = None

    def setParent(self, parent): # parent: Vec2Node
        self.parent = parent

    def heuristic(self) -> float:
        dx = self.loc.x - self.target.x
        dz = self.loc.z - self.target.z

        return math.sqrt(dx * dx + dz * dz)

    def __lt__(self, obj) -> bool:
        """self < obj."""
        return self.heuristic() < obj.heuristic()

    def __le__(self, obj) -> bool:
        """self <= obj."""
        return self.heuristic() <= obj.heuristic()

    def __eq__(self, obj) -> bool:
        """self == obj."""
        return self.heuristic() == obj.heuristic()

    def __ne__(self, obj) -> bool:
        """self != obj."""
        return self.heuristic() != obj.heuristic()

    def __gt__(self, obj) -> bool:
        """self > obj."""
        return self.heuristic() > obj.heuristic()

    def __ge__(self, obj) -> bool:
        """self >= obj."""
        return self.heuristic() >= obj.heuristic()

    def __hash__(self) -> int:
        return self.loc.__hash__()

    def __str__(self) -> str:
        return "%" + self.loc.__str__()

class Vec2f:
    def __init__(self, x: float, z: float):
        self.x = x
        self.z = z

    def x(self) -> float:
        return self.x

    def z(self) -> float:
        return self.z

class DriveInstruction:
    def __init__(self, forwards: float, angle: float):
        self.forwards = forwards
        self.angle = angle

        if forwards is not 0 and angle is not 0:
            print("Only one of forwards and angle should exist in an instruction!")

    def get_angle(self):
        return self.angle

    def get_forwards(self):
        # TODO: change this constant!!!
        TIME_TO_GO_FOWARDS_AN_INCH = 0.2
        return self.forwards * TIME_TO_GO_FOWARDS_AN_INCH

class ContainingPrioQueue(PriorityQueue):
    def _init(self, maxsize):
        self.set = set()
        super()._init(maxsize)

    def _get(self):
        item = super()._get()
        self.set.remove(item)
        return item

    def _put(self, item):
        self.set.add(item)
        super()._put(item)

    def __contains__(self, item):
        return item in self.set