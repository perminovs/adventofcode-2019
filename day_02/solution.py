from typing import Sequence, Optional, List, Tuple

raw_data = """1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,19,5,23,2,13,23,27,1
,10,27,31,2,6,31,35,1,9,35,39,2,10,39,43,1,43,9,47,1,47,9,51,2,10,51,55,1,55,
9,59,1,59,5,63,1,63,6,67,2,6,67,71,2,10,71,75,1,75,5,79,1,9,79,83,2,83,10,87,
1,87,6,91,1,13,91,95,2,10,95,99,1,99,6,103,2,13,103,107,1,107,2,111,1,111,9,0,
99,2,14,0,0"""


PACK_SIZE = 4
PLUS_OP_CODE = 1
MULT_OP_CODE = 2
END_OP_CODE = 99


def get_packet(idx: int, encounters: Sequence[int]) -> Optional[Sequence[int]]:
    start_position = idx * PACK_SIZE
    if encounters[start_position] == END_OP_CODE:
        return None

    end_position = start_position + PACK_SIZE
    return encounters[start_position:end_position]


def solve(encounters: List[int]) -> None:
    idx = 0
    packet = get_packet(idx, encounters)
    while packet is not None:
        op_code, op1_idx, op2_idx, result_idx = packet
        if op_code == PLUS_OP_CODE:
            encounters[result_idx] = encounters[op1_idx] + encounters[op2_idx]
        elif op_code == MULT_OP_CODE:
            encounters[result_idx] = encounters[op1_idx] * encounters[op2_idx]
        else:
            raise ValueError(f'cannot proceed {op_code} at {idx} iteration')

        idx += 1
        packet = get_packet(idx, encounters)


def bruteforce(encounters, expected) -> Optional[Tuple[int, int]]:
    for i in range(100):
        for j in range(100):
            encts = encounters[:]
            encts[1] = i
            encts[2] = j
            solve(encts)
            if encts[0] == expected:
                return i, j
    return None


def main():
    g = (s for s in raw_data.replace('\n', '').split(',') if s)
    encounters = list(map(int, g))
    # encounters[1] = 12
    # encounters[2] = 2
    # solve(encounters)
    # print(encounters[0])
    answer = bruteforce(encounters, expected=19690720)
    if not answer:
        return
    noun, verb = answer
    print(100 * noun + verb)


if __name__ == '__main__':
    main()
