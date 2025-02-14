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

    def __eq__(self, obj) -> bool:
        return self.x == obj.x and self.z == obj.z

    def __hash__(self) -> int:
        return self.x * 1319198731747 + self.z * 91317744

    def _kind(self) -> str:
        return "Vec2i"

    def __str__(self) -> str:
        return self._kind() + "[" + str(self.x) + ", " + str(self.z) + "]"


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