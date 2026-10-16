from mazegen.generator import MazeGenerator

gen = MazeGenerator(11, 7, (0, 0), (10, 6), seed=1)
gen.generate()

for y in range(gen.height):
    linha = ""
    for x in range(gen.width):
        if (x, y) in gen.forty_two_cells:
            linha += "*"
        else:
            linha += "."
    print(linha)


def desenhar(gen):
    for y in range(gen.height):
        topo = ""
        meio = ""
        for x in range(gen.width):
            celula = gen.grid[y][x]
            topo += "+" + ("---" if celula & 1 else "   ")
            meio += "|" if celula & 8 else " "
            meio += "###" if (x, y) in gen.forty_two_cells else "   "
        print(topo + "+")
        print(meio + "|")
    print("+---" * gen.width + "+")


desenhar(gen)

abertas = sum(1 for linha in gen.grid for c in linha if c != 15)
esperado = gen.width * gen.height - len(gen.forty_two_cells)
print("sem células isoladas:", abertas == esperado)

g1 = MazeGenerator(15, 11, (0, 0), (14, 10), seed=7)
g2 = MazeGenerator(15, 11, (0, 0), (14, 10), seed=7)
g1.generate()
g2.generate()
print("mesma seed, mesmo labirinto:", g1.grid == g2.grid)