def arithmetic_mean(numbers):
    if len(numbers) == 0:
        return None
    return sum(numbers) / len(numbers)
numbers = [1, 2, 3, 4, 5]
mean = arithmetic_mean(numbers)
print (mean)