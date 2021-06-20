def is_all_upper(text: str) -> bool:
    return text == text.upper()
    # lista = text.split(" ")
    # x = len(lista)
    # print(x)
    # i = 0
    # for i <= x:
    #     if lista[i].islower():
    #         i += 1
    #         return False
    #     if lista[i].isdigit():
    #         return False
    #     if lista[i].upper():
    #         return True
    # # if text[i].
    # else:
    #     return True
    # # if text.islower():
    # #     return False
    # # if text.isalnum():
    # #     return True
    # # if text.isdigit():
    # #     return True
    # # if text.istitle():
    # #     return False
    # # if text.isupper():
    # #     return True
    # # else:
    # #     return False


if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('UPPER and lower'))

    # These "asserts" are used for self-checking and not for an auto-testing
    # assert is_all_upper('ALL UPPER') == True
    # assert is_all_upper('all lower') == False
    assert is_all_upper('UPPER and lower') == False
    # assert is_all_upper('') == True
    # assert is_all_upper('     ') == True
    # assert is_all_upper('444') == True
    # assert is_all_upper('55 55 5') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
