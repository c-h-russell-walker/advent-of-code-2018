from utils.get_input import get_from_url


def main():
    input_url = 'https://adventofcode.com/2018/day/3/input'

    fabric_claims = get_from_url(input_url)

    max_x = 1000
    max_y = 1000

    for fabric_claim in fabric_claims.split('\n'):
        if fabric_claim == '':
            continue
        parts = fabric_claim.split(' @ ')
        parts_two = parts[1].split(': ')
        x, y = parts_two[0].split(',')
        width, length = parts_two[1].split('x')

        x_2 = int(x) + int(width)
        y_2 = int(y) + int(length)

        if x_2 > max_x:
            max_x = x_2

        if y_2 > max_y:
            max_y = y_2

    matrix = [[0 for m_x in range(max_x)] for m_y in range(max_y)]

    conflict_count = 0
    for fabric_claim in fabric_claims.split('\n'):
        if fabric_claim == '':
            continue
        parts = fabric_claim.split(' @ ')
        parts_two = parts[1].split(': ')
        x, y = parts_two[0].split(',')
        width, length = parts_two[1].split('x')

        x = int(x)
        y = int(y)

        x_2 = x + int(width)
        y_2 = y + int(length)

        for xs in range(x, x_2):
            for ys in range(y, y_2):
                matrix[xs][ys] += 1
                # If it's the first conflict for the coordinate
                if matrix[xs][ys] == 2:
                    conflict_count += 1

    print(conflict_count)


if __name__ == '__main__':
    main()
