from utils.get_input import get_from_url


def main():
    input_url = 'https://adventofcode.com/2018/day/2/input'

    boxes = get_from_url(input_url)

    for base_idx, inp in enumerate(boxes.split('\n')):
        for idx, compare_inp in enumerate(boxes.split('\n')):
            mismatch_count = 0
            mismatch_idx = None
            if base_idx != idx:
                for new_idx, (char_1, char_2) in enumerate(zip(inp, compare_inp)):
                    if char_1 != char_2:
                        mismatch_count += 1
                        mismatch_idx = new_idx
                    if mismatch_count > 1:
                        break
                    if new_idx + 1 == len(compare_inp) and mismatch_count == 1:
                        answer = []
                        for answer_idx, char in enumerate(inp):
                            if answer_idx != mismatch_idx:
                                answer.append(char)
                        print(''.join(answer))
                        exit()


if __name__ == '__main__':
    main()
