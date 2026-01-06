def sum_of_the_digits(number): # Recursion Functio
    if number < 10: #Base Case or Termination Condition
        return number 
    else:
        return (number % 10) + sum_of_the_digits(number // 10) #Recursion


number = int(input())
result = sum_of_the_digits(number)
print(result)
