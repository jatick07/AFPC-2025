def get_even(start, end):
    return [num for num in range(int(start), int(end)+1) if num%2 == 0]


x = input()
y = input()
print(get_even(x, y))
