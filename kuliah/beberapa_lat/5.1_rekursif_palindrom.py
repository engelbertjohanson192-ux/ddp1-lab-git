def is_palindrom (str) :
    if len(str) <= 1 :
        return False
    if str [0] != str [-1] :
        return False
    return is_palindrom (str[1:-1])
