def file_stat():
    numbers = []
    with open(input(), encoding="UTF-8") as file_in:
        lines = file_in.readlines()
        for line in lines:
            line = line.rstrip('\n').split()
            numbers.extend(map(int, line))

            # TODO: Все параметры лучше
            #  здесь реализовать, в одном цикле

    count_digits = len(numbers)
    positive = len(list(filter(lambda x: x > 0, numbers)))
    total = sum(numbers)
    average = round(total / count_digits, 2)
    print(count_digits,
          positive,
          min(numbers),
          max(numbers),
          total,
          average,
          sep='\n')


file_stat()
