import re
def between_markers(text: str, begin: str, end: str) -> str:

    result = print_string(text,begin,end)
    return result

def print_string(text,start_digit,end_digit):
    start = text.index(start_digit)
    end = text.index(end_digit)
    print(text[start:end])
    return text[start+1:end]

if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers('What is [apple]', '[', ']') == "apple"
    assert between_markers('What is ><', '>', '<') == ""
    assert between_markers('>apple<', '>', '<') == "apple"
    print('Wow, you are doing pretty good. Time to check it!')
