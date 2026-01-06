def calculate_power(x, y):
    if y == 1:
        return x
    else:
        y -= 1
        return x * calculate_power(x, y)


a = int(input())
b = int(input())
result = calculate_power(a, b)
print(result)
