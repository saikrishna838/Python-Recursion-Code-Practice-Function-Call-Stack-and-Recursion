def get_sum(numbers, index = 0):
    if index == len(numbers):
        return 0
    else:
        return int(numbers[index]) + get_sum(numbers, index + 1)

numbers = input().split()

sum_of_numbers = get_sum(numbers)# Call the get_sum function
print(sum_of_numbers)