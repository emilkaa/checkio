def correct_sentence(text: str) -> str:
    first_letter = text[0].replace(text[0],text[0].upper())
    text = first_letter+text[1:]
    print(text)
    if text[-1] == '.':
        return text
    else:
        text = text.__add__('.')
        print(text)
        return text

if __name__ == '__main__':

    # These "asserts" are used for self-checking and not for an auto-testing
    assert correct_sentence("greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends") == "Greetings, friends."
    assert correct_sentence("Greetings, friends.") == "Greetings, friends."
    assert correct_sentence("hi") == "Hi."
    assert correct_sentence("welcome to New York") == "Welcome to New York."

    print("Coding complete? Click 'Check' to earn cool rewards!")
