from mazegen.generator import MazeGenerator

gen = MazeGenerator(15, 11, (0, 0), (14, 10), seed=1)
gen.generate()

for y in range(gen.height):
    linha = ""
    for x in range(gen.width):
        if (x, y) in gen.forty_two_cells:
            linha += "X"
        else:
            linha += "."
    print(linha)