def compute_factorial(n):
    if n <= 0:  # Base Case or Termination condition
        return 1 
    else:
        return n * compute_factorial(n - 1) #Recursion
    

num = int(input())
factorial = compute_factorial(num) # Call the compute_factorial function
print(factorial)