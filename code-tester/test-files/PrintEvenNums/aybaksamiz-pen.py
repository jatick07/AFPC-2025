def get_even(start, end):
    num_list = [num for num in range(int(start), int(end)+1)]
    return [num for num in num_list if num%2 == 0]


x = input()
y = input()
print(get_even(x, y))