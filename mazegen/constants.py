NORTH: int = 1
EAST: int = 2
SOUTH: int = 4
WEST: int = 8

Coord = tuple[int, int]
Grid = list[list[int]]

FORTY_TWO = [
        "X.X.XXX",
        "X.X...X",
        "XXX.XXX",
        "..X.X..",
        "..X.XXX",
]

DIRECTIONS = [
        (0, -1, NORTH, SOUTH),
        (1, 0, EAST, WEST),
        (0, 1, SOUTH, NORTH),
        (-1, 0, WEST, EAST),
]