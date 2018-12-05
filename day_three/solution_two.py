from utils.get_input import get_from_url


def main():
    input_url = 'https://adventofcode.com/2018/day/3/input'

    fabric_claims = get_from_url(input_url)

    max_x = 1000
    max_y = 1000

    matrix = [[0 for m_x in range(max_x)] for m_y in range(max_y)]

    for fabric_claim in fabric_claims.split('\n'):
        if fabric_claim == '':
            continue
        parts = fabric_claim.split(' @ ')
        claim_id = parts[0]
        parts_two = parts[1].split(': ')
        x, y = parts_two[0].split(',')
        width, length = parts_two[1].split('x')

        x = int(x)
        y = int(y)

        x_2 = x + int(width)
        y_2 = y + int(length)

        # Populate matrix
        for xs in range(x, x_2):
            for ys in range(y, y_2):
                matrix[xs][ys] += 1

    for fabric_claim in fabric_claims.split('\n'):
        if fabric_claim == '':
            continue
        parts = fabric_claim.split(' @ ')
        claim_id = parts[0]
        parts_two = parts[1].split(': ')
        x, y = parts_two[0].split(',')
        width, length = parts_two[1].split('x')

        x = int(x)
        y = int(y)

        x_2 = x + int(width)
        y_2 = y + int(length)

        no_conflict = True
        for xs in range(x, x_2):
            for ys in range(y, y_2):
                if matrix[xs][ys] > 1:
                    no_conflict = False
        if no_conflict:
            no_conflict_id = claim_id

    print(no_conflict_id)


if __name__ == '__main__':
    main()
