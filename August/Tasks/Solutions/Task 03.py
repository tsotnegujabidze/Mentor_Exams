def make_number_longer(number):
    num_str = str(number)
    lenght = len(num_str)
    part = []

    for something in range(lenght):
        number = num_str[something]
        if number != '0':
            value = 10 ** (lenght - something - 1)
            part.append(str(int(number) * value))
    return ' + '.join(part)

print(make_number_longer(70304)) # '70000 + 300 + 4'
print(make_number_longer(42)) # '40 + 2'
print(make_number_longer(710163)) # '700000 + 10000 + 100 + 60 + 3'
print(make_number_longer(853546)) # '800000 + 50000 + 3000 + 500 + 40 + 6'
print(make_number_longer(511604)) # '500000 + 10000 + 1000 + 600 + 4'