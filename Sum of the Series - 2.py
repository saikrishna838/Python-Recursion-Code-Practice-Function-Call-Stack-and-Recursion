def get_sum_of_series(number, number_of_terms):
    
    if number_of_terms == 1:
        return number
        
    return number + get_sum_of_series(number - 2, number_of_terms - 1)
    
number = int(input())
number_of_terms = int(input())


series_sum = get_sum_of_series(number, number_of_terms)
print(series_sum)