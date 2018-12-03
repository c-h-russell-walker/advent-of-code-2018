from utils.get_input import get_from_url


def main():
    input_url = 'https://adventofcode.com/2018/day/1/input'

    drift_input = get_from_url(input_url)

    def _parse_int(x):
        if not x:
            return 0
        elif x[0] == '+':
            return int(x[1:])
        else:
            return int(x)

    total_drift = sum(map(_parse_int, drift_input.split('\n')))

    print(total_drift)


if __name__ == '__main__':
    main()
