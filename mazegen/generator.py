from mazegen.constants import Coord, Grid, FORTY_TWO, DIRECTIONS
import random


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

        for x, y in (entry, exit):
            if not (0 <= x < width and 0 <= y < height):
                raise ValueError("Entry or exit is outside the maze")

        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.perfect = perfect
        self.seed = seed
        self.grid: Grid = []
        self.forty_two_cells: set[Coord] = set()
        self.forty_two_omitted = False

    def generate(self) -> None:
        if self.seed is None:
            self.seed = random.randint(0, 999999)
        random.seed(self.seed)

        self.grid = [
            [15 for _ in range(self.width)] for _ in range(self.height)
        ]

        self._place_forty_two()

        visited: set[Coord] = {self.entry}
        stack: list[Coord] = [self.entry]

        while stack:
            x, y = stack[-1]
            neighbors = self._get_neighbors(x, y, visited)
            if neighbors:
                nx, ny, bit_here, bit_there = random.choice(neighbors)
                self.grid[y][x] &= ~bit_here
                self.grid[ny][nx] &= ~bit_there
                visited.add((nx, ny))
                stack.append((nx, ny))
            else:
                stack.pop()

    def _place_forty_two(self) -> None:
        self.forty_two_cells = set()

        if self.width < 7 or self.height < 5:
            self.forty_two_omitted = True
            return

        self.forty_two_omitted = False

        start_x = (self.width - 7) // 2
        start_y = (self.height - 5) // 2

        for dy, row in enumerate(FORTY_TWO):
            for dx, char in enumerate(row):
                if char == "X":
                    self.forty_two_cells.add((start_x + dx, start_y + dy))

        if (
            self.entry in self.forty_two_cells
            or self.exit in self.forty_two_cells
        ):
            raise ValueError("Entry or exit overlaps the 42 pattern")

    def _get_neighbors(
        self, x: int, y: int, visited: set[Coord]
        ) -> list[tuple[int, int, int, int]]:
        result: list[tuple[int, int, int, int]] = []
        for dx, dy, bit_here, bit_there in DIRECTIONS:
            nx = x + dx
            ny = y + dy
            if not (0 <= nx < self.width and 0 <= ny < self.height):
                continue
            if (nx, ny) in visited:
                continue
            if (nx, ny) in self.forty_two_cells:
                continue
            result.append((nx, ny, bit_here, bit_there))
        return result
