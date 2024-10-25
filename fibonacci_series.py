num_ele = int(input("Number of Elemen: "))
first_series = [0,1]
for i in range(2,num_ele):
    next_fib = (first_series[-1]) + (first_series[-2])
    first_series.append(next_fib)
print(first_series)
        
