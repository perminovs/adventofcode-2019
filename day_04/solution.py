START = 271973
END = 785961


def has_decrease(digits: str) -> bool:
    prev = ''
    for d in digits:
        if prev > d:
            return True
        prev = d
    return False


def has_duplicate(digits: str) -> bool:
    for a, b in zip(digits, digits[1:]):
        if a == b:
            return True
    return False


def additional_criteria(digits: str):
    duplicates = {}
    for a, b in zip(digits, digits[1:]):
        if a == b:
            if a in duplicates:
                duplicates[a] += 1
            else:
                duplicates[a] = 2

    for cnt in duplicates.values():
        if cnt == 2:
            return True
    return False


def good_password_v1(number: int) -> bool:
    digits = str(number)
    return not has_decrease(digits) and has_duplicate(digits)


def good_password_v2(number: int) -> bool:
    digits = str(number)
    return not has_decrease(digits) and additional_criteria(digits)


def main():
    cnt_v1 = sum(good_password_v1(number) for number in range(START, END + 1))
    print(cnt_v1)
    cnt_v2 = sum(good_password_v2(number) for number in range(START, END + 1))
    print(cnt_v2)


if __name__ == '__main__':
    main()
