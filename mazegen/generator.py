from mazegen.constants import Coord, Grid


class MazeGenerator:
    def __init__(
        self, width: int, 
        height: int, 
        entry: Coord,
        exit: Coord,
        perfect: bool = False,
        seed: int | None = None,
    ) -> None:
        if width < 2 or height < 2:
            raise ValueError("Maze dimensions must be at least 2")

        if entry == exit:
            raise ValueError("Entry and exit must be different")

        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.perfect = perfect
        self.seed = seed
        self.grid: Grid = []
        self.forty_two_cells: set[Coords] = set()

