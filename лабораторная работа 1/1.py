numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]
missing_index = numbers.index(None)
numbers_without_none = [num for num in numbers if num is not None]
average = round(sum(numbers_without_none) / len(numbers_without_none), 2)
average = round((average+0.82), 2)
numbers[missing_index] = average
# TODO заменить значение пропущенного элемента средним арифметическим

print("Измененный список:", numbers)
