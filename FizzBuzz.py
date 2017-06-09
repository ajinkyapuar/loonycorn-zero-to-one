# % by 3 Fizz
# % by 5 Buzz
# % by 3 & 5 FizzBuzz

# For instance, the result will look something like this for 1 to 20.

# 1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz', 16, 17, 'Fizz', 19

['Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i for i in range(1, 20)]
