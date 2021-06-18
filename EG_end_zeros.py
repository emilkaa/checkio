def end_zeros(num: int) -> int:
    y = str(num)
    end = 0
    i = -1
    if int(y[i]) == 0:
        end = end + 1
        i = i - 1
        return end
    else:
        return end
#    return end


if __name__ == '__main__':
    print("Example:")
    print(end_zeros(0))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
