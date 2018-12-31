from collections import defaultdict
from collections import namedtuple

from utils.get_input import get_from_url


Coord = namedtuple('Coord', ['x', 'y'])


def main():
    input_url = 'https://adventofcode.com/2018/day/6/input'

    coords_input = get_from_url(input_url)

    x_vals = []
    y_vals = []
    coords = []

    def man_distance(x1, y1, x2, y2):
        return abs(x1 - x2) + abs(y1 - y2)

    for raw_coord in coords_input.strip().split('\n'):
        x, y = [int(val) for val in raw_coord.split(', ')]
        x_vals.append(x)
        y_vals.append(y)
        coords.append(Coord(x, y))

    max_x = max(x_vals)
    max_y = max(y_vals)

    cell_counts = defaultdict(int)
    infinites = set()
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            distances = sorted(
                (man_distance(x, y, px, py), i)
                for i, (px, py) in enumerate(coords)
            )
            if distances[0][0] != distances[1][0]:
                cell_counts[distances[0][1]] += 1
                if x == 0 or y == 0 or x == max_x or y == max_y:
                    infinites.add(distances[0][1])

    for k in infinites:
        cell_counts.pop(k)

    print(max(cell_counts.values()))


if __name__ == '__main__':
    main()
