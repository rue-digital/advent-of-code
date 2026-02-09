def parse(filepath):
    with open(filepath, "r") as file:
        grid = [list(line.strip()) for line in file]
    return grid


def part1(filepath):
    grid = parse(filepath)

    splits = 0
    beams = set()

    for i, row in enumerate(grid):
        if "S" in row:  # first row
            beams.add(row.index("S"))
            continue
        if i == len(grid) - 1:  # last row
            break
        # propagate beams from current to the row below
        splitters = set()
        newBeams = set()
        for beam in beams:
            if grid[i + 1][beam] == "^":
                splitters.add(beam)
                splits += 1
                if beam - 1 > -1:
                    newBeams.add(beam - 1)
                if beam + 1 < len(grid[0]):
                    newBeams.add(beam + 1)

        beams.update(newBeams)
        beams = beams - splitters
    return splits
