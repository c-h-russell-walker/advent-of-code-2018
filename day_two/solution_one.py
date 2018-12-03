from collections import Counter

from utils.get_input import get_from_url


def main():
    input_url = 'https://adventofcode.com/2018/day/2/input'

    boxes = get_from_url(input_url)

    two_count = 0
    three_count = 0

    for box_input in boxes.split('\n'):
        three_found = False
        two_found = False
        for letter, count in Counter(box_input).most_common():
            if not three_found and count == 3:
                three_found = True
                three_count += 1
            elif not two_found and count == 2:
                two_found = True
                two_count += 1
            elif count < 2:
                break

    print('two_count: {}'.format(two_count))
    print('three_count: {}'.format(three_count))

    print(two_count * three_count)


if __name__ == '__main__':
    main()
