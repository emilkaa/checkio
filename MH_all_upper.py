def is_all_upper(text: str) -> bool:
    text = text.split(" ")
    output = ""
    for i in text:
        output = output.__add__(i)
        print(output)
    if output.__eq__(""):
        return True
    elif output.isupper():
        return True
    elif output.isdigit():
        return True
    else:
        return False

if __name__ == '__main__':
    print("Example:")
    print(is_all_upper('ALL UPPER'))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert is_all_upper('ALL UPPER') == True
    assert is_all_upper('all lower') == False
    assert is_all_upper('mixed UPPER and lower') == False
    assert is_all_upper('') == True
    assert is_all_upper('     ') == True
    assert is_all_upper('444') == True
    assert is_all_upper('55 55 5') == True
    print("Coding complete? Click 'Check' to earn cool rewards!")
