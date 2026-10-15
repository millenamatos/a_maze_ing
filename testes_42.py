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