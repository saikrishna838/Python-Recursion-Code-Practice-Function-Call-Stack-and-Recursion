def get_reversed_string(string):
    if len(string) <= 1:
        return string
    return get_reversed_string(string[1:]) + string[0]

string = input()

resultant_string = get_reversed_string(string)
print(resultant_string)