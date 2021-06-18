def end_zeros(num: int) -> int:
    y = str(num)
    x = ""
    x = x.__add__(''.join(reversed(y)))
    output = 0
    #pętla zliczająca odwóconego string i zlicza 0 od początku
    for i in x:
        if i == "0":
            output += 1
        else:
            break
    return output

    # best solution: return len(str(n)) - len(str(n).rstrip('0'))
    # pierw długośc jako string później od prawej slicza ilość '0'



if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for an auto-testing
    assert end_zeros(0) == 1
    assert end_zeros(1) == 0
    assert end_zeros(10) == 1
    assert end_zeros(101) == 0
    assert end_zeros(245) == 0
    assert end_zeros(100100) == 2
    print("Coding complete? Click 'Check' to earn cool rewards!")
