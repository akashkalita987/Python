# Question 3: Sum the series \sum_{k=1}^{100} 1/k

series_sum = 0.0
for k in range(1, 101):
    series_sum += 1 / k
print(f"The sum of the series from k=1 to 100 is: {series_sum:.6f}")