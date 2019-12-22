from __future__ import annotations

from typing import List

from day_22.data import RAW

CARDS_NUMBER = 10007
TARGET_CARD = 2019


def stack_shuffle(cards: List[int]) -> List[int]:
    return list(reversed(cards))


def cut_shuffle(cards: List[int], n: int) -> List[int]:
    return cards[n:] + cards[:n]


def increment_shuffle(cards: List[int], n: int) -> List[int]:
    new_deck = [None for _ in cards]
    for idx in range(len(cards)):
        new_idx = idx * n % len(cards)
        new_deck[new_idx] = cards[idx]
    return new_deck


def parse_instruction(instruction: str) -> tuple:
    if instruction.startswith('deal with increment'):
        n = instruction.split()[-1]
        return increment_shuffle, (int(n), )

    if instruction.startswith('cut'):
        n = instruction.split()[-1]
        return cut_shuffle, (int(n), )

    if instruction == 'deal into new stack':
        return stack_shuffle, ()

    raise ValueError


def shuffle(cards: List[int], instructions: List[str]) -> List[str]:
    for instruction in instructions:
        func, args = parse_instruction(instruction)
        cards = func(cards, *args)
    return cards


def main():
    cards = [i for i in range(CARDS_NUMBER)]
    instructions = RAW.split('\n')
    cards = shuffle(cards, instructions)
    print(cards.index(TARGET_CARD))


if __name__ == '__main__':
    main()
