def find_smallest(numbers):
    if not numbers:
        return None
    smallest = numbers[0]
    for num in numbers[1:]:
        if num < smallest:
            smallest = num
    return smallest
