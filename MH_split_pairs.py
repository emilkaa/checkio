from textwrap import wrap
def split_pairs(a):
    print(len(a))
    if len(a) % 2:
        print("Nieparzysta")
        a = a.__add__("_")
    else:
        print("Parzysta")
    print(a)
    x = wrap(a, 2)
    print(x)
    return x



if __name__ == '__main__':
    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(split_pairs('abcd')) == ['ab', 'cd']
    assert list(split_pairs('abc')) == ['ab', 'c_']
    assert list(split_pairs('abcdf')) == ['ab', 'cd', 'f_']
    assert list(split_pairs('a')) == ['a_']
    assert list(split_pairs('')) == []
    print("Coding complete? Click 'Check' to earn cool rewards!")
