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

    count = 0
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (
                sum(man_distance(x, y, coord.x, coord.y) for coord in coords)
                < 10000
            ):
                count += 1
    print(count)


if __name__ == '__main__':
    main()
