numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
           11, 12, 13, 14, 15, 16, 17, 18]
sum_of_even = 0
for number in numbers:
    if number  % 2 ==0:
        sum_of_even += number
print(f"The sum of even numbers is {sum_of_even}")
sum_of_all_numbers=0
for i in numbers:
    if i % 1==0:
        sum_of_all_numbers+=i
print(f"The sum of all numbers is {sum_of_all_numbers}")


