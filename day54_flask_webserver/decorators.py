def reversing(fxn):
    def wrapper(arg):
        fxn(arg[::-1])

    return wrapper


def print_string(string):
    print(string)


@reversing
def print_string_r(string):
    print(string)

print_string("BATMAN\n\n")
print_string_r("BATMAN")