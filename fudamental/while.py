number = 0
while number < 10:
    if number == 5:
        continue
    print("The number is", number)
    number += 2
else:
    print("the last number is", number)
