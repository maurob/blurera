from math import sqrt
from typing import TypeVar, Any
from dataclasses import dataclass, astuple

TP = TypeVar("TP", bound="Point")
TB = TypeVar("TB", bound="Box")


class AsTuple:
    def __iter__(self):
        yield from astuple(self)

    def __getitem__(self, index):
        return astuple(self)[index]


@dataclass(frozen=True)
class Point(AsTuple):
    x: int
    y: int

    def __add__(self, p2: TP) -> TP:
        return Point(self.x + p2.x, self.y + p2.y)

    def __sub__(self, p2: TP) -> TP:
        return Point(self.x - p2.x, self.y - p2.y)

    def __mul__(self, scalar: float) -> TP:
        return Point(int(self.x*scalar), int(self.y*scalar))

    @property
    def modulo(self) -> float:
        return sqrt(self.x**2 + self.y**2)


@dataclass(frozen=True)
class Box:
    p1: Point
    p2: Point

    @property
    def center(self) -> Point:
        return self.p1 + (self.p2 - self.p1) * 0.5

    def __sub__(self, box2: TB) -> float:
        return (self.center - box2.center).modulo

    @property
    def weight(self) -> int:
        return self.p2.x - self.p1.x

    w = weight

    @property
    def height(self) -> int:
        return self.p2.y - self.p1.y

    h = height

    def __call__(self, img):
        """
        return the image region defined by this box
        """
        return img[self.p1.y:self.p2.y, self.p1.x:self.p2.x]

    @classmethod
    def from_(cls, iterable):
        x1, y1, x2, y2 = iterable
        return cls(Point(x1, y1), Point(x2, y2))


@dataclass(frozen=True)
class DistantBox(Box):
    frame_distance: int  # number of frame this Box is distant relative to a current image


@dataclass
class Frame:
    id: int
    img: Any

    @property
    def first(self):
        return self.id == 0

    def __bool__(self):
        return self.img is not None

    @property
    def size(self):
        return self.img.shape[1], self.img.shape[0]

    def __iter__(self):
        yield from astuple(self)

@dataclass
class FrameWithBoxes(Frame):
    boxes: set[Box]


@dataclass
class FrameWithDistantBoxes(Frame):
    boxes: set[DistantBox]
