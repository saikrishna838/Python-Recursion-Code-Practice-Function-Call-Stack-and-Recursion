def get_sum_of_squares(numbers):
    total = sum(int(char) ** 2 for char in numbers.split())
    return total



    
numbers = input()
squares_sum = get_sum_of_squares(numbers) # Call the get_sum_of_squares function
print(squares_sum)