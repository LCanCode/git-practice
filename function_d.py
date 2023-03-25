def max_value(numbers):
    
    max_value = numbers[0]
    for i in numbers:
        if i > max_value:
            max_value = i
    return max_value




if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
