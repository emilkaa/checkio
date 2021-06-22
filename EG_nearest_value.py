import numpy as np


def nearest_value(values: set, one: int) -> int:
    li = list(values)
    li.sort()
    end = li[-1]
    if one in li:
        return one
    if one > end:
        li.sort()
        return end
    else:
        # difference_array = np.absolute(li-one)
        # absolute_difference_function = lambda list_value: abs(li - one)
        # closest_value = min(li, key=absolute_difference_function)
        y = min(li, key=lambda x: abs(x - one))
        return y



if __name__ == '__main__':
    print("Example:")
    print(nearest_value({4, 7, 10, 11, 12, 17}, 100))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert nearest_value({4, 7, 10, 11, 12, 17}, 9) == 10
    assert nearest_value({4, 7, 10, 11, 12, 17}, 8) == 7
    assert nearest_value({4, 8, 10, 11, 12, 17}, 9) == 8
    assert nearest_value({4, 9, 10, 11, 12, 17}, 9) == 9
    assert nearest_value({4, 7, 10, 11, 12, 17}, 0) == 4
    assert nearest_value({4, 7, 10, 11, 12, 17}, 100) == 17
    assert nearest_value({5, 10, 8, 12, 89, 100}, 7) == 8
    assert nearest_value({-1, 2, 3}, 0) == -1
    print("Coding complete? Click 'Check' to earn cool rewards!")
