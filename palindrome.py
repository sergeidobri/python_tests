def is_palindrome(phrase: str) -> bool:
    if type(phrase) is not str:
        raise TypeError("Палиндром - это, в первую очередь, строка")
    
    result = phrase.strip().replace(' ', '').lower()
    return result == result[::-1]