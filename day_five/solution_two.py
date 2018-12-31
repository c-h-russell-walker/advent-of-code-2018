from utils.get_input import get_from_url


def main():
    input_url = 'https://adventofcode.com/2018/day/5/input'

    polymer_input = get_from_url(input_url).strip()

    def _reduce_polymer(polymer):
        idx = 0
        while idx < len(polymer):
            char = polymer[idx]
            if idx == 0:
                prev_char = polymer[0]
                idx += 1
                continue
            else:
                prev_char = polymer[idx - 1]
            if not isinstance(char, str):
                raise Exception('Not a letter! {}'.format(char))
            if char.lower() == prev_char.lower() and char != prev_char:
                polymer = polymer[:idx - 1] + polymer[idx + 1:]
                # Minus two for deletions and one more to account for incrementing below
                idx = idx - 3
                if idx < 0:
                    idx = 0

            prev_char = char
            idx += 1
        return polymer

    all_units = set([char.lower() for char in polymer_input])

    lengths = {u: 0 for u in all_units}

    for unit in all_units:
        print('Removing unit: {}'.format(unit))
        polymer = polymer_input.replace(unit, '').replace(unit.upper(), '')
        print('Length at start: {}'.format(len(polymer)))
        final_polymer = _reduce_polymer(polymer)
        print(len(final_polymer))
        lengths[unit] = len(final_polymer)

    shortest = min([v for k, v in lengths.items() if v > 0])
    print('Smallest length: {}'.format(shortest))


if __name__ == '__main__':
    main()
