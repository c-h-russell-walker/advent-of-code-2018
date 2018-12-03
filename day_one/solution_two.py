from collections import Counter
from itertools import cycle

from utils.get_input import get_from_url


def main():
    input_url = 'https://adventofcode.com/2018/day/1/input'

    drift_input = get_from_url(input_url)

    def _parse_int(x):
        if not x:
            return None
        elif x[0] == '+':
            return int(x[1:])
        else:
            return int(x)

    data_as_list = [
        _parse_int(di)
        for di in drift_input.split('\n')
        if _parse_int(di) is not None
    ]

    list_as_cycle = cycle(data_as_list)

    total_drift = 0
    ctr = Counter()
    ctr[total_drift] += 1

    while True:
        inp = next(list_as_cycle)
        total_drift += inp
        ctr[total_drift] += 1
        if ctr[total_drift] > 1:
            break

    freq, change = ctr.most_common(1)[0]
    print(
        'Freq: {}\nChange: {}'.format(freq, change)
    )


if __name__ == '__main__':
    main()
