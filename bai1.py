T = int(input())
results = []
for _ in range(T):
    s = input()
    current_number = ""
    numbers = []
    for char in s:
        if char.isdigit():
            current_number += char
        else:
            if current_number:
                numbers.append(int(current_number))
                current_number = ""
    if current_number:
        numbers.append(int(current_number))
    results.append(min(numbers))
for result in results:
    print(result)