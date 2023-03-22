def first():
    x = 2
    def try_again():
        nonlocal x
        x = 2
    return try_again
first()()